---
name: aow4_tome
description: 当询问奇迹时代4(AOW4)魔典(Tome)信息，或者询问相关魔典问题，魔典出发什么技能；提供初始魔典后，后续魔典如何选择；最佳的魔典选择路径，最优的魔典选择路径
allowed-tools: 
disable: false
---

## CRITICAL: 必须严格按照规则进行魔典解锁，不可以跳过规则选择未解锁的魔典
- 永远可以解锁所有一级魔典
- 解锁所有二级魔典时，之前必须已经解锁了2本魔典
- 解锁所有三级魔典时，之前必须已经解锁了4本魔典
- 解锁所有四级魔典时，之前必须已经解锁了6本魔典
- 解锁所有五级魔典时，之前必须已经解锁了8本魔典

## CRITICAL: 解锁三级，四级Hybrid魔典时，必须参考魔典列表中的affinity字段 
- 解锁三级Hybrid魔典时，之前必须已经解锁了4本魔典，且魔典的所需的Affinity相加 >= 3
```
# 比如: 三级Hybrid魔典`Dragons`, affinity 字段为。
    "affinity": [
      "+1 Chaos",
      "+1 Nature"
    ]
# 所以， 解锁`Dragons` 需要Affinity点, Chaos+Natrue>=3; 也就是 2点Chaos+1点Nature，或者 1点Chaos+2点Nature 即可解决
```
- 解锁四级Hybrid魔典时，之前必须已经解锁了6本魔典，且魔典的所需的Affinity相加 >= 6

## 魔典解锁规则
### 解锁规则如下:
- Tier I tomes are always available
- Tier II tomes require 2 tomes
- Tier III tomes require 4 tomes and 3 points in their affinity
- Tier IV tomes require 6 tomes and 6 points in their affinity
- Tier V tomes require 8 tomes and 8 points in their affinity and only one tier V tome can be unlocked per game
- 一级魔典：始终可用
- 二级魔典：需要 2 本魔典
- 三级魔典：需要 4 本魔典且Affinity >= 3 点
- 四级魔典：需要 6 本魔典且Affinity >= 6 点
- 五级魔典：需要 8 本魔典且Affinity >= 8 点，且每局游戏只能解锁一本五级魔典


## 最佳选择策略
- 第2, 3, 4本魔典可以按起始魔典的 Affinity 点数来选择。 比如：某一 Affinity 点数>=6，或者某2种 Affinity 点数相加>=6
- 第5，6 本魔典选择不用在意魔典 Affinity 种类，可以按魔典中的单位附魔技能为优先。一级，二级魔典优先。选择时考虑魔典中的单位附魔技能，与之前单位附魔技能交集越大的魔典。比如：之前魔典技能加强的是远程单位，那后续魔典就尽量选择远程单位的魔典。
- 第7，8 本魔典必须是四级魔典
- 第9本魔典必须是五级魔典


## 获取魔典数据
获取数据时，第一优先使用缓存中的数据。除非用户明确指出不使用缓存数据


## 技能统计方法 

按如下方式分类统计单位附魔技能
- Unit Enchantment
    - Ranged Unit
    - Skirmisher Unit
    - Battle Mage Unit
    - Support Unit
    - Shield Unit
    - Fighter Unit
    - Polearm Unit

按如下Spell分类统计新技能
- New Spells
    - Damage Spell
    - Summon Spell
    - Buff Spell
    - Debuff Spell
    - Friendly Army Spell
    - Terraforming Spell
    - Sustained City Spell
    - Enemy army spell
    - Other Spells

按如下变形分类统计新特性
- Transformation
    - Minor race transformation
    - Major race transformation

- Unit

## 核心工作步骤 

### Step 1
用户必须先给出起始魔典的名字。同时提供种族的Affinity点数各是多少

比如：
```
文化：封建-帝君
起始魔典: 野兽
Affinity 点数: 自然+2; 物质+2
```

### Step 2
读取起始魔典的具体信息。按奇迹时代4专家推荐的技能选择规则选取3-4个技能。

### Step 3 
1. 按上面的`魔典解锁规则`查看当前可以解锁的魔典。
2. 按文中的最佳选择策略，选择下一本魔典 
3. 加上选择魔典的Affinity点
4. 按奇迹时代4专家推荐的技能选择规则选取4个技能，优先考虑单位附魔技能

### Step 4
按上面的`魔典解锁规则`，判断是否可以解锁五级魔典。
- 可以找到可用魔典，选择该魔典为最后一本。进入Step 5
- 无法找到可用五级魔典，返回Step 3 

### Step 5 
- 找到最优的路径后，给出最优的魔典选择路径及相关信息
- 最好给结果起一个符合逻辑的名字，可以按学习的魔典和技能来命名

比如:
```
# 物质狂热远程流

## 魔典选择路径
- <起始魔典 级别> (当前affinity点数)
    - [技能1]
    - [技能2]
    - [技能3]
- [选择的魔典1 级别] (当前affinity点数)
    - [技能1]
    - [技能2]
    - [技能3]
    - [技能4]
...
- [最终五级魔典] (当前affinity点数)

## 技能统计结果
按上面的技能统计方法把所有技能统计结果进行汇总
```

## Best Practice

### 一定做的事情
- ✅ 必须严格遵守魔典解锁规则
- ✅ Affinity 点数必须严格按照魔典列表中的affinity字段
- ✅ 解锁 III, IV 级混合魔典时，必须满足两种Affinity的相加要求
- ✅ 混合魔典只算一本，不算两本

### 一定不要做的事情
- ❌ 不要跳过魔典解锁规则，比如：解锁四级魔典时，之前只解锁了5本魔典。解锁五级魔典时，之前只解锁了7本魔典。
- ❌ 不要把一本Hybrid魔典计算为2本。该类魔典只是拥有2种Affinity点数。并不是两本魔典
- ❌ 不要捏造魔典的Affinity点数

