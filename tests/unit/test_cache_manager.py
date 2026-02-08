"""Tests for CacheManager."""

import pytest
import fakeredis

from src.services.cache_manager import CacheManager
from src.exceptions import CacheError


@pytest.fixture
def fake_cache() -> CacheManager:
    """Create a CacheManager with fake Redis for testing."""
    fake_redis = fakeredis.FakeRedis(decode_responses=True)
    cache = CacheManager.__new__(CacheManager)
    cache._redis = fake_redis
    return cache


class TestCacheManager:
    """Test cases for CacheManager."""
    
    def test_get_tome_list_empty(self, fake_cache: CacheManager) -> None:
        """Test getting Tome list when cache is empty."""
        result = fake_cache.get_tome_list()
        assert result is None
    
    def test_set_and_get_tome_list(self, fake_cache: CacheManager) -> None:
        """Test setting and getting Tome list."""
        tomes = [
            {"name": "Nature's Wrath", "tier": 3, "category": "Nature"},
            {"name": "Chaos Storm", "tier": 2, "category": "Chaos"},
        ]
        fake_cache.set_tome_list(tomes)
        
        result = fake_cache.get_tome_list()
        assert result == tomes
    
    def test_get_tome_detail_empty(self, fake_cache: CacheManager) -> None:
        """Test getting Tome detail when cache is empty."""
        result = fake_cache.get_tome_detail("Nature's Wrath")
        assert result is None
    
    def test_set_and_get_tome_detail(self, fake_cache: CacheManager) -> None:
        """Test setting and getting Tome detail."""
        detail = {
            "name": "Nature's Wrath",
            "tier": 3,
            "category": "Nature",
            "summary": "A powerful nature tome",
            "tome_skills": [],
            "tome_info": {},
        }
        fake_cache.set_tome_detail("Nature's Wrath", detail)
        
        result = fake_cache.get_tome_detail("Nature's Wrath")
        assert result == detail
    
    def test_multiple_tome_details(self, fake_cache: CacheManager) -> None:
        """Test caching multiple Tome details."""
        detail1 = {"name": "Nature's Wrath", "tier": 3, "category": "Nature"}
        detail2 = {"name": "Chaos Storm", "tier": 2, "category": "Chaos"}
        
        fake_cache.set_tome_detail("Nature's Wrath", detail1)
        fake_cache.set_tome_detail("Chaos Storm", detail2)
        
        assert fake_cache.get_tome_detail("Nature's Wrath") == detail1
        assert fake_cache.get_tome_detail("Chaos Storm") == detail2
    
    def test_clear_cache(self, fake_cache: CacheManager) -> None:
        """Test clearing all cache entries."""
        # Set some data
        fake_cache.set_tome_list([{"name": "Test", "tier": 1}])
        fake_cache.set_tome_detail("Test", {"name": "Test"})
        
        # Clear cache
        fake_cache.clear_cache()
        
        # Verify all cleared
        assert fake_cache.get_tome_list() is None
        assert fake_cache.get_tome_detail("Test") is None
    
    def test_tome_detail_with_special_characters(self, fake_cache: CacheManager) -> None:
        """Test caching Tome details with special characters in name."""
        detail = {"name": "Nature's Wrath (Enhanced)", "tier": 4}
        fake_cache.set_tome_detail("Nature's Wrath (Enhanced)", detail)
        
        result = fake_cache.get_tome_detail("Nature's Wrath (Enhanced)")
        assert result == detail
