"""CLI entry point for AOW4 Tome Scraper."""

import asyncio
import json
import sys
from typing import Any

import typer
from rich.console import Console
from rich.table import Table

from src.services.tome_service import TomeService
from src.exceptions import AOW4ScraperError, TomeNotFoundError

app = typer.Typer(
    name="aow4-tome",
    help="CLI tool to fetch and cache Age of Wonders 4 Tome information",
    add_completion=False,
)
console = Console()


# Global options
def global_options(
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
    no_cache: bool = typer.Option(False, "--no-cache", help="Skip cache, fetch from Wiki"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
) -> dict[str, Any]:
    """Global CLI options."""
    return {
        "json_output": json_output,
        "no_cache": no_cache,
        "verbose": verbose,
    }


@app.command()
def list_tomes(
    ctx: typer.Context,
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
    no_cache: bool = typer.Option(False, "--no-cache", help="Skip cache"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
) -> None:
    """List all available Tomes grouped by category."""
    asyncio.run(_list_tomes_async(json_output, no_cache, verbose))


async def _list_tomes_async(
    json_output: bool,
    no_cache: bool,
    verbose: bool,
) -> None:
    """Async implementation of list command."""
    try:
        service = TomeService()
        tomes = await service.list_tomes(use_cache=not no_cache)
        
        if verbose:
            console.print(f"[dim]Fetched {len(tomes)} tomes[/dim]")
        
        if json_output:
            # Output as JSON
            output = [t.to_dict() for t in tomes]
            console.print(json.dumps(output, indent=2))
        else:
            # Output as table
            _display_tomes_table(tomes)
    
    except AOW4ScraperError as e:
        console.print(f"[red]Error: {e.message}[/red]")
        if e.details and verbose:
            console.print(f"[dim]Details: {e.details}[/dim]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        sys.exit(1)


def _display_tomes_table(tomes: list) -> None:
    """Display tomes in a rich table."""
    # Group by category
    from collections import defaultdict
    by_category = defaultdict(list)
    for tome in tomes:
        by_category[tome.category].append(tome)
    
    # Create table
    table = Table(title="AOW4 Tomes")
    table.add_column("Category", style="cyan", no_wrap=True)
    table.add_column("Name", style="green")
    table.add_column("Tier", style="yellow", justify="center")
    
    for category in sorted(by_category.keys()):
        category_tomes = sorted(by_category[category], key=lambda t: t.tier)
        for i, tome in enumerate(category_tomes):
            cat_display = category if i == 0 else ""
            table.add_row(
                cat_display,
                tome.name,
                tome.tier_roman,
            )
    
    console.print(table)


@app.command()
def show(
    name: str = typer.Argument(..., help="Tome name to display"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
    no_cache: bool = typer.Option(False, "--no-cache", help="Skip cache"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
) -> None:
    """Show detailed information for a specific Tome."""
    asyncio.run(_show_async(name, json_output, no_cache, verbose))


async def _show_async(
    name: str,
    json_output: bool,
    no_cache: bool,
    verbose: bool,
) -> None:
    """Async implementation of show command."""
    try:
        service = TomeService()
        detail = await service.get_tome_detail(name, use_cache=not no_cache)
        
        if verbose:
            console.print(f"[dim]Fetched details for: {detail.name}[/dim]")
        
        if json_output:
            console.print(json.dumps(detail.to_dict(), indent=2))
        else:
            _display_tome_detail(detail)
    
    except TomeNotFoundError as e:
        console.print(f"[red]Error: {e.message}[/red]")
        if e.details and verbose:
            console.print(f"[dim]Details: {e.details}[/dim]")
        sys.exit(5)
    except AOW4ScraperError as e:
        console.print(f"[red]Error: {e.message}[/red]")
        if e.details and verbose:
            console.print(f"[dim]Details: {e.details}[/dim]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        sys.exit(1)


def _display_tome_detail(detail: Any) -> None:
    """Display tome details in formatted output."""
    # Title
    console.print(f"\n[bold cyan]{detail.name}[/bold cyan]")
    console.print("=" * len(detail.name))
    
    # Basic info
    console.print(f"[yellow]Category:[/yellow] {detail.category}")
    console.print(f"[yellow]Tier:[/yellow] {detail.tier}")
    
    # Summary
    console.print(f"\n[yellow]Summary:[/yellow]")
    console.print(detail.summary)
    
    # Skills
    if detail.tome_skills:
        console.print(f"\n[yellow]Skills:[/yellow]")
        skills_table = Table()
        skills_table.add_column("Skill", style="green")
        skills_table.add_column("Tier", style="yellow", justify="center")
        skills_table.add_column("Type", style="blue")
        
        for skill in detail.tome_skills:
            from src.utils.roman_numerals import int_to_roman
            skills_table.add_row(
                skill.name,
                str(skill.tier),
                skill.type,
            )
        
        console.print(skills_table)
    
    # Info
    if detail.tome_info:
        console.print(f"\n[yellow]Info:[/yellow]")
        for value in detail.tome_info:
            console.print(f"{value}")
    
    console.print()


@app.command()
def refresh(
    list_only: bool = typer.Option(False, "--list-only", help="Only refresh tome list"),
    detail: str = typer.Option(None, "--detail", help="Refresh specific tome detail"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
) -> None:
    """Refresh cached Tome data."""
    asyncio.run(_refresh_async(list_only, detail, verbose))


async def _refresh_async(
    list_only: bool,
    detail_name: str | None,
    verbose: bool,
) -> None:
    """Async implementation of refresh command."""
    try:
        service = TomeService()
        
        console.print("[dim]Refreshing cache...[/dim]")
        
        if detail_name:
            # Refresh specific tome
            detail = await service.get_tome_detail(detail_name, use_cache=False)
            console.print(f"[green]✓ Refreshed:[/green] {detail.name}")
        elif list_only:
            # Refresh only list
            tomes = await service.list_tomes(use_cache=False)
            console.print(f"[green]✓ Tome list refreshed ({len(tomes)} tomes)[/green]")
        else:
            # Refresh all
            service.refresh_cache()
            tomes = await service.list_tomes(use_cache=False)
            console.print(f"[green]✓ Tome list refreshed ({len(tomes)} tomes)[/green]")
            console.print("[green]✓ All cache refreshed[/green]")
    
    except AOW4ScraperError as e:
        console.print(f"[red]Error: {e.message}[/red]")
        if e.details and verbose:
            console.print(f"[dim]Details: {e.details}[/dim]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        sys.exit(1)


@app.callback()
def main(
    version: bool = typer.Option(False, "--version", help="Show version"),
) -> None:
    """AOW4 Tome Scraper - CLI tool for Age of Wonders 4 Tome information."""
    if version:
        from src import __version__
        console.print(f"aow4-tome version {__version__}")
        raise typer.Exit()


if __name__ == "__main__":
    app()
