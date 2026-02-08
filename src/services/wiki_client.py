"""Wiki page fetcher using Playwright."""

from typing import Final

from playwright.async_api import async_playwright, Page
from pydantic import HttpUrl

from src.config import PLAYWRIGHT_HEADLESS, PLAYWRIGHT_TIMEOUT, WIKI_BASE_URL
from src.exceptions import WikiError


class WikiClient:
    """Client for fetching and parsing AOW4 Wiki pages."""
    
    def __init__(
        self,
        headless: bool = PLAYWRIGHT_HEADLESS,
        timeout: int = PLAYWRIGHT_TIMEOUT,
    ) -> None:
        """Initialize Wiki client.
        
        Args:
            headless: Whether to run browser in headless mode
            timeout: Page load timeout in milliseconds
        """
        self._headless = headless
        self._timeout = timeout
        self._playwright = None
        self._browser = None
    
    async def __aenter__(self) -> "WikiClient":
        """Async context manager entry."""
        await self._init_browser()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        await self.close()
    
    async def _init_browser(self) -> None:
        """Initialize Playwright browser."""
        try:
            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(
                headless=self._headless
            )
        except Exception as e:
            raise WikiError(
                "Failed to initialize Playwright browser",
                details=str(e)
            ) from e
    
    async def close(self) -> None:
        """Close browser and cleanup resources."""
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
    
    async def fetch_page(self, url: str) -> str:
        """Fetch page content from URL.
        
        Args:
            url: Page URL to fetch
            
        Returns:
            Page HTML content
            
        Raises:
            WikiError: If page cannot be fetched
        """
        if not self._browser:
            await self._init_browser()
        
        page: Page | None = None
        try:
            page = await self._browser.new_page()
            await page.goto(url, timeout=self._timeout, wait_until="networkidle")
            
            # Wait for page content to load
            await page.wait_for_load_state("domcontentloaded")
            
            content = await page.content()
            return content
        except Exception as e:
            raise WikiError(
                f"Failed to fetch page: {url}",
                details=str(e)
            ) from e
        finally:
            if page:
                await page.close()
    
    async def fetch_tomes_page(self) -> str:
        """Fetch the main Tomes list page.
        
        Returns:
            HTML content of the Tomes page
        """
        from src.config import WIKI_TOMES_URL
        return await self.fetch_page(WIKI_TOMES_URL)
    
    async def fetch_tome_detail_page(self, tome_link: HttpUrl) -> str:
        """Fetch a specific Tome detail page.
        
        Args:
            tome_name: Name of the Tome
            
        Returns:
            HTML content of the Tome detail page
        """
        # Convert tome name to URL-safe format
        url = f"{tome_link}"
        return await self.fetch_page(url)
