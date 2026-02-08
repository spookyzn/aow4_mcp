"""Redis cache management for AOW4 Tome Scraper."""

import json
from typing import Any

import redis

from src.config import CACHE_KEY_TOME_DETAIL_PREFIX, CACHE_KEY_TOME_LIST, REDIS_URL
from src.exceptions import CacheError


class CacheManager:
    """Manages Redis cache operations for Tome data.
    
    Cache keys:
    - aow4:tome:list - Stores list of all Tomes
    - aow4:tome:detail:{name} - Stores individual Tome details
    """
    
    def __init__(self, redis_url: str = REDIS_URL) -> None:
        """Initialize cache manager with Redis connection.
        
        Args:
            redis_url: Redis connection URL
        """
        try:
            self._redis = redis.from_url(redis_url, decode_responses=True)
        except redis.ConnectionError as e:
            raise CacheError(
                f"Failed to connect to Redis at {redis_url}",
                details=str(e)
            ) from e
    
    def get_tome_list(self) -> list[dict[str, Any]] | None:
        """Get cached Tome list.
        
        Returns:
            List of Tome dictionaries or None if not cached
        """
        try:
            data = self._redis.get(CACHE_KEY_TOME_LIST)
            if data:
                return json.loads(data)
            return None
        except redis.RedisError as e:
            raise CacheError("Failed to read Tome list from cache", details=str(e)) from e
    
    def set_tome_list(self, tomes: list[dict[str, Any]]) -> None:
        """Cache Tome list. Cache never expires.
        
        Args:
            tomes: List of Tome dictionaries
        """
        try:
            self._redis.set(CACHE_KEY_TOME_LIST, json.dumps(tomes))
        except redis.RedisError as e:
            raise CacheError("Failed to write Tome list to cache", details=str(e)) from e
    
    def get_tome_detail(self, name: str) -> dict[str, Any] | None:
        """Get cached Tome detail.
        
        Args:
            name: Tome name
            
        Returns:
            Tome detail dictionary or None if not cached
        """
        key = f"{CACHE_KEY_TOME_DETAIL_PREFIX}{name}"
        try:
            data = self._redis.get(key)
            if data:
                return json.loads(data)
            return None
        except redis.RedisError as e:
            raise CacheError(
                f"Failed to read Tome detail from cache for {name}",
                details=str(e)
            ) from e
    
    def set_tome_detail(self, name: str, detail: dict[str, Any]) -> None:
        """Cache Tome detail. Cache never expires.
        
        Args:
            name: Tome name
            detail: Tome detail dictionary
        """
        key = f"{CACHE_KEY_TOME_DETAIL_PREFIX}{name}"
        try:
            self._redis.set(key, json.dumps(detail))
        except redis.RedisError as e:
            raise CacheError(
                f"Failed to write Tome detail to cache for {name}",
                details=str(e)
            ) from e
    
    def clear_cache(self) -> None:
        """Clear all Tome-related cache entries."""
        try:
            # Delete Tome list
            self._redis.delete(CACHE_KEY_TOME_LIST)
            
            # Delete all Tome details
            pattern = f"{CACHE_KEY_TOME_DETAIL_PREFIX}*"
            for key in self._redis.scan_iter(match=pattern):
                self._redis.delete(key)
        except redis.RedisError as e:
            raise CacheError("Failed to clear cache", details=str(e)) from e
    
    def close(self) -> None:
        """Close Redis connection."""
        self._redis.close()
