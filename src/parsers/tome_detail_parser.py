"""Parser for AOW4 Wiki Tome detail pages."""

from bs4 import BeautifulSoup, Tag

from src.models.tome_detail import TomeDetail
from src.models.tome_skill import TomeSkill
from src.exceptions import ParseError
from src.utils.roman_numerals import roman_to_int


class TomeDetailParser:
    """Parse individual Tome detail pages from AOW4 Wiki.
    
    Extracts summary, skills, and sidebar information.
    """
    
    def parse(self, html: str, tome_name: str, category: str, tier: int) -> TomeDetail:
        """Parse HTML content and return TomeDetail object.
        
        Args:
            html: HTML content from the Tome detail page
            tome_name: Name of the Tome
            category: Tome category
            tier: Tome tier
            
        Returns:
            TomeDetail object
            
        Raises:
            ParseError: If HTML structure is unexpected
        """
        soup = BeautifulSoup(html, "html.parser")
        
        # Extract summary
        summary = self._extract_summary(soup)
        
        # Extract tome skills
        tome_skills = self._extract_tome_skills(soup)
        
        # Extract sidebar info
        tome_info = self._extract_sidebar_info(soup)
        
        return TomeDetail(
            name=tome_name,
            tier=tier,
            category=category,
            summary=summary,
            tome_skills=tome_skills,
            tome_info=tome_info,
        )
    
    def _extract_summary(self, soup: BeautifulSoup) -> str:
        """Extract the summary/description section.
        
        Args:
            soup: BeautifulSoup object
            
        Returns:
            Summary text
        """
        # Try to find the first paragraph after the title
        # The summary is typically the first substantial paragraph
        content_div = soup.find("div", {"id": "mw-content-text"})
        if not content_div:
            return ""
        
        # The first p startwith test Tier 
        for p in content_div.find_all("p"):
            text = p.get_text(strip=True)
            if text and text.startswith('Tier'):  # Skip very short paragraphs
                return text
        
        return ""
    
    def _extract_tome_skills(self, soup: BeautifulSoup) -> list[TomeSkill]:
        """Extract Tome skills from the page.
        
        Args:
            soup: BeautifulSoup object
            
        Returns:
            List of TomeSkill objects
        """
        skills: list[TomeSkill] = []
        
        # Find skills section - look for "Tome Skills" header
        skills_header = None
        for header in soup.find_all(["h2", "h3", "h4"]):
            header_lower = header.get_text(strip=True).lower() 
            if "tome skill" in header_lower or "tome spells" in header_lower:
                skills_header = header
                break
        
        if not skills_header:
            return skills
        
        # Find the table following this header
        table = skills_header.find_next("table")
        if not table:
            return skills
        
        # Parse skill rows
        rows = table.find_all("tr")
        for row in rows:
            # Skip header rows
            if row.find("th"):
                continue
            
            cells = row.find_all("td")
            if len(cells) >= 3:
                skill = self._parse_skill_row(cells)
                if skill:
                    skills.append(skill)
        
        return skills
    
    def _parse_skill_row(self, cells: list[Tag]) -> TomeSkill | None:
        """Parse a single skill table row.
        
        Args:
            cells: List of table cell elements
            
        Returns:
            TomeSkill object or None
        """
        try:
            # Typical structure: Name | Tier | Type | Effects | Units (optional)
            name = cells[1].get_text(strip=True)
            
            # Extract tier
            tier_text = cells[2].get_text(strip=True) if len(cells) > 1 else "1" 
            try:
                tier = int(tier_text) 
            except ValueError:
                tier = 1
            
            # Extract type(s)
            type_text = cells[3].get_text(strip=True) if len(cells) > 2 else ""
            skill_types = type_text.strip()
            if not skill_types:
                skill_types = "Unknown"
            
            # Extract effects
            effects_text = cells[4].get_text(separator=" ", strip=True) if len(cells) > 3 else ""
            #.replace("\n", " ").replace("\u00a0", "") if len(cells) > 3 else ""
            if not effects_text:
                effects_text = "Unknown"
            
            return TomeSkill(
                name=name,
                tier=tier,
                type=skill_types,
                effects=effects_text,
            )
        except Exception as e:
            raise ParseError(
                f"Failed to parse skill row",
                details=str(e)
            ) from e
    
    def _extract_sidebar_info(self, soup: BeautifulSoup) -> list[str]:
        """Extract information from the sidebar/info box.
        
        Args:
            soup: BeautifulSoup object
            
        Returns:
            Dictionary of sidebar information
        """
        info = [] 
        
        # Find infobox/sidebar
        infobox = soup.find("aside") or soup.find("table", {"class": "wikitable"})
        if not infobox:
            return info
        
        # Extract key-value pairs
        rows = infobox.find_all("tr")
        # Get all list items
        lis = rows[2].find_all("li")
        for li in lis:
            info.append(li.get_text(strip=True, separator=" "))
        return info
