# Implementation Plan: AOW4 Tome Scraper

**Branch**: `002-aow4-tome-scraper` | **Date**: 2025-02-07 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-aow4-tome-scraper/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

开发一个CLI工具，从AOW4 Wiki抓取Tome信息。使用Playwright获取页面内容，Redis作为缓存层存储抓取结果。提供 `--list` 列出所有Tome，`--show <Tome>` 查看详情，`--refresh` 刷新缓存。数据模型包括Tome、Tome Detail和Tome Skill。

## Technical Context

**Language/Version**: Python 3.13+ (per constitution)  
**Primary Dependencies**: Playwright (页面抓取), Redis-py (缓存), Pydantic (数据模型), Typer/Click (CLI框架)  
**Storage**: Redis (缓存，永不过期，用户手动刷新)  
**Testing**: pytest (per constitution: Type Safety + Test Coverage requirements)  
**Target Platform**: Cross-platform CLI (Linux/macOS/Windows)  
**Project Type**: single CLI application  
**Performance Goals**: Tome列表获取 < 10秒，单个详情获取 < 5秒  
**Constraints**: 缓存优先策略，Wiki结构变更时需重新适配解析逻辑  
**Scale/Scope**: 约60+ Tome，7个大类，单用户本地使用

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| **I. Type Safety** | ✓ PASS | 使用 Pydantic 定义所有数据模型 (Tome, TomeDetail, TomeSkill)，Playwright和Redis操作都将有类型注解 |
| **II. Test Coverage** | ✓ PASS | pytest测试框架；关键路径：Wiki抓取、缓存机制、数据解析；测试覆盖Tome列表七个大类验证、详情解析、缓存刷新逻辑 |
| **III. Documentation** | ✓ PASS | CLI --help自动生成，代码docstrings，ADR记录Playwright选择理由 |

**Gate Result**: ✓ ALL PASS - Proceed to Phase 0

## Project Structure

### Documentation (this feature)

```text
specs/002-aow4-tome-scraper/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
src/
├── models/              # Pydantic models: Tome, TomeDetail, TomeSkill
├── services/            # Core services: WikiScraper, CacheManager
├── cli.py               # CLI entry point (Typer/Click)
└── config.py            # Configuration (Redis connection, etc.)

tests/
├── unit/                # Unit tests for models, services
├── integration/         # Integration tests for Wiki scraping
└── conftest.py          # pytest fixtures (Redis mock, Playwright mock)
```

**Structure Decision**: Single CLI application (Option 1).使用模块化结构分离模型、服务和CLI层，便于测试和维护。

## Phase Completion

### Phase 0: Research ✓
- [research.md](./research.md) - Technology decisions documented

### Phase 1: Design ✓
- [data-model.md](./data-model.md) - Entity models defined
- [contracts/cli-interface.md](./contracts/cli-interface.md) - CLI contract defined
- [quickstart.md](./quickstart.md) - Usage documentation

---

## Post-Design Constitution Check

| Principle | Status | Verification |
|-----------|--------|--------------|
| **I. Type Safety** | ✓ PASS | Pydantic models defined for Tome, TomeDetail, TomeSkill; all fields typed |
| **II. Test Coverage** | ✓ PASS | Test cases defined for: 7 categories validation, roman numeral conversion, cache refresh logic |
| **III. Documentation** | ✓ PASS | CLI contract documented, quickstart guide created, data model documented |

**Final Gate Result**: ✓ ALL PASS

---

## Next Step

Run `/speckit.tasks` to generate the implementation task list.

## Complexity Tracking

> No violations - all principles satisfied with standard patterns.
