# Data Model: AOW4 Tome Scraper

**Feature**: AOW4 Tome Scraper  
**Date**: 2025-02-07

---

## Entity Overview

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│     Tome        │────▶│   TomeDetail     │────▶│   TomeSkill     │
├─────────────────┤     ├──────────────────┤     ├─────────────────┤
│ - name: str     │     │ - name: str      │     │ - name: str     │
│ - tier: int     │     │ - tier: int      │     │ - tier: int     │
│ - category: str │     │ - category: str  │     │ - type: list    │
│ - link: str     │     │ - summary: str   │     │ - effects: list │
└─────────────────┘     │ - tome_skills: []│     │ - units: list   │
                        │ - tome_info: dict│     └─────────────────┘
                        └──────────────────┘
```

---

## 1. Tome (Basic Info)

**Purpose**: 代表Tome的基本信息，用于列表展示

**Fields**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `str` | ✓ | Tome名称（如 "Nature's Wrath"） |
| `tier` | `int` | ✓ | 等级，罗马数字转换为整数（1-7） |
| `category` | `str` | ✓ | 所属大类（7大类之一） |
| `link` | `str` | ✓ | Wiki页面完整URL |

**Validation Rules**:
- `tier` 必须在 1-7 范围内
- `category` 必须是7个有效大类之一
- `link` 必须是有效的HTTP(S) URL

**Example**:
```python
{
    "name": "Nature's Wrath",
    "tier": 3,
    "category": "Nature",
    "link": "https://aow4.paradoxwikis.com/Nature's_Wrath"
}
```

---

## 2. TomeDetail (Full Info)

**Purpose**: 代表Tome的完整详细信息

**Fields**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `str` | ✓ | Tome名称 |
| `tier` | `int` | ✓ | 等级（1-7） |
| `category` | `str` | ✓ | 所属大类 |
| `summary` | `str` | ✓ | Tome描述性介绍 |
| `tome_skills` | `list[TomeSkill]` | ✓ | 该Tome提供的技能列表 |
| `tome_info` | `dict` | ✓ | 右侧信息栏的键值对 |

**Validation Rules**:
- `summary` 不能为空字符串
- `tome_skills` 可以为空列表（某些Tome可能没有技能）
- `tome_info` 包含页面右侧的所有属性（Tier, Type, Unlocks等）

**Example**:
```python
{
    "name": "Nature's Wrath",
    "tier": 3,
    "category": "Nature",
    "summary": "This tome focuses on...",
    "tome_skills": [
        {
            "name": "Entangling Vines",
            "tier": 1,
            "type": ["Battle Magic"],
            "effects": ["Immobilizes enemy units"],
            "units": None
        }
    ],
    "tome_info": {
        "Tier": "III",
        "Type": "Nature",
        "Unlocks": "Requires Nature I"
    }
}
```

---

## 3. TomeSkill (Skill Info)

**Purpose**: 代表Tome提供的单个技能

**Fields**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `str` | ✓ | 技能名称 |
| `tier` | `int` | ✓ | 技能等级（1-7） |
| `type` | `list[str]` | ✓ | 技能类型列表（如 ["Battle Magic", "Summoning"]） |
| `effects` | `list[str]` | ✓ | 技能效果描述列表 |
| `units` | `list[str] \| None` | ✓ | 可解锁的单位类型，None表示无单位 |

**Validation Rules**:
- `type` 至少包含一个元素
- `effects` 至少包含一个元素
- `units` 可为None或有效单位类型列表（Shield, Fighter, Shock等）

**Unit Types**:
- Shield
- Fighter
- Shock
- Ranged
- Support
- Cavalry
- Flying
- Siege

**Example**:
```python
{
    "name": "Summon Treant",
    "tier": 3,
    "type": ["Summoning", "Nature"],
    "effects": ["Summons a Treant unit", "Lasts 3 turns"],
    "units": ["Support"]
}
```

---

## 4. Cache Data Structure

### Redis Keys

| Key Pattern | Value Type | TTL | Description |
|-------------|------------|-----|-------------|
| `aow4:tome:list` | JSON string | Never | 所有Tome列表（序列化的list[Tome]） |
| `aow4:tome:detail:{name}` | JSON string | Never | 单个Tome详情（序列化的TomeDetail） |

### Cache Hit Flow

```
User Request ──▶ Check Redis ──▶ Cache Hit? ──Yes──▶ Return Data
                                      │
                                      No
                                      ▼
                              Fetch from Wiki
                                      │
                                      ▼
                              Store in Redis
                                      │
                                      ▼
                              Return Data
```

---

## 5. Pydantic Model Definitions

```python
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional, Dict, Any

class Tome(BaseModel):
    """Basic Tome information for listing."""
    name: str = Field(..., description="Tome name")
    tier: int = Field(..., ge=1, le=7, description="Tome tier (1-7)")
    category: str = Field(..., description="Tome category (one of 7 main types)")
    link: HttpUrl = Field(..., description="Wiki page URL")

class TomeSkill(BaseModel):
    """Skill provided by a Tome."""
    name: str = Field(..., description="Skill name")
    tier: int = Field(..., ge=1, le=7, description="Skill tier (1-7)")
    type: List[str] = Field(..., min_length=1, description="Skill types")
    effects: List[str] = Field(..., min_length=1, description="Skill effects")
    units: Optional[List[str]] = Field(None, description="Unlockable unit types")

class TomeDetail(BaseModel):
    """Detailed Tome information."""
    name: str = Field(..., description="Tome name")
    tier: int = Field(..., ge=1, le=7, description="Tome tier (1-7)")
    category: str = Field(..., description="Tome category")
    summary: str = Field(..., min_length=1, description="Tome description")
    tome_skills: List[TomeSkill] = Field(default_factory=list, description="Tome skills")
    tome_info: Dict[str, Any] = Field(default_factory=dict, description="Additional info from sidebar")
```

---

## 6. Category Validation

### Valid Categories (7大类)

```python
VALID_CATEGORIES = [
    "Nature",
    "Chaos", 
    "Order",
    "Shadow",
    "Creation",
    "Destruction",
    "Materium"
]
```

**Important**: Wiki页面上的 "Other Tomes" 分类应被**排除**在抓取范围外。
