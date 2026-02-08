"""Tests for TomeListParser."""

import pytest

from src.parsers.tome_list_parser import TomeListParser
from src.exceptions import ParseError
from src.config import VALID_CATEGORIES


class TestTomeListParser:
    """Test cases for TomeListParser."""
    
    @pytest.fixture
    def parser(self) -> TomeListParser:
        """Create a parser instance."""
        return TomeListParser()
    
    def test_parse_empty_html(self, parser: TomeListParser) -> None:
        """Test parsing empty HTML returns empty list."""
        result = parser.parse("<html></html>")
        assert result == []
    
    def test_parse_sample_html(self, parser: TomeListParser) -> None:
        """Test parsing sample HTML with Nature tomes."""
        html = """
        <html>
        <body>
            <h2>Nature</h2>
            <table>
                <tr><th>Name</th><th>Tier</th></tr>
                <tr>
                    <td><a href="/Nature's_Embrace">Nature's Embrace I</a></td>
                    <td>I</td>
                </tr>
                <tr>
                    <td><a href="/Nature's_Wrath">Nature's Wrath III</a></td>
                    <td>III</td>
                </tr>
            </table>
            <h2>Chaos</h2>
            <table>
                <tr><th>Name</th><th>Tier</th></tr>
                <tr>
                    <td><a href="/Chaos_Flame">Chaos Flame II</a></td>
                    <td>II</td>
                </tr>
            </table>
        </body>
        </html>
        """
        result = parser.parse(html)
        
        assert len(result) == 3
        
        # Check Nature tomes
        nature_tomes = [t for t in result if t.category == "Nature"]
        assert len(nature_tomes) == 2
        assert nature_tomes[0].name == "Nature's Embrace I"
        assert nature_tomes[0].tier == 1
        assert nature_tomes[1].name == "Nature's Wrath III"
        assert nature_tomes[1].tier == 3
        
        # Check Chaos tome
        chaos_tomes = [t for t in result if t.category == "Chaos"]
        assert len(chaos_tomes) == 1
        assert chaos_tomes[0].tier == 2
    
    def test_extract_tier_from_name(self, parser: TomeListParser) -> None:
        """Test tier extraction from name."""
        html = """
        <html>
        <body>
            <h2>Nature</h2>
            <table>
                <tr><td><a href="/Test">Test Tome V</a></td><td></td></tr>
            </table>
        </body>
        </html>
        """
        result = parser.parse(html)
        assert len(result) == 1
        assert result[0].tier == 5
    
    def test_extract_tier_from_cell(self, parser: TomeListParser) -> None:
        """Test tier extraction from table cell."""
        html = """
        <html>
        <body>
            <h2>Nature</h2>
            <table>
                <tr><td><a href="/Test">Test Tome</a></td><td>VII</td></tr>
            </table>
        </body>
        </html>
        """
        result = parser.parse(html)
        assert len(result) == 1
        assert result[0].tier == 7
    
    def test_invalid_category_excluded(self, parser: TomeListParser) -> None:
        """Test that "Other Tomes" category is excluded."""
        html = """
        <html>
        <body>
            <h2>Nature</h2>
            <table>
                <tr><td><a href="/Nature">Nature Tome</a></td><td>I</td></tr>
            </table>
            <h2>Other Tomes</h2>
            <table>
                <tr><td><a href="/Other">Other Tome</a></td><td>I</td></tr>
            </table>
        </body>
        </html>
        """
        result = parser.parse(html)
        
        # Should only have Nature tome, not Other Tome
        assert len(result) == 1
        assert result[0].category == "Nature"
        assert result[0].name == "Nature Tome"
    
    def test_only_seven_categories_returned(self, parser: TomeListParser) -> None:
        """Test that only the 7 valid categories are returned."""
        html = """
        <html>
        <body>
            <h2>Nature</h2><table><tr><td><a href="/N">N</a></td><td>I</td></tr></table>
            <h2>Chaos</h2><table><tr><td><a href="/C">C</a></td><td>I</td></tr></table>
            <h2>Order</h2><table><tr><td><a href="/O">O</a></td><td>I</td></tr></table>
            <h2>Shadow</h2><table><tr><td><a href="/S">S</a></td><td>I</td></tr></table>
            <h2>Creation</h2><table><tr><td><a href="/Cr">Cr</a></td><td>I</td></tr></table>
            <h2>Destruction</h2><table><tr><td><a href="/D">D</a></td><td>I</td></tr></table>
            <h2>Materium</h2><table><tr><td><a href="/M">M</a></td><td>I</td></tr></table>
            <h2>Other Tomes</h2><table><tr><td><a href="/OT">OT</a></td><td>I</td></tr></table>
            <h2>Special</h2><table><tr><td><a href="/Sp">Sp</a></td><td>I</td></tr></table>
        </body>
        </html>
        """
        result = parser.parse(html)
        
        # Should have exactly 7 tomes (one from each valid category)
        assert len(result) == 7
        
        # Check that only valid categories are present
        categories = set(t.category for t in result)
        assert categories == set(VALID_CATEGORIES)
        
        # Verify no "Other Tomes" or "Special" in results
        for tome in result:
            assert tome.category in VALID_CATEGORIES
            assert tome.category != "Other Tomes"
            assert tome.category != "Special"
    
    def test_link_url_construction(self, parser: TomeListParser) -> None:
        """Test that links are properly constructed."""
        html = """
        <html>
        <body>
            <h2>Nature</h2>
            <table>
                <tr><td><a href="/Nature's_Wrath">Nature's Wrath</a></td><td>I</td></tr>
            </table>
        </body>
        </html>
        """
        result = parser.parse(html)
        assert len(result) == 1
        link_str = str(result[0].link)
        assert "aow4.paradoxwikis.com/Nature's_Wrath" in link_str
    
    def test_no_link_in_row(self, parser: TomeListParser) -> None:
        """Test handling of rows without links."""
        html = """
        <html>
        <body>
            <h2>Nature</h2>
            <table>
                <tr><td>No Link Here</td><td>I</td></tr>
            </table>
        </body>
        </html>
        """
        result = parser.parse(html)
        # Should skip rows without links
        assert len(result) == 0
