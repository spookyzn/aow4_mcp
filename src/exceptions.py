"""Custom exceptions for AOW4 Tome Scraper."""


class AOW4ScraperError(Exception):
    """Base exception for all scraper errors."""
    
    def __init__(self, message: str, details: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details


class WikiError(AOW4ScraperError):
    """Raised when there's an error connecting to or fetching from the Wiki."""
    pass


class ParseError(AOW4ScraperError):
    """Raised when there's an error parsing Wiki HTML content."""
    pass


class CacheError(AOW4ScraperError):
    """Raised when there's an error with Redis cache operations."""
    pass


class TomeNotFoundError(AOW4ScraperError):
    """Raised when a requested Tome is not found."""
    pass
