"""pytest fixtures for AOW4 Tome Scraper tests."""

import pytest
from unittest.mock import MagicMock

import fakeredis


@pytest.fixture
def fake_redis():
    """Create a fake Redis instance for testing."""
    return fakeredis.FakeRedis(decode_responses=True)


@pytest.fixture
def mock_cache_manager(fake_redis):
    """Create a mock CacheManager with fake Redis."""
    from src.services.cache_manager import CacheManager
    
    cache = MagicMock(spec=CacheManager)
    cache._redis = fake_redis
    return cache


@pytest.fixture
def sample_tome_dict():
    """Return a sample tome dictionary for testing."""
    return {
        "name": "Nature's Wrath",
        "tier": 3,
        "category": "Nature",
        "link": "https://aow4.paradoxwikis.com/Nature's_Wrath",
    }


@pytest.fixture
def sample_tome_detail_dict():
    """Return a sample tome detail dictionary for testing."""
    return {
        "name": "Nature's Wrath",
        "tier": 3,
        "category": "Nature",
        "summary": "A powerful nature tome focused on aggressive magic.",
        "tome_skills": [
            {
                "name": "Entangling Vines",
                "tier": 1,
                "type": ["Battle Magic"],
                "effects": ["Immobilizes enemy units"],
                "units": None,
            }
        ],
        "tome_info": {
            "Tier": "III",
            "Type": "Nature",
        },
    }
