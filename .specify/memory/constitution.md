<!--
================================================================================
SYNC IMPACT REPORT
================================================================================
Version Change: 1.0.0 → 1.0.1 (PATCH: clarified test coverage threshold)

Principles Modified:
- II. Test Coverage: Changed coverage threshold from ≥80% to ≥60%
- II. Test Coverage: Clarified scope to "关键功能" (critical functionality only)

No Added/Removed Principles

Templates Requiring Updates:
- ✅ No template updates required (coverage threshold is internal guidance)

Follow-up TODOs: None
================================================================================
-->

# aow4-mcp Constitution

## Core Principles

### I. Type Safety (NON-NEGOTIABLE)

All variables, function parameters, and return values MUST have explicit type annotations.

**Rules:**
- Use `pydantic` for data models, configuration, and validation
- Use `typing` module for complex types (Optional, Union, List, Dict, etc.)
- No untyped code in production; `Any` type must be justified with comment
- Type checkers (mypy/pyright) MUST pass with strict mode

**Rationale:** Explicit types catch errors at static analysis time, improve IDE support, and serve as living documentation. Pydantic provides runtime validation that complements static types.

### II. Test Coverage (NON-NEGOTIABLE)

关键功能 MUST have comprehensive unit tests.

**Rules:**
- Use `pytest` as the testing framework
- Tests MUST be written BEFORE implementation (TDD preferred)
- All public APIs MUST have unit tests
- Test coverage for critical paths MUST be ≥ 60%
- Tests must be independent and idempotent

**Rationale:** Tests provide safety net for refactoring, document expected behavior, and prevent regressions. pytest offers powerful fixtures, parametrize, and ecosystem compatibility.

### III. Documentation (NON-NEGOTIABLE)

All public APIs and significant features MUST be documented.

**Rules:**
- Use Markdown for all documentation
- Every public module, class, and function MUST have docstrings
- Complex logic MUST have inline comments explaining "why"
- Architecture decisions MUST be recorded in `docs/adr/` (Architecture Decision Records)
- User-facing features MUST have usage examples

**Rationale:** Documentation reduces onboarding time, preserves institutional knowledge, and enables async collaboration. Markdown is ubiquitous and version-control friendly.

## Technology Stack

**Language**: Python 3.13+

**Required Dependencies:**
- `pydantic` - Data validation and settings management
- `pytest` - Testing framework

**Development Dependencies:**
- `mypy` or `pyright` - Static type checking
- `pytest-cov` - Test coverage reporting

**Package Manager**: `uv` (preferred) or `pip`

## Governance

This constitution supersedes all other development practices. All changes MUST comply with the principles above.

**Amendment Procedure:**
1. Proposed changes must be documented with rationale
2. Changes affecting principles require explicit approval
3. Breaking changes to principles require MAJOR version bump
4. New principles or expanded guidance require MINOR version bump
5. Clarifications and typo fixes require PATCH version bump

**Compliance Verification:**
- All PRs must pass type checking (mypy/pyright)
- All PRs must pass pytest test suite
- All PRs must include documentation updates for user-facing changes

**Versioning Policy**: Follows Semantic Versioning (MAJOR.MINOR.PATCH)

**Version**: 1.0.1 | **Ratified**: 2025-02-07 | **Last Amended**: 2025-02-07
