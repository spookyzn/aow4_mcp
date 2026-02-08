"""Integration tests for TomeService."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from src.services.tome_service import TomeService
from src.services.cache_manager import CacheManager
from src.models.tome import Tome
from src.models.tome_detail import TomeDetail
from src.exceptions import TomeNotFoundError


class TestTomeServiceIntegration:
    """Integration tests for TomeService with mocked Wiki."""
    
    @pytest.fixture
    def mock_cache(self) -> MagicMock:
        """Create a mock cache manager."""
        cache = MagicMock(spec=CacheManager)
        cache.get_tome_list.return_value = None
        cache.get_tome_detail.return_value = None
        return cache
    
    @pytest.fixture
    def mock_wiki(self) -> AsyncMock:
        """Create a mock wiki client."""
        wiki = AsyncMock()
        return wiki
    
    @pytest.mark.asyncio
    async def test_list_tomes_from_wiki(self, mock_cache: MagicMock) -> None:
        """Test listing tomes fetches from Wiki when cache is empty."""
        html = """
        <html>
        <body>
            <h2>Nature</h2>
            <table>
                <tr><td><a href="/Nature's_Wrath">Nature's Wrath III</a></td><td>III</td></tr>
            </table>
        </body>
        </html>
        """
        mock_wiki = AsyncMock()
        mock_wiki.fetch_tomes_page.return_value = html
        
        service = TomeService(cache_manager=mock_cache, wiki_client=mock_wiki)
        
        tomes = await service.list_tomes()
        
        assert len(tomes) == 1
        assert tomes[0].name == "Nature's Wrath III"
        assert tomes[0].category == "Nature"
        
        # Verify cache was updated
        mock_cache.set_tome_list.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_list_tomes_from_cache(self, mock_cache: MagicMock) -> None:
        """Test listing tomes returns cached data when available."""
        mock_cache.get_tome_list.return_value = [
            {
                "name": "Cached Tome",
                "tier": 2,
                "category": "Nature",
                "link": "https://example.com/test"
            }
        ]
        
        service = TomeService(cache_manager=mock_cache)
        
        tomes = await service.list_tomes()
        
        assert len(tomes) == 1
        assert tomes[0].name == "Cached Tome"
    
    @pytest.mark.asyncio
    async def test_list_tomes_skip_cache(self, mock_cache: MagicMock) -> None:
        """Test listing tomes with use_cache=False fetches from Wiki."""
        html = """
        <html>
        <body>
            <h2>Nature</h2>
            <table>
                <tr><td><a href="/New_Tome">New Tome I</a></td><td>I</td></tr>
            </table>
        </body>
        </html>
        """
        mock_wiki = AsyncMock()
        mock_wiki.fetch_tomes_page.return_value = html
        
        mock_cache.get_tome_list.return_value = [
            {"name": "Cached Tome", "tier": 1, "category": "Nature", "link": "https://example.com"}
        ]
        
        service = TomeService(cache_manager=mock_cache, wiki_client=mock_wiki)
        
        tomes = await service.list_tomes(use_cache=False)
        
        # Should get new data, not cached
        assert len(tomes) == 1
        assert tomes[0].name == "New Tome I"
    
    @pytest.mark.asyncio
    async def test_get_tome_detail_not_found(self, mock_cache: MagicMock) -> None:
        """Test getting detail for non-existent tome raises error."""
        # Mock empty tome list
        mock_wiki = AsyncMock()
        mock_wiki.fetch_tomes_page.return_value = """
        <html><body><h2>Nature</h2><table></table></body></html>
        """
        
        service = TomeService(cache_manager=mock_cache, wiki_client=mock_wiki)
        
        with pytest.raises(TomeNotFoundError, match="not found"):
            await service.get_tome_detail("NonExistent")
    
    def test_refresh_cache(self, mock_cache: MagicMock) -> None:
        """Test refreshing cache clears all cached data."""
        service = TomeService(cache_manager=mock_cache)
        
        service.refresh_cache()
        
        mock_cache.clear_cache.assert_called_once()
    
    def test_get_categories(self) -> None:
        """Test getting valid categories."""
        service = TomeService()
        
        categories = service.get_categories()
        
        assert len(categories) == 7
        assert "Nature" in categories
        assert "Chaos" in categories
        assert "Other Tomes" not in categories
