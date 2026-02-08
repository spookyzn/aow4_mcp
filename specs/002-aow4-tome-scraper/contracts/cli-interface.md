# CLI Interface Contract

**Feature**: AOW4 Tome Scraper  
**Date**: 2025-02-07

---

## Command Overview

```bash
aow4-tome [OPTIONS]
```

**Entry Point**: `src/cli.py`

---

## Commands & Options

### 1. List All Tomes

List all available tomes grouped by category.

```bash
aow4-tome --list
```

**Output Format**: Rich table (interactive) or JSON (piped)

**Table Columns**:
| Column | Description |
|--------|-------------|
| Name | Tome name |
| Tier | Roman numeral tier (I-VII) |
| Category | One of 7 categories |

**JSON Output**:
```json
[
  {
    "name": "Nature's Wrath",
    "tier": 3,
    "category": "Nature",
    "link": "https://aow4.paradoxwikis.com/Nature's_Wrath"
  }
]
```

**Exit Codes**:
- `0`: Success
- `1`: Network error
- `2`: Parsing error

---

### 2. Show Tome Details

Display detailed information about a specific tome.

```bash
aow4-tome --show <TOME_NAME>
```

**Arguments**:
| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `TOME_NAME` | string | ✓ | Exact tome name (case-insensitive) |

**Output Format**: Rich formatted output or JSON

**Example**:
```bash
aow4-tome --show "Nature's Wrath"
```

**Output Structure**:
```
Nature's Wrath
==============
Category: Nature
Tier: III

Summary:
This tome focuses on aggressive nature magic...

Skills:
┌───────────────────┬──────┬──────────────┐
│ Skill             │ Tier │ Type         │
├───────────────────┼──────┼──────────────┤
│ Entangling Vines  │ I    │ Battle Magic │
│ Summon Treant     │ III  │ Summoning    │
└───────────────────┴──────┴──────────────┘

Info:
  Tier: III
  Type: Nature
  Unlocks: Requires Nature I
```

**Error Cases**:
- Tome not found: "Error: Tome 'XYZ' not found. Use --list to see available tomes."

---

### 3. Refresh Cache

Force refresh the cache by fetching latest data from Wiki.

```bash
aow4-tome --refresh
```

**Options** (mutually exclusive):
| Option | Description |
|--------|-------------|
| `--refresh-list` | Only refresh tome list |
| `--refresh-detail <NAME>` | Only refresh specific tome detail |

**Default**: Refreshes both list and all cached details

**Output**:
```
Refreshing cache...
✓ Tome list refreshed (63 tomes)
✓ Tome details refreshed (12 cached)
```

---

### 4. Global Options

| Option | Description |
|--------|-------------|
| `--json` | Output raw JSON instead of formatted tables |
| `--no-cache` | Skip cache, always fetch from Wiki |
| `--cache-dir <PATH>` | Custom Redis connection (default: localhost:6379) |
| `-v, --verbose` | Verbose output with debug info |
| `--version` | Show version number |
| `-h, --help` | Show help message |

---

## Usage Examples

### Basic Usage

```bash
# List all tomes
aow4-tome --list

# Show specific tome
aow4-tome --show "Nature's Wrath"

# Refresh all cache
aow4-tome --refresh
```

### Scripting Usage

```bash
# Get JSON output for scripting
aow4-tome --list --json > tomes.json

# Check if specific tome exists
aow4-tome --show "Nature's Wrath" --json | jq '.name'

# Refresh and check
aow4-tome --refresh && aow4-tome --list
```

### Debug Usage

```bash
# Verbose mode for troubleshooting
aow4-tome --list --verbose

# Skip cache for testing
aow4-tome --show "Nature's Wrath" --no-cache
```

---

## Error Handling

### Error Format (JSON mode)

```json
{
  "error": true,
  "code": "NETWORK_ERROR",
  "message": "Failed to connect to AOW4 Wiki",
  "details": "Connection timeout after 30s"
}
```

### Error Codes

| Code | Description | HTTP Equivalent |
|------|-------------|-----------------|
| `NETWORK_ERROR` | Cannot connect to Wiki | 503 |
| `PARSE_ERROR` | Failed to parse Wiki HTML | 500 |
| `NOT_FOUND` | Tome not found | 404 |
| `CACHE_ERROR` | Redis connection failed | 500 |
| `VALIDATION_ERROR` | Invalid input | 400 |

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `AOW4_REDIS_URL` | `redis://localhost:6379/0` | Redis connection URL |
| `AOW4_TIMEOUT` | `30` | Request timeout in seconds |
| `AOW4_HEADLESS` | `true` | Run Playwright in headless mode |

---

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | General error |
| `2` | Network/Wiki error |
| `3` | Cache/Redis error |
| `4` | Invalid input |
| `5` | Tome not found |
