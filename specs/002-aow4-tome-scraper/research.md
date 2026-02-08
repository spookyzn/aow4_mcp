# Phase 0: Research & Decisions

**Feature**: AOW4 Tome Scraper  
**Date**: 2025-02-07

---

## 1. Web Scraping Technology

### Decision: Use Playwright

**Rationale**:
- AOW4 Wiki使用JavaScript动态渲染内容，传统的requests+BeautifulSoup无法正确抓取
- Playwright支持完整的浏览器自动化，可以等待页面加载完成并执行JavaScript
- 能够处理可能的AJAX请求和动态内容
- 与Python生态集成良好

**Alternatives Considered**:
- **requests + BeautifulSoup**: 拒绝，无法处理动态渲染的Wiki页面
- **Selenium**: 功能相似但Playwright API更现代化，性能更好，维护更活跃
- **Scrapy**: 过于重量级，本项目只需要简单抓取两个页面

---

## 2. Caching Strategy

### Decision: Redis with Permanent Storage

**Rationale**:
- 缓存永不过期，避免重复请求Wiki（减少服务器压力，提高响应速度）
- 用户通过 `--refresh` 显式控制缓存刷新时机
- Redis数据结构丰富，适合存储JSON序列化的Tome数据

**Cache Key Design**:
- `aow4:tome:list` - 存储Tome列表（全部7大类）
- `aow4:tome:detail:{tome_name}` - 存储单个Tome详情

**Alternatives Considered**:
- **SQLite本地文件**: 拒绝，Redis更轻量，API更简单
- **文件系统缓存**: 拒绝，难以原子操作，并发问题
- **内存缓存**: 拒绝，进程重启后数据丢失

---

## 3. CLI Framework

### Decision: Use Typer

**Rationale**:
- 基于Python类型注解，自动生成功能完整的CLI
- 内置 `--help` 生成，符合文档要求
- 与现代Python工具链集成良好
- 支持命令参数、选项、子命令

**CLI Design**:
```bash
aow4-tome --list              # 列出所有Tome
aow4-tome --show "Nature"     # 显示指定Tome详情
aow4-tome --refresh           # 强制刷新缓存
```

**Alternatives Considered**:
- **Click**: Typer的底层，但Typer更简洁现代
- **argparse**: 标准库但API冗长，类型支持弱
- **Fire**: 过于自动魔法，难以精确控制CLI行为

---

## 4. Data Parsing Strategy

### Decision: CSS Selectors + Regex

**Rationale**:
- Wiki页面结构相对稳定，CSS选择器可以精确定位元素
- Playwright原生支持querySelector
- 罗马数字转换使用标准库 `roman` 或自定义映射

**Roman Numeral Mapping**:
```python
ROMAN_TO_INT = {
    'I': 1, 'II': 2, 'III': 3, 'IV': 4,
    'V': 5, 'VI': 6, 'VII': 7
}
```

**Parsing Targets**:
- Tome列表：解析 https://aow4.paradoxwikis.com/Tomes 的表格/列表
- Tome详情：解析页面中的Summary段落、Tome Skills表格、右侧信息栏

---

## 5. Project Dependencies

### Core Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| `playwright` | 浏览器自动化 | latest |
| `redis` | 缓存存储 | latest |
| `pydantic` | 数据模型 (constitution required) | latest |
| `typer` | CLI框架 | latest |
| `rich` | 格式化输出（表格、颜色） | latest |

### Dev Dependencies

| Package | Purpose |
|---------|---------|
| `pytest` | 测试框架 (constitution required) |
| `pytest-asyncio` | 异步测试支持 |
| `pytest-mock` | Mock工具 |
| `fakeredis` | Redis测试mock |
| `mypy` | 类型检查 |

---

## 6. Error Handling Strategy

### Decision: Layered Error Handling

**Network Layer**:
- Playwright timeout: 30秒
- 连接失败：返回用户友好的错误信息
- HTTP 404："Tome不存在"提示

**Parsing Layer**:
- HTML结构变更：记录详细错误日志
- 缺失字段：使用Optional类型，允许部分数据

**Cache Layer**:
- Redis连接失败：优雅降级到直接抓取
- 序列化错误：记录并清理损坏的缓存

---

## 7. Testing Strategy

### Test Categories

1. **Unit Tests**: 模型验证、罗马数字转换、缓存逻辑
2. **Integration Tests**: Wiki抓取（使用mock HTML）
3. **CLI Tests**: 命令行参数解析、输出格式

### Critical Test Cases

- ✓ Tome列表只有7个大类，没有"Other Tomes"
- ✓ 罗马数字正确转换为整数
- ✓ 缓存命中时不再请求Wiki
- ✓ `--refresh` 强制刷新缓存

---

## 8. Open Questions Resolved

| Question | Decision | Rationale |
|----------|----------|-----------|
| 缓存过期策略 | 永不过期 | 减少Wiki服务器压力，数据相对静态 |
| 输出格式 | Rich表格 + JSON | 交互式使用表格，脚本使用JSON |
| 错误处理 | 异常类层级 | 清晰区分网络/解析/缓存错误 |

---

## Research Complete

All technical decisions made. Proceeding to Phase 1: Design & Contracts.
