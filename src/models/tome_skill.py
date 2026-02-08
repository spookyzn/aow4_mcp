"""TomeSkill model for skill information."""

from typing import Any

from pydantic import BaseModel, Field, field_validator


class TomeSkill(BaseModel):
    """Skill provided by a Tome.
    
    Attributes:
        name: Skill name
        tier: Skill tier (1-10)
        type: List of skill types (e.g., ["Battle Magic", "Summoning"])
        effects: List of skill effect descriptions
        units: List of unlockable unit types or None
    """
    
    name: str = Field(..., description="Skill name")
    tier: int = Field(..., ge=1, le=10, description="Skill tier (1-10)")
    type: str = Field(..., description="Skill types")
    effects: str = Field(..., description="Skill effects")
    
    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for caching."""
        return {
            "name": self.name,
            "tier": self.tier,
            "type": self.type,
            "effects": self.effects,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TomeSkill":
        """Create TomeSkill from dictionary."""
        return cls(**data)
