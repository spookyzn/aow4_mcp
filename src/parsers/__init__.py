"""HTML parsers for Wiki page scraping."""

from .tome_list_parser import TomeListParser
from .tome_detail_parser import TomeDetailParser

__all__ = ["TomeListParser", "TomeDetailParser"]
