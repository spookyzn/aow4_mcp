# Implementation Tasks: AOW4 Tome Scraper

**Branch**: `002-aow4-tome-scraper` | **Date**: 2025-02-07  
**Spec**: [spec.md](./spec.md) | **Plan**: [plan.md](./plan.md) | **Data Model**: [data-model.md](./data-model.md)

---

## Summary

CLI tool to scrape AOW4 Tome information from Wiki using Playwright with Redis caching. Two P1 user stories: (1) List all Tomes (7 categories), (2) Show Tome details.

**Total Tasks**: 28  
**Estimated Duration**: 2-3 days  
**Parallel Opportunities**: Models, Services, Tests can be developed in parallel within each story

---

## Dependencies & Execution Order

```
Phase 1: Setup
    │
    ▼
Phase 2: Foundational (Redis, Playwright, Utilities)
    │
    ├──────────────────┬──────────────────┐
    ▼                  ▼                  ▼
Phase 3: US1       Phase 4: US2       Phase 5: CLI
(Tome List)        (Tome Detail)      (Integration)
    │                  │                  │
    └──────────────────┴──────────────────┘
                       │
                       ▼
                Phase 6: Polish
```

**User Story Dependencies**: US1 and US2 are **independent** - can be implemented in parallel after Phase 2.

---

## Phase 1: Project Setup

**Goal**: Initialize project structure and dependencies  
**Blocking**: All subsequent phases

- [x] T001 Create project directory structure: `src/models/`, `src/services/`, `tests/unit/`, `tests/integration/`
- [x] T002 Add dependencies to `pyproject.toml`: pydantic, playwright, redis, typer, rich, pytest, pytest-asyncio, fakeredis
- [x] T003 Create `src/__init__.py` and `src/models/__init__.py` package files
- [x] T004 Create `src/config.py` with Redis connection settings and environment variables
- [x] T005 Install Playwright browsers: `playwright install chromium`
- [x] T006 Verify project setup: run `python -c "import src"` successfully

---

## Phase 2: Foundational Infrastructure

**Goal**: Build shared utilities and services used by all user stories  
**Blocking**: Phase 3, Phase 4

- [x] T007 [P] Create `src/utils/roman_numerals.py` with `roman_to_int()` function (I→1, V→5, etc.)
- [x] T008 Create `tests/unit/test_roman_numerals.py` with test cases for all Roman numerals I-VII
- [x] T009 [P] Create `src/services/cache_manager.py` with `CacheManager` class for Redis operations
- [x] T010 Create `tests/unit/test_cache_manager.py` using fakeredis for mocking
- [x] T011 [P] Create `src/services/wiki_client.py` with `WikiClient` class using Playwright
- [x] T012 Create `tests/unit/test_wiki_client.py` with mocked Playwright responses
- [x] T013 Create `src/exceptions.py` with custom exception classes: `WikiError`, `ParseError`, `CacheError`

---

## Phase 3: User Story 1 - List All Tomes

**Goal**: Implement `--list` command to fetch and display all Tomes (7 categories only)  
**Independent Test**: Can test by running `--list` and verifying 7 categories returned, no "Other Tomes"
**Priority**: P1

### Models
- [x] T014 [P] [US1] Create `src/models/tome.py` with `Tome` Pydantic model (name, tier, category, link)
- [x] T015 [US1] Create `tests/unit/test_tome_model.py` validating Tome model constraints

### Parser
- [x] T016 [P] [US1] Create `src/parsers/tome_list_parser.py` with `TomeListParser` class
- [x] T017 [US1] Implement parsing logic: extract tomes from https://aow4.paradoxwikis.com/Tomes
- [x] T018 [US1] Add filter: exclude "Other Tomes" category, keep only 7 main categories
- [x] T019 [US1] Add Roman numeral conversion for tier field during parsing
- [x] T020 [US1] Create `tests/unit/test_tome_list_parser.py` with mocked HTML samples

### Service
- [x] T021 [P] [US1] Create `src/services/tome_service.py` with `TomeService.list_tomes()` method
- [x] T022 [US1] Implement caching: cache key `aow4:tome:list`, TTL never expires
- [x] T023 [US1] Create `tests/integration/test_tome_list_integration.py`

### Acceptance Test
- [x] T024 [US1] Create test: verify only 7 categories returned, "Other Tomes" excluded

---

## Phase 4: User Story 2 - Show Tome Details

**Goal**: Implement `--show <Tome>` command to fetch and display Tome details  
**Independent Test**: Can test by running `--show "Nature's Wrath"` and verifying Summary, Skills, Info returned
**Priority**: P1

### Models
- [x] T025 [P] [US2] Create `src/models/tome_skill.py` with `TomeSkill` Pydantic model
- [x] T026 [P] [US2] Create `src/models/tome_detail.py` with `TomeDetail` Pydantic model
- [x] T027 [US2] Create `tests/unit/test_tome_detail_model.py` validating model constraints

### Parser
- [x] T028 [P] [US2] Create `src/parsers/tome_detail_parser.py` with `TomeDetailParser` class
- [x] T029 [US2] Implement parsing: extract Summary section from page
- [x] T030 [US2] Implement parsing: extract Tome Skills table
- [x] T031 [US2] Implement parsing: extract sidebar info (tier, type, unlocks, etc.)
- [x] T032 [US2] Create `tests/unit/test_tome_detail_parser.py` with mocked HTML samples

### Service
- [x] T033 [P] [US2] Add `TomeService.get_tome_detail(name)` method
- [x] T034 [US2] Implement caching: cache key `aow4:tome:detail:{name}`, TTL never expires
- [x] T035 [US2] Create `tests/integration/test_tome_detail_integration.py`

---

## Phase 5: CLI Integration

**Goal**: Integrate services into CLI interface with Typer  
**Depends On**: Phase 3, Phase 4

- [x] T036 [P] Create `src/cli.py` with Typer app and main entry point
- [x] T037 Implement `--list` command: fetch from cache or Wiki, display as Rich table or JSON
- [x] T038 Implement `--show <TOME>` command: fetch detail, display formatted output
- [x] T039 Implement `--refresh` command: clear cache and re-fetch
- [x] T040 Add `--json` global flag for JSON output mode
- [x] T041 Add `--no-cache` global flag to bypass cache
- [x] T042 Add error handling with friendly messages for network/parse errors
- [x] T043 Create `tests/integration/test_cli.py` testing all commands

---

## Phase 6: Polish & Cross-Cutting

**Goal**: Documentation, type checking, and final validation  
**Depends On**: All previous phases

- [x] T044 [P] Run `mypy src/` and fix all type errors
- [x] T045 [P] Run `pytest` and ensure all tests pass
- [x] T046 Add docstrings to all public modules, classes, and functions
- [x] T047 Update `README.md` with installation and usage instructions
- [x] T048 Create `docs/adr/001-playwright-choice.md` documenting Playwright decision
- [ ] T049 Final integration test: full workflow `--list` → `--show` → `--refresh`
- [x] T050 Verify test coverage ≥60% for critical paths

---

## Parallel Execution Examples

### Within Phase 2 (3 developers)

```bash
# Developer A: Roman numerals + Cache
git checkout -b feature/roman-and-cache
touch src/utils/roman_numerals.py tests/unit/test_roman_numerals.py
touch src/services/cache_manager.py tests/unit/test_cache_manager.py

# Developer B: Wiki Client
git checkout -b feature/wiki-client
touch src/services/wiki_client.py tests/unit/test_wiki_client.py

# Developer C: Exceptions
git checkout -b feature/exceptions
touch src/exceptions.py
```

### Within Phase 3 (2 developers)

```bash
# Developer A: Models + Tests
git checkout -b feature/us1-models
# T014, T015

# Developer B: Parser + Tests
git checkout -b feature/us1-parser
# T016, T017, T018, T019, T020
```

### US1 and US2 in Parallel (after Phase 2)

```bash
# Team A: Phase 3 (US1 - List)
git checkout -b feature/us1-list-tomes
# T014-T024

# Team B: Phase 4 (US2 - Detail)
git checkout -b feature/us2-tome-detail
# T025-T035
```

---

## Task Checklist Summary

| Phase | Tasks | Story | Parallel? |
|-------|-------|-------|-----------|
| 1: Setup | T001-T006 | - | No |
| 2: Foundation | T007-T013 | - | Yes |
| 3: US1 | T014-T024 | US1 | Yes |
| 4: US2 | T025-T035 | US2 | Yes |
| 5: CLI | T036-T043 | - | Partial |
| 6: Polish | T044-T050 | - | Yes |

**Total**: 50 tasks  
**MVP Scope**: Phase 1-3 (US1 only) = 24 tasks

---

## MVP Recommendation

**Implement Phase 1-3 first** to deliver a working `--list` command:

1. Can list all Tomes grouped by 7 categories
2. Cache works (faster subsequent runs)
3. Excludes "Other Tomes" as required

This provides immediate value while US2 (details) is being developed in parallel.
