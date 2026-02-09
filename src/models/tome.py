"""Tome model for basic Tome information."""

from typing import Any

from pydantic import BaseModel, Field, HttpUrl, field_validator

from src.config import VALID_CATEGORIES
from src.utils.roman_numerals import int_to_roman


class Tome(BaseModel):
    """Basic Tome information for listing.
    
    Attributes:
        name: Tome name (e.g., "Nature's Wrath")
        tier: Tome tier as integer (1-7)
        category: Tome category (one of 7 main types)
        link: Wiki page URL
        affinity: List of affinity elements
    """
    
    name: str = Field(..., description="Tome name")
    tier: int = Field(..., ge=1, le=7, description="Tome tier (1-7)")
    category: str = Field(..., description="Tome category (one of 7 main types)")
    link: HttpUrl = Field(..., description="Wiki page URL")
    affinity: list[str] = Field(default_factory=list, description="Affinity elements")
    
    @field_validator("category")
    @classmethod
    def validate_category(cls, v: str) -> str:
        """Validate that category is one of the 7 valid categories."""
        if v not in VALID_CATEGORIES:
            raise ValueError(
                f"Invalid category: {v}. Must be one of: {', '.join(VALID_CATEGORIES)}"
            )
        return v
    
    @property
    def tier_roman(self) -> str:
        """Get tier as Roman numeral."""
        return int_to_roman(self.tier)
    
    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for caching."""
        return {
            "name": self.name,
            "tier": self.tier,
            "category": self.category,
            "link": str(self.link),
            "affinity": self.affinity,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Tome":
        """Create Tome from dictionary (e.g., from cache)."""
        return cls(**data)
