---
name: aow4_tome
description: 当询问奇迹时代4(AOW4)魔典(Tome)信息，或者询问相关魔典问题，魔典出发什么技能；提供初始魔典后，后续魔典如何选择；最佳的魔典选择路径，最优的魔典选择路径
allowed-tools: 
disable: false
---

## CRITICAL: 必须严格按照规则进行魔典解锁，不可以跳过规则选择未解锁的魔典
- 魔典级别参考tier字段，魔典affinity点数参考affinity字段
- 解锁二级魔典时，之前必须已经解锁了2本魔典
- 解锁三级魔典时，之前必须已经解锁了4本魔典，且魔典的所需的Affinity >= 3
- 解锁四级魔典时，之前必须已经解锁了6本魔典, 且魔典的所需的Affinity >= 6  
- 解锁五级魔典时，之前必须已经解锁了8本魔典, 且魔典的所需的Affinity >= 8  

## CRITICAL: 解锁Hybrid魔典时，必须参考魔典列表中的affinity字段 
- 永远可以解锁一级Hybrid魔典
- 解锁二级Hybrid魔典时，之前必须已经解锁了2本魔典
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
- 混合魔典的一级、二级、三级、四级和五级解锁方式与非混合魔典相同；混合魔典的所属亲和，魔典列表中的affinity字段


## 获取魔典数据
获取数据时，第一优先使用缓存中的数据。除非用户明确指出不使用缓存数据


## 技能统计方法 
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
起始魔典: 野兽
种族点数: 自然+2; 物质+2
```

### Step 2
读取起始魔典的具体信息。按奇迹时代4专家推荐的技能选择规则选取3-4个技能。

### Step 3 
1. 按上面的`魔典解锁规则`查看当前可以解锁的魔典。
2. 查看所有可用魔典之中的技能。优先考虑有单位附魔的魔典，并且和之前选择魔典中的单位附魔技能交集越大的。 其次按奇迹时代4专家思维方式，依据之前已经选择的魔典，选择一个最合适的魔典 
4. 按奇迹时代4专家推荐的技能选择规则选取3-4个技能

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
- <起始魔典> (当前affinity点数)
    - [技能1]
    - [技能2]
    - [技能3]
- [选择的魔典1] (当前affinity点数)
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
- ✅ 最后结果报表显示，必须要显示单位附魔的统计效果 

### 一定不要做的事情
- ❌ 不要跳过魔典解锁规则，比如：解锁四级魔典时，之前只解锁了5本魔典。解锁五级魔典时，之前只解锁了7本魔典。