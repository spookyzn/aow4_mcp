"""Tests for TomeSkill and TomeDetail models."""

import pytest
from pydantic import ValidationError

from src.models.tome_skill import TomeSkill
from src.models.tome_detail import TomeDetail
from src.config import VALID_CATEGORIES, UNIT_TYPES


class TestTomeSkillModel:
    """Test cases for TomeSkill model."""
    
    def test_valid_skill_creation(self) -> None:
        """Test creating a valid TomeSkill."""
        skill = TomeSkill(
            name="Entangling Vines",
            tier=1,
            type=["Battle Magic"],
            effects=["Immobilizes enemy units"],
        )
        assert skill.name == "Entangling Vines"
        assert skill.tier == 1
        assert skill.units is None
    
    def test_skill_with_units(self) -> None:
        """Test creating a skill with unlockable units."""
        skill = TomeSkill(
            name="Summon Treant",
            tier=3,
            type=["Summoning", "Nature"],
            effects=["Summons a Treant unit", "Lasts 3 turns"],
            units=["Support"],
        )
        assert skill.units == ["Support"]
    
    def test_invalid_unit_type(self) -> None:
        """Test that invalid unit type raises ValidationError."""
        with pytest.raises(ValidationError, match="Invalid unit type"):
            TomeSkill(
                name="Test Skill",
                tier=1,
                type=["Battle Magic"],
                effects=["Test effect"],
                units=["InvalidUnit"],
            )
    
    def test_all_valid_unit_types(self) -> None:
        """Test creating skills with all valid unit types."""
        for unit_type in UNIT_TYPES:
            skill = TomeSkill(
                name=f"Summon {unit_type}",
                tier=1,
                type=["Summoning"],
                effects=[f"Summons a {unit_type} unit"],
                units=[unit_type],
            )
            assert unit_type in skill.units
    
    def test_empty_type_list(self) -> None:
        """Test that empty type list raises ValidationError."""
        with pytest.raises(ValidationError, match="too_short"):
            TomeSkill(
                name="Test Skill",
                tier=1,
                type=[],  # Empty
                effects=["Test effect"],
            )

    def test_empty_effects_list(self) -> None:
        """Test that empty effects list raises ValidationError."""
        with pytest.raises(ValidationError, match="too_short"):
            TomeSkill(
                name="Test Skill",
                tier=1,
                type=["Battle Magic"],
                effects=[],  # Empty
            )
    
    def test_to_dict(self) -> None:
        """Test conversion to dictionary."""
        skill = TomeSkill(
            name="Test Skill",
            tier=2,
            type=["Type1", "Type2"],
            effects=["Effect1", "Effect2"],
            units=["Shield", "Fighter"],
        )
        data = skill.to_dict()
        assert data["name"] == "Test Skill"
        assert data["tier"] == 2
        assert data["type"] == ["Type1", "Type2"]
        assert data["effects"] == ["Effect1", "Effect2"]
        assert data["units"] == ["Shield", "Fighter"]
    
    def test_from_dict(self) -> None:
        """Test creation from dictionary."""
        data = {
            "name": "Test Skill",
            "tier": 2,
            "type": ["Type1"],
            "effects": ["Effect1"],
            "units": None,
        }
        skill = TomeSkill.from_dict(data)
        assert skill.name == "Test Skill"
        assert skill.units is None


class TestTomeDetailModel:
    """Test cases for TomeDetail model."""
    
    def test_valid_detail_creation(self) -> None:
        """Test creating a valid TomeDetail."""
        detail = TomeDetail(
            name="Nature's Wrath",
            tier=3,
            category="Nature",
            summary="A powerful nature tome focused on aggressive magic.",
            tome_skills=[
                TomeSkill(
                    name="Entangling Vines",
                    tier=1,
                    type=["Battle Magic"],
                    effects=["Immobilizes enemies"],
                )
            ],
            tome_info={"Tier": "III", "Type": "Nature"},
        )
        assert detail.name == "Nature's Wrath"
        assert len(detail.tome_skills) == 1
    
    def test_all_valid_categories(self) -> None:
        """Test creating TomeDetail with all 7 valid categories."""
        for category in VALID_CATEGORIES:
            detail = TomeDetail(
                name=f"Test {category}",
                tier=1,
                category=category,
                summary=f"A {category} tome.",
            )
            assert detail.category == category
    
    def test_invalid_category(self) -> None:
        """Test that invalid category raises ValidationError."""
        with pytest.raises(ValidationError, match="Invalid category"):
            TomeDetail(
                name="Invalid",
                tier=1,
                category="Other Tomes",  # Invalid
                summary="Test summary.",
            )
    
    def test_empty_summary(self) -> None:
        """Test that empty summary raises ValidationError."""
        with pytest.raises(ValidationError, match="too_short"):
            TomeDetail(
                name="Invalid",
                tier=1,
                category="Nature",
                summary="",  # Empty
            )
    
    def test_whitespace_only_summary(self) -> None:
        """Test that whitespace-only summary raises ValidationError."""
        with pytest.raises(ValidationError, match="Summary must not be empty"):
            TomeDetail(
                name="Invalid",
                tier=1,
                category="Nature",
                summary="   ",  # Whitespace only
            )
    
    def test_empty_skills_list(self) -> None:
        """Test that empty skills list is allowed."""
        detail = TomeDetail(
            name="Test",
            tier=1,
            category="Nature",
            summary="Test summary.",
            tome_skills=[],  # Empty is allowed
        )
        assert detail.tome_skills == []
    
    def test_to_dict(self) -> None:
        """Test conversion to dictionary."""
        detail = TomeDetail(
            name="Nature's Wrath",
            tier=3,
            category="Nature",
            summary="A powerful nature tome.",
            tome_skills=[
                TomeSkill(
                    name="Test Skill",
                    tier=1,
                    type=["Battle Magic"],
                    effects=["Test effect"],
                )
            ],
            tome_info={"Tier": "III"},
        )
        data = detail.to_dict()
        assert data["name"] == "Nature's Wrath"
        assert data["tier"] == 3
        assert data["tome_info"] == {"Tier": "III"}
        assert len(data["tome_skills"]) == 1
    
    def test_from_dict(self) -> None:
        """Test creation from dictionary."""
        data = {
            "name": "Nature's Wrath",
            "tier": 3,
            "category": "Nature",
            "summary": "A powerful nature tome.",
            "tome_skills": [
                {
                    "name": "Test Skill",
                    "tier": 1,
                    "type": ["Battle Magic"],
                    "effects": ["Test effect"],
                    "units": None,
                }
            ],
            "tome_info": {"Tier": "III"},
        }
        detail = TomeDetail.from_dict(data)
        assert detail.name == "Nature's Wrath"
        assert len(detail.tome_skills) == 1
        assert isinstance(detail.tome_skills[0], TomeSkill)
