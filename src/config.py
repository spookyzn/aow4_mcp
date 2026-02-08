"""Configuration settings for AOW4 Tome Scraper."""

import os
from typing import Final

# Redis Configuration
REDIS_URL: Final[str] = os.getenv("AOW4_REDIS_URL", "redis://localhost:6379/0")
REDIS_TIMEOUT: Final[int] = int(os.getenv("AOW4_TIMEOUT", "30"))

# Cache Keys
CACHE_KEY_TOME_LIST: Final[str] = "aow4:tome:list"
CACHE_KEY_TOME_DETAIL_PREFIX: Final[str] = "aow4:tome:detail:"

# Wiki URLs
WIKI_BASE_URL: Final[str] = "https://aow4.paradoxwikis.com"
WIKI_TOMES_URL: Final[str] = f"{WIKI_BASE_URL}/Tomes"

# Playwright Configuration
PLAYWRIGHT_HEADLESS: Final[bool] = os.getenv("AOW4_HEADLESS", "true").lower() == "true"
PLAYWRIGHT_TIMEOUT: Final[int] = int(os.getenv("AOW4_TIMEOUT", "30")) * 1000  # milliseconds

# Valid Tome Categories (7 main categories)
VALID_CATEGORIES: Final[list[str]] = [
    "Nature",
    "Chaos",
    "Order",
    "Shadow",
    "Astral",
    "Hybrid",
    "Materium",
]

# Unit Types for Tome Skills
UNIT_TYPES: Final[list[str]] = [
    "Shield",
    "Fighter",
    "Shock",
    "Ranged",
    "Support",
    "Cavalry",
    "Flying",
    "Siege",
]
