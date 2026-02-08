"""Integration tests for CLI commands."""

import pytest
from typer.testing import CliRunner
from unittest.mock import AsyncMock, MagicMock, patch

from src.cli import app


runner = CliRunner()


class TestListCommand:
    """Test cases for --list command."""
    
    def test_list_tomes_json(self) -> None:
        """Test listing tomes with JSON output."""
        with patch("src.cli.TomeService") as mock_service_class:
            mock_service = MagicMock()
            mock_service.list_tomes = AsyncMock(return_value=[
                MagicMock(
                    name="Nature's Wrath",
                    tier=3,
                    category="Nature",
                    link="https://example.com/nature",
                    to_dict=lambda: {
                        "name": "Nature's Wrath",
                        "tier": 3,
                        "category": "Nature",
                        "link": "https://example.com/nature",
                    },
                    tier_roman="III",
                )
            ])
            mock_service_class.return_value = mock_service
            
            result = runner.invoke(app, ["list", "--json"])
            
            assert result.exit_code == 0
            assert '"name": "Nature\'s Wrath"' in result.output
            assert '"tier": 3' in result.output
    
    def test_list_tomes_table(self) -> None:
        """Test listing tomes with table output."""
        with patch("src.cli.TomeService") as mock_service_class:
            mock_service = MagicMock()
            mock_service.list_tomes = AsyncMock(return_value=[
                MagicMock(
                    name="Nature's Wrath",
                    tier=3,
                    category="Nature",
                    tier_roman="III",
                )
            ])
            mock_service_class.return_value = mock_service
            
            result = runner.invoke(app, ["list"])
            
            assert result.exit_code == 0
            assert "Nature's Wrath" in result.output
            assert "III" in result.output


class TestShowCommand:
    """Test cases for --show command."""
    
    def test_show_tome_json(self) -> None:
        """Test showing tome details with JSON output."""
        with patch("src.cli.TomeService") as mock_service_class:
            mock_service = MagicMock()
            mock_detail = MagicMock()
            mock_detail.to_dict.return_value = {
                "name": "Nature's Wrath",
                "tier": 3,
                "category": "Nature",
                "summary": "A powerful tome.",
            }
            mock_service.get_tome_detail = AsyncMock(return_value=mock_detail)
            mock_service_class.return_value = mock_service
            
            result = runner.invoke(app, ["show", "Nature's Wrath", "--json"])
            
            assert result.exit_code == 0
            assert '"name": "Nature\'s Wrath"' in result.output
    
    def test_show_tome_not_found(self) -> None:
        """Test showing non-existent tome."""
        from src.exceptions import TomeNotFoundError
        
        with patch("src.cli.TomeService") as mock_service_class:
            mock_service = MagicMock()
            error = TomeNotFoundError("Tome 'NonExistent' not found.")
            mock_service.get_tome_detail = AsyncMock(side_effect=error)
            mock_service_class.return_value = mock_service
            
            result = runner.invoke(app, ["show", "NonExistent"])
            
            assert result.exit_code == 5
            assert "not found" in result.output


class TestRefreshCommand:
    """Test cases for --refresh command."""
    
    def test_refresh_all(self) -> None:
        """Test refreshing all cache."""
        with patch("src.cli.TomeService") as mock_service_class:
            mock_service = MagicMock()
            mock_service.list_tomes = AsyncMock(return_value=[
                MagicMock(name="Tome1"),
                MagicMock(name="Tome2"),
            ])
            mock_service_class.return_value = mock_service
            
            result = runner.invoke(app, ["refresh"])
            
            assert result.exit_code == 0
            assert "refreshed" in result.output.lower()
    
    def test_refresh_list_only(self) -> None:
        """Test refreshing only tome list."""
        with patch("src.cli.TomeService") as mock_service_class:
            mock_service = MagicMock()
            mock_service.list_tomes = AsyncMock(return_value=[
                MagicMock(name="Tome1"),
            ])
            mock_service_class.return_value = mock_service
            
            result = runner.invoke(app, ["refresh", "--list-only"])
            
            assert result.exit_code == 0
            assert "Tome list refreshed" in result.output


class TestVersionCommand:
    """Test cases for --version."""
    
    def test_version(self) -> None:
        """Test version command."""
        result = runner.invoke(app, ["--version"])
        
        assert result.exit_code == 0
        assert "aow4-tome version" in result.output
