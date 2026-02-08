"""Tests for Tome model."""

import pytest
from pydantic import ValidationError

from src.models.tome import Tome
from src.config import VALID_CATEGORIES


class TestTomeModel:
    """Test cases for Tome Pydantic model."""
    
    def test_valid_tome_creation(self) -> None:
        """Test creating a valid Tome instance."""
        tome = Tome(
            name="Nature's Wrath",
            tier=3,
            category="Nature",
            link="https://aow4.paradoxwikis.com/Nature's_Wrath"
        )
        assert tome.name == "Nature's Wrath"
        assert tome.tier == 3
        assert tome.category == "Nature"
    
    def test_all_valid_categories(self) -> None:
        """Test creating Tomes with all 7 valid categories."""
        for i, category in enumerate(VALID_CATEGORIES, 1):
            tome = Tome(
                name=f"Test {category}",
                tier=i,
                category=category,
                link=f"https://example.com/{category}"
            )
            assert tome.category == category
    
    def test_invalid_category(self) -> None:
        """Test that invalid category raises ValidationError."""
        with pytest.raises(ValidationError, match="Invalid category"):
            Tome(
                name="Invalid Tome",
                tier=1,
                category="Other Tomes",  # Invalid category
                link="https://example.com/test"
            )
    
    def test_tier_out_of_range(self) -> None:
        """Test that tier outside 1-7 raises ValidationError."""
        with pytest.raises(ValidationError):
            Tome(
                name="Invalid Tier",
                tier=8,  # Too high
                category="Nature",
                link="https://example.com/test"
            )
        
        with pytest.raises(ValidationError):
            Tome(
                name="Invalid Tier",
                tier=0,  # Too low
                category="Nature",
                link="https://example.com/test"
            )
    
    def test_invalid_url(self) -> None:
        """Test that invalid URL raises ValidationError."""
        with pytest.raises(ValidationError):
            Tome(
                name="Invalid URL",
                tier=1,
                category="Nature",
                link="not-a-valid-url"
            )
    
    def test_tier_roman_property(self) -> None:
        """Test tier_roman property returns correct Roman numeral."""
        test_cases = [
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (5, "V"),
            (6, "VI"),
            (7, "VII"),
        ]
        for tier, expected_roman in test_cases:
            tome = Tome(
                name="Test",
                tier=tier,
                category="Nature",
                link="https://example.com/test"
            )
            assert tome.tier_roman == expected_roman
    
    def test_to_dict(self) -> None:
        """Test conversion to dictionary."""
        tome = Tome(
            name="Nature's Wrath",
            tier=3,
            category="Nature",
            link="https://aow4.paradoxwikis.com/Nature's_Wrath"
        )
        data = tome.to_dict()
        assert data["name"] == "Nature's Wrath"
        assert data["tier"] == 3
        assert data["category"] == "Nature"
        assert data["link"] == "https://aow4.paradoxwikis.com/Nature's_Wrath"
    
    def test_from_dict(self) -> None:
        """Test creation from dictionary."""
        data = {
            "name": "Nature's Wrath",
            "tier": 3,
            "category": "Nature",
            "link": "https://aow4.paradoxwikis.com/Nature's_Wrath"
        }
        tome = Tome.from_dict(data)
        assert tome.name == "Nature's Wrath"
        assert tome.tier == 3
        assert tome.category == "Nature"
