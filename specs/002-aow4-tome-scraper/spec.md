# Feature Specification: AOW4 Tome Scraper

**Feature Branch**: `002-aow4-tome-scraper`  
**Created**: 2025-02-07  
**Status**: Draft  
**Input**: User description: "开发一个通过读取AOW4 Wiki获取Tome相关信息的功能，包括获取所有Tome列表和指定Tome的详细信息"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - 获取所有Tome列表 (Priority: P1)

作为AOW4玩家，我想要获取游戏中所有Tome的完整列表，以便了解可用的魔法书种类。

**Why this priority**: 这是基础功能，用户首先需要知道有哪些Tome存在，才能进一步查询特定Tome的详细信息。

**Independent Test**: 可以独立测试，通过调用功能获取Tome列表并验证返回了七个大类约60+个Tome的基本信息。

**Acceptance Scenarios**:

1. **Given** Wiki页面可访问, **When** 请求获取所有Tome列表, **Then** 系统返回包含所有Tome名称、分类和链接的列表
2. **Given** 返回的Tome列表, **When** 检查数据结构, **Then** 每个Tome包含名称、所属大类、Wiki链接地址
3. **Given** 完整的Tome列表, **When** 统计数量, **Then** 包含约60+个Tome，分为7个大类（如Nature, Chaos, Order等）

---

### User Story 2 - 获取指定Tome详细信息 (Priority: P1)

作为AOW4玩家，我想要查看特定Tome的详细信息，包括Summary、技能和属性，以便做出游戏策略决策。

**Why this priority**: 与Story 1同等重要，用户获取列表后需要查看详情来深入了解每个Tome的特性。

**Independent Test**: 可以独立测试，通过提供Tome链接获取详细信息并验证包含Summary、Tome技能和侧边栏属性。

**Acceptance Scenarios**:

1. **Given** 有效的Tome Wiki链接, **When** 请求获取该Tome详情, **Then** 系统返回包含Summary、Tome skills和属性信息的数据
2. **Given** 返回的Tome详情, **When** 检查Summary字段, **Then** 包含Tome的描述性文本介绍
3. **Given** 返回的Tome详情, **When** 检查Tome skills字段, **Then** 包含该Tome提供的所有技能列表
4. **Given** 返回的Tome详情, **When** 检查属性信息, **Then** 包含页面右侧信息栏中的关键属性（如等级、类型、解锁条件等）

---

### Edge Cases

- **网络不可用时**: 系统应返回友好的错误提示，说明无法连接到Wiki
- **Wiki页面结构变更时**: 如果页面HTML结构改变导致解析失败，系统应返回解析错误并提供调试信息
- **Tome链接无效时**: 当提供的Tome链接不存在或返回404时，系统应返回"Tome不存在"的明确提示
- **Wiki响应超时**: 如果Wiki响应时间超过合理阈值（如30秒），系统应处理超时并提供重试选项

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: 系统必须能够从 https://aow4.paradoxwikis.com/Tomes 获取完整的Tome列表
- **FR-002**: Tome列表必须包含每个Tome的名称、所属大类（Nature、Chaos、Order等共7类）、Wiki页面链接
- **FR-003**: 系统必须能够根据Tome的Wiki链接获取该Tome的详细信息
- **FR-004**: Tome详细信息必须包含Summary（描述性介绍）
- **FR-005**: Tome详细信息必须包含Tome skills（该Tome提供的所有技能）
- **FR-006**: Tome详细信息必须包含页面右侧信息栏中的关键属性（如等级、类型、解锁条件等）
- **FR-007**: 系统必须处理网络异常，包括连接失败、超时、HTTP错误等
- **FR-008**: 系统必须提供清晰的错误信息，帮助用户理解问题原因

### Key Entities *(include if feature involves data)*

- **Tome列表项**: 代表单个Tome的基本信息，包含名称(name)、分类(category)、链接(url)
- **Tome详情**: 代表单个Tome的完整信息，包含名称(name)、分类(category)、Summary(summary)、技能列表(skills)、属性信息(properties)
- **技能**: 代表Tome提供的技能，包含名称(name)、描述(description)、解锁条件(unlock_condition)
- **属性信息**: 代表Tome的关键属性，包含等级(tier)、类型(type)、解锁要求(unlock_requirement)、成本(cost)等

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 系统能够在10秒内获取完整的Tome列表（约60+个Tome）
- **SC-002**: Tome列表数据的完整性达到100%（所有Wiki上的Tome都被成功抓取）
- **SC-003**: 单个Tome详情获取时间在5秒内完成
- **SC-004**: 抓取的数据准确率不低于95%（Summary、Skills、属性信息正确提取）
- **SC-005**: 系统能够处理所有常见的网络异常情况，并提供用户友好的错误提示
- **SC-006**: 用户能够通过简单的接口调用获取所需数据，无需了解Wiki页面结构

## Assumptions

- Wiki页面结构相对稳定，不会有频繁的重大结构变更
- Wiki页面使用HTML格式，可以通过DOM解析提取数据
- 用户有基本的网络连接能力访问Wiki
- 七个大类的分类方式与Wiki当前展示一致
- Tome技能信息在页面上有明确的标识和格式

## Dependencies

- 依赖AOW4 Wiki网站的可访问性 (https://aow4.paradoxwikis.com)
- 需要网络请求能力来获取Wiki页面内容
- 需要HTML解析能力来提取结构化数据
