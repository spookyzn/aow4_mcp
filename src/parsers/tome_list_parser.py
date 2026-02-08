"""Parser for AOW4 Wiki Tomes list page."""

from bs4 import BeautifulSoup, Tag

from src.config import VALID_CATEGORIES, WIKI_BASE_URL
from src.models.tome import Tome
from src.exceptions import ParseError
from src.utils.roman_numerals import roman_to_int


class TomeListParser:
    """Parse the Tomes list page from AOW4 Wiki.
    
    Extracts all Tomes grouped by their categories, filtering out
    any "Other Tomes" category entries.
    """
    
    def parse(self, html: str) -> list[Tome]:
        """Parse HTML content and return list of Tome objects.
        
        Args:
            html: HTML content from the Tomes Wiki page
            
        Returns:
            List of Tome objects
            
        Raises:
            ParseError: If HTML structure is unexpected
        """
        soup = BeautifulSoup(html, "html.parser")
        tomes: list[Tome] = []
        
        # Find all category sections
        # Wiki page structure: each category has a header followed by a table
        for category in VALID_CATEGORIES:
            category_tomes = self._parse_category(soup, category)
            tomes.extend(category_tomes)
        
        return tomes
    
    def _parse_category(self, soup: BeautifulSoup, category: str) -> list[Tome]:
        """Parse a single category section.
        
        Args:
            soup: BeautifulSoup object
            category: Category name to parse
            
        Returns:
            List of Tome objects for this category
        """
        tomes: list[Tome] = []
        
        # Find the category header (h2 or h3)
        # Try different possible header formats
        header = self._find_category_header(soup, category)
        if not header:
            return tomes
        
        # Find the table following this header
        table = header.find_next("table")
        if not table:
            return tomes
        
        # Parse rows from the table
        rows = table.find_all("tr")
        for row in rows:
            # Skip header rows
            if row.find("th"):
                continue
            
            cells = row.find_all("td")
            if len(cells) >= 2:
                tome = self._parse_tome_row(cells, category)
                if tome:
                    tomes.append(tome)
        
        return tomes
    
    def _find_category_header(self, soup: BeautifulSoup, category: str) -> Tag | None:
        """Find the header element for a category.

        Args:
            soup: BeautifulSoup object
            category: Category name

        Returns:
            Header element or None
        """
        for header in soup.find_all(["h3"]):
            header_text = header.get_text(strip=True)
            if category.lower() in header_text.lower():
                return header  # type: ignore
        return None
    
    def _parse_tome_row(self, cells: list[Tag], category: str) -> Tome | None:
        """Parse a single table row into a Tome.

        Args:
            cells: List of table cell elements
            category: Category name

        Returns:
            Tome object or None if parsing fails
        """
        try:
            # First cell typically contains name and tier
            name_cell = cells[0]

            # Extract link and name
            link_elem = name_cell.find("a")
            if not link_elem:
                return None

            name = link_elem.get_text(strip=True)
            href = link_elem.get("href", "")

            # Build full URL
            if href.startswith("/"):
                link = f"{WIKI_BASE_URL}{href}"
            else:
                link = f"{WIKI_BASE_URL}/{href}"

            # Try to extract tier from the name or additional cells
            tier = self._extract_tier(name, cells)

            return Tome(
                name=name,
                tier=tier,
                category=category,
                link=link,  # type: ignore
            )
        except Exception as e:
            raise ParseError(
                f"Failed to parse Tome row for category {category}",
                details=str(e)
            ) from e
    
    def _extract_tier(self, name: str, cells: list[Tag]) -> int:
        """Extract tier from name or cells.

        Args:
            name: Tome name
            cells: Table cells

        Returns:
            Tier as integer (default 1 if not found)
        """
        # Try to find Roman numeral in name (e.g., "Nature's Wrath III")
        import re
        match = re.search(r'\s+([IVX]+)$', name)
        if match:
            try:
                return roman_to_int(match.group(1))
            except ValueError:
                pass

        # Check additional cells for tier info
        for cell in cells[1:]:
            text = cell.get_text(strip=True)
            match = re.search(r'^([IVX]+)$', text)
            if match:
                try:
                    return roman_to_int(match.group(1))
                except ValueError:
                    pass

        # Default to tier 1 if not found
        return 1
