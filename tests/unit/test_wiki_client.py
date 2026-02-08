"""Tests for WikiClient."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from src.services.wiki_client import WikiClient
from src.exceptions import WikiError


class TestWikiClient:
    """Test cases for WikiClient."""
    
    @pytest.mark.asyncio
    async def test_fetch_page_success(self) -> None:
        """Test successful page fetch."""
        mock_page = AsyncMock()
        mock_page.content.return_value = "<html><body>Test Content</body></html>"
        
        mock_browser = AsyncMock()
        mock_browser.new_page.return_value = mock_page
        
        mock_playwright = AsyncMock()
        mock_playwright.chromium.launch.return_value = mock_browser
        
        mock_context = AsyncMock()
        mock_context.__aenter__ = AsyncMock(return_value=mock_playwright)
        mock_context.__aexit__ = AsyncMock(return_value=False)
        
        with patch("src.services.wiki_client.async_playwright", return_value=mock_context):
            client = WikiClient()
            await client._init_browser()
            content = await client.fetch_page("https://example.com/test")
            
            assert "Test Content" in content
            mock_page.goto.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_fetch_page_error(self) -> None:
        """Test page fetch error handling."""
        mock_page = AsyncMock()
        mock_page.goto.side_effect = Exception("Network error")
        
        mock_browser = AsyncMock()
        mock_browser.new_page.return_value = mock_page
        
        mock_playwright = AsyncMock()
        mock_playwright.chromium.launch.return_value = mock_browser
        
        mock_context = AsyncMock()
        mock_context.__aenter__ = AsyncMock(return_value=mock_playwright)
        mock_context.__aexit__ = AsyncMock(return_value=False)
        
        with patch("src.services.wiki_client.async_playwright", return_value=mock_context):
            client = WikiClient()
            await client._init_browser()
            with pytest.raises(WikiError, match="Failed to fetch page"):
                await client.fetch_page("https://example.com/test")
    
    @pytest.mark.asyncio
    async def test_browser_initialization_error(self) -> None:
        """Test browser initialization error handling."""
        with patch("src.services.wiki_client.async_playwright") as mock_pw:
            mock_pw.return_value.start.side_effect = Exception("Browser launch failed")
            
            client = WikiClient()
            with pytest.raises(WikiError, match="Failed to initialize Playwright"):
                await client._init_browser()
    
    @pytest.mark.asyncio
    async def test_context_manager(self) -> None:
        """Test async context manager usage."""
        mock_browser = AsyncMock()
        mock_playwright = AsyncMock()
        mock_playwright.chromium.launch.return_value = mock_browser
        
        mock_context = AsyncMock()
        mock_context.__aenter__ = AsyncMock(return_value=mock_playwright)
        mock_context.__aexit__ = AsyncMock(return_value=False)
        
        with patch("src.services.wiki_client.async_playwright", return_value=mock_context):
            async with WikiClient() as client:
                assert client._browser is not None
            
            # Verify cleanup was called
            mock_browser.close.assert_called_once()
            mock_playwright.stop.assert_called_once()
