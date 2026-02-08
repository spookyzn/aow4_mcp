# AOW4 Tome Scraper

CLI tool to fetch and cache Age of Wonders 4 Tome information from the official Wiki.

## Features

- **List all Tomes**: Display all 60+ Tomes grouped by their 7 categories (Nature, Chaos, Order, Shadow, Creation, Destruction, Materium)
- **Show Tome Details**: View detailed information including Summary, Skills, and Attributes
- **Redis Caching**: Fast subsequent lookups with manual refresh control
- **JSON Output**: Script-friendly output format
- **Rich Tables**: Beautiful terminal output with colors

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd aow4-mcp

# Install dependencies
uv pip install -e .

# Install Playwright browsers
playwright install chromium

# Start Redis (required for caching)
redis-server
```

## Usage

### List All Tomes

```bash
# Display as table
aow4-tome list

# Output as JSON
aow4-tome list --json
```

### Show Tome Details

```bash
# Display formatted details
aow4-tome show "Nature's Wrath"

# Output as JSON
aow4-tome show "Nature's Wrath" --json
```

### Options

- `--json`: Output as JSON instead of formatted tables
- `--no-cache`: Skip cache and fetch from Wiki
- `--verbose, -v`: Show verbose output
- `--version`: Show version

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `AOW4_REDIS_URL` | `redis://localhost:6379/0` | Redis connection URL |
| `AOW4_TIMEOUT` | `30` | Request timeout in seconds |
| `AOW4_HEADLESS` | `true` | Run Playwright in headless mode |

## Configure MCP servers

```json
{
  "mcpServers": {
    "AOW4_Tomes": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/aow4_mcp",
        "run",
        "aow4_mcp.py"
      ],
      "disabled": false,
      "timeout": 60
    }
  }
}
```

## Development

```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src

# Type checking
uv run mypy src/
```

## Architecture

- **src/models/**: Pydantic data models (Tome, TomeDetail, TomeSkill)
- **src/services/**: Core services (WikiClient, CacheManager, TomeService)
- **src/parsers/**: HTML parsing logic
- **src/cli.py**: Typer CLI interface

## License

MIT
