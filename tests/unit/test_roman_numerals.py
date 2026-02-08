"""Tests for Roman numeral conversion utilities."""

import pytest

from src.utils.roman_numerals import int_to_roman, roman_to_int


class TestRomanToInt:
    """Test cases for roman_to_int function."""
    
    def test_all_valid_roman_numerals(self) -> None:
        """Test conversion of all valid Roman numerals I-VII."""
        test_cases = [
            ("I", 1),
            ("II", 2),
            ("III", 3),
            ("IV", 4),
            ("V", 5),
            ("VI", 6),
            ("VII", 7),
        ]
        for roman, expected in test_cases:
            assert roman_to_int(roman) == expected
    
    def test_lowercase_input(self) -> None:
        """Test that lowercase Roman numerals are accepted."""
        assert roman_to_int("i") == 1
        assert roman_to_int("iv") == 4
        assert roman_to_int("vii") == 7
    
    def test_whitespace_handling(self) -> None:
        """Test that whitespace is stripped from input."""
        assert roman_to_int("  I  ") == 1
        assert roman_to_int("II ") == 2
        assert roman_to_int(" III") == 3
    
    def test_invalid_roman_numeral(self) -> None:
        """Test that invalid Roman numerals raise ValueError."""
        with pytest.raises(ValueError, match="Invalid Roman numeral"):
            roman_to_int("VIII")
        
        with pytest.raises(ValueError, match="Invalid Roman numeral"):
            roman_to_int("IX")
        
        with pytest.raises(ValueError, match="Invalid Roman numeral"):
            roman_to_int("ABC")
    
    def test_empty_string(self) -> None:
        """Test that empty string raises ValueError."""
        with pytest.raises(ValueError, match="Invalid Roman numeral"):
            roman_to_int("")


class TestIntToRoman:
    """Test cases for int_to_roman function."""
    
    def test_all_valid_integers(self) -> None:
        """Test conversion of all valid integers 1-7."""
        test_cases = [
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (5, "V"),
            (6, "VI"),
            (7, "VII"),
        ]
        for value, expected in test_cases:
            assert int_to_roman(value) == expected
    
    def test_invalid_integer(self) -> None:
        """Test that integers outside 1-7 raise ValueError."""
        with pytest.raises(ValueError, match="Invalid tier value"):
            int_to_roman(0)
        
        with pytest.raises(ValueError, match="Invalid tier value"):
            int_to_roman(8)
        
        with pytest.raises(ValueError, match="Invalid tier value"):
            int_to_roman(-1)
