# Quick Start Guide

**Feature**: AOW4 Tome Scraper  
**Date**: 2025-02-07

---

## Installation

### Prerequisites

- Python 3.13+
- Redis server (local or remote)
- Playwright browsers installed

### Install Dependencies

```bash
# Install Python dependencies
uv pip install -e .

# Or using pip
pip install -e .

# Install Playwright browsers
playwright install chromium
```

### Configure Redis

```bash
# Using default local Redis (no config needed)
redis-server

# Or set custom Redis URL
export AOW4_REDIS_URL="redis://localhost:6379/0"
```

---

## First Run

### 1. List All Tomes

```bash
# Fetch and display all tomes (uses cache after first run)
aow4-tome --list

# Example output:
# ┌────────────────────────┬──────┬────────────┐
# │ Name                   │ Tier │ Category   │
# ├────────────────────────┼──────┼────────────┤
# │ Nature's Embrace       │ I    │ Nature     │
# │ Nature's Wrath         │ III  │ Nature     │
# │ ...                    │ ...  │ ...        │
# └────────────────────────┴──────┴────────────┘
```

### 2. View Tome Details

```bash
# Show detailed info for a specific tome
aow4-tome --show "Nature's Wrath"

# Example output:
# Nature's Wrath
# ==============
# Category: Nature
# Tier: III
#
# Summary:
# This tome focuses on aggressive nature magic and summoning...
#
# Skills:
# ┌───────────────────┬──────┬──────────────┐
# │ Skill             │ Tier │ Type         │
# ├───────────────────┼──────┼──────────────┤
# │ Entangling Vines  │ I    │ Battle Magic │
# └───────────────────┴──────┴──────────────┘
```

### 3. Refresh Cache

```bash
# Force refresh all cached data
aow4-tome --refresh

# Refresh only the tome list
aow4-tome --refresh-list

# Refresh only a specific tome
aow4-tome --refresh-detail "Nature's Wrath"
```

---

## Common Usage Patterns

### Scripting with JSON Output

```bash
# Export all tomes to JSON
aow4-tome --list --json > all_tomes.json

# Find tomes by category
aow4-tome --list --json | jq '.[] | select(.category == "Nature")'

# Get specific field
aow4-tome --show "Nature's Wrath" --json | jq '.summary'
```

### Filter by Tier

```bash
# Get all Tier V tomes
aow4-tome --list --json | jq '.[] | select(.tier == 5)'
```

### Batch Operations

```bash
# Refresh all Nature tomes
for tome in $(aow4-tome --list --json | jq -r '.[] | select(.category == "Nature") | .name'); do
    aow4-tome --refresh-detail "$tome"
done
```

---

## Troubleshooting

### Redis Connection Error

```
Error: Cannot connect to Redis at localhost:6379
```

**Solution**:
```bash
# Start Redis server
redis-server

# Or configure remote Redis
export AOW4_REDIS_URL="redis://remote-host:6379/0"
```

### Wiki Parse Error

```
Error: Failed to parse Wiki HTML structure
```

**Solution**:
```bash
# Try refreshing cache
aow4-tome --refresh --verbose

# Check if Wiki is accessible
curl https://aow4.paradoxwikis.com/Tomes
```

### Playwright Not Installed

```
Error: Browser not found
```

**Solution**:
```bash
playwright install chromium
```

---

## Configuration

### Environment Variables

Create `.env` file or export variables:

```bash
# Redis connection
export AOW4_REDIS_URL="redis://localhost:6379/0"

# Request timeout (seconds)
export AOW4_TIMEOUT="30"

# Verbose logging
export AOW4_VERBOSE="true"
```

### Cache Behavior

- **First run**: Fetches from Wiki, stores in Redis
- **Subsequent runs**: Reads from Redis (instant)
- **Refresh**: Use `--refresh` to update cached data
- **No expiration**: Cache persists until manually refreshed

---

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test
pytest tests/unit/test_models.py -v
```

### Type Checking

```bash
mypy src/
```

---

## Getting Help

```bash
# Show help
aow4-tome --help

# Show version
aow4-tome --version

# Verbose mode for debugging
aow4-tome --list --verbose
```
