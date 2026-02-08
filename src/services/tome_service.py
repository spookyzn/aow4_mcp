"""Tome service for fetching and caching Tome data."""

from typing import Any

from src.config import VALID_CATEGORIES
from src.models.tome import Tome
from src.models.tome_detail import TomeDetail
from src.parsers.tome_list_parser import TomeListParser
from src.parsers.tome_detail_parser import TomeDetailParser
from src.services.cache_manager import CacheManager
from src.services.wiki_client import WikiClient
from src.exceptions import TomeNotFoundError


class TomeService:
    """Service for managing Tome data.
    
    Handles fetching from Wiki, caching in Redis, and retrieving Tome information.
    """
    
    def __init__(
        self,
        cache_manager: CacheManager | None = None,
        wiki_client: WikiClient | None = None,
    ) -> None:
        """Initialize Tome service.
        
        Args:
            cache_manager: Optional CacheManager instance
            wiki_client: Optional WikiClient instance
        """
        self._cache = cache_manager or CacheManager()
        self._wiki = wiki_client
        self._list_parser = TomeListParser()
        self._detail_parser = TomeDetailParser()
    
    async def list_tomes(self, use_cache: bool = True) -> list[Tome]:
        """Get list of all Tomes.
        
        Args:
            use_cache: Whether to use cached data if available
            
        Returns:
            List of Tome objects
        """
        # Check cache first
        if use_cache:
            cached = self._cache.get_tome_list()
            if cached:
                return [Tome.from_dict(t) for t in cached]
        
        # Fetch from Wiki
        if not self._wiki:
            self._wiki = WikiClient()
        
        async with self._wiki:
            html = await self._wiki.fetch_tomes_page()
        
        # Parse and filter to 7 categories only
        tomes = self._list_parser.parse(html)
        
        # Cache the results
        self._cache.set_tome_list([t.to_dict() for t in tomes])
        
        return tomes
    
    async def get_tome_detail(
        self,
        name: str,
        use_cache: bool = True,
    ) -> TomeDetail:
        """Get detailed information for a specific Tome.
        
        Args:
            name: Tome name
            use_cache: Whether to use cached data if available
            
        Returns:
            TomeDetail object
            
        Raises:
            TomeNotFoundError: If Tome is not found
        """
        # Check cache first
        if use_cache:
            cached = self._cache.get_tome_detail(name)
            if cached:
                return TomeDetail.from_dict(cached)
        
        # Get tome list to find category and tier
        tomes = await self.list_tomes(use_cache=True)
        tome_info = None
        for t in tomes:
            if t.name.lower() == name.lower():
                tome_info = t
                break
        
        if not tome_info:
            raise TomeNotFoundError(
                f"Tome '{name}' not found. Use --list to see available tomes."
            )
        
        # Fetch detail from Wiki
        if not self._wiki:
            self._wiki = WikiClient()
        
        async with self._wiki:
            html = await self._wiki.fetch_tome_detail_page(tome_info.link)
        
        # Parse detail page
        detail = self._detail_parser.parse(
            html,
            tome_info.name,
            tome_info.category,
            tome_info.tier,
        )
        
        # Cache the result
        self._cache.set_tome_detail(name, detail.to_dict())
        
        return detail
    
    def refresh_cache(self) -> None:
        """Clear all cached Tome data."""
        self._cache.clear_cache()
    
    def get_categories(self) -> list[str]:
        """Get list of valid Tome categories.
        
        Returns:
            List of category names
        """
        return VALID_CATEGORIES.copy()
