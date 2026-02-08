"""Roman numeral to integer conversion utilities."""

from typing import Final

# Mapping of Roman numerals to integers for Tome tiers
ROMAN_TO_INT: Final[dict[str, int]] = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
}

# Reverse mapping for display purposes
INT_TO_ROMAN: Final[dict[int, str]] = {v: k for k, v in ROMAN_TO_INT.items()}


def roman_to_int(roman: str) -> int:
    """Convert a Roman numeral string to an integer.
    
    Args:
        roman: Roman numeral string (I, II, III, IV, V, VI, VII)
        
    Returns:
        Integer value (1-7)
        
    Raises:
        ValueError: If the Roman numeral is not valid
    """
    roman_upper = roman.upper().strip()
    if roman_upper not in ROMAN_TO_INT:
        raise ValueError(f"Invalid Roman numeral: {roman}. Expected I-VII.")
    return ROMAN_TO_INT[roman_upper]


def int_to_roman(value: int) -> str:
    """Convert an integer to a Roman numeral string.
    
    Args:
        value: Integer value (1-7)
        
    Returns:
        Roman numeral string
        
    Raises:
        ValueError: If the integer is not in range 1-7
    """
    if value not in INT_TO_ROMAN:
        raise ValueError(f"Invalid tier value: {value}. Expected 1-7.")
    return INT_TO_ROMAN[value]
