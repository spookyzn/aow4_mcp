"""TomeDetail model for full Tome information."""

from typing import Any

from pydantic import BaseModel, Field, field_validator

from src.config import VALID_CATEGORIES
from src.models.tome_skill import TomeSkill


class TomeDetail(BaseModel):
    """Detailed Tome information.
    
    Attributes:
        name: Tome name
        tier: Tome tier (1-7)
        category: Tome category
        summary: Tome description text
        tome_skills: List of skills provided by this Tome
        tome_info: Additional info from sidebar (tier, type, unlocks, etc.)
    """
    
    name: str = Field(..., description="Tome name")
    tier: int = Field(..., ge=1, le=7, description="Tome tier (1-7)")
    category: str = Field(..., description="Tome category")
    summary: str = Field(..., min_length=1, description="Tome description")
    tome_skills: list[TomeSkill] = Field(
        default_factory=list,
        description="Tome skills"
    )
    tome_info: list[str] = Field(default_factory=list, description="Additional info from sidebar")
    
    @field_validator("category")
    @classmethod
    def validate_category(cls, v: str) -> str:
        """Validate that category is one of the 7 valid categories."""
        if v not in VALID_CATEGORIES:
            raise ValueError(
                f"Invalid category: {v}. Must be one of: {', '.join(VALID_CATEGORIES)}"
            )
        return v
    
    @field_validator("summary")
    @classmethod
    def validate_summary(cls, v: str) -> str:
        """Validate that summary is not empty."""
        if not v or len(v.strip()) == 0:
            raise ValueError("summary: Summary must not be empty")
        return v
    
    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for caching."""
        return {
            "name": self.name,
            "tier": self.tier,
            "category": self.category,
            "summary": self.summary,
            "tome_skills": [skill.to_dict() for skill in self.tome_skills],
            "tome_info": self.tome_info,
        }
    
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TomeDetail":
        """Create TomeDetail from dictionary."""
        # Convert skill dicts back to TomeSkill objects
        skills_data = data.get("tome_skills", [])
        skills = [TomeSkill.from_dict(skill) for skill in skills_data]
        
        return cls(
            name=data["name"],
            tier=data["tier"],
            category=data["category"],
            summary=data["summary"],
            tome_skills=skills,
            tome_info=data.get("tome_info", []),
        )
