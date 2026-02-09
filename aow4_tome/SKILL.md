---
name: aow4_tome
description: 当询问奇迹时代4(AOW4)魔典(Tome)信息，或者询问相关魔典问题，魔典出发什么技能；提供初始魔典后，后续魔典如何选择；最佳的魔典选择路径，最优的魔典选择路径
---

# 魔典选择规则

## 魔典解锁规则
`最重要: 必须严格按照规则进行魔典解锁，不可以跳过规则选择为解锁的魔典。`

规则如下:
- Tier I tomes are always available
- Tier II tomes require 2 tomes
- Tier III tomes require 4 tomes and 3 points in their affinity
- Tier IV tomes require 6 tomes and 6 points in their affinity
- Tier V tomes require 8 tomes and 8 points in their affinity and only one tier V tome can be unlocked per game


## 获取魔典数据
获取数据时，第一优先使用缓存中的数据。除非用户明确指出不使用缓存数据


## 技能统计方法 

`最重要: 统计时把增强效果累加，按类别分别统计`
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


## Instruction 

### Step 1
用户必须先给出起始魔典的名字。同时提供种族的Affinity点数各是多少

比如：
```
起始魔典: 野兽
种族点数: 自然+2; 物质+2
```

### Step 2
读取起始魔典的具体信息。随机选取4个技能, 按上面的技能统计方法进行统计


### Step 3 
1. 按上面的魔典解锁规则选择下一个可以解锁的魔典。
2. 随机选取4个技能, 按上面的技能统计方法进行统计
3. 再次按上面的魔典解锁规则选择可以解锁的魔典, 直到可以选到第一本五级魔典为止

### Step 4
比较所有路径的技能统计结果，提供最优的魔典选择路径
判断最优的路径的规则如下，优先级从高到低
1. 按照单位增强效果
2. 按照技能强度进行评分，强度越高越好

### Step 5
- 找到最优的路径后，给出最优的魔典选择路径及相关信息
- 最好给结果起一个符合逻辑的名字，可以按学习的魔典和技能来命名

比如:
```
# 物质狂热远程流

## 魔典选择路径
- <起始魔典>
    - [技能1]
    - [技能2]
    - [技能3]
    - [技能4]
- [选择的魔典1]
    - [技能1]
    - [技能2]
    - [技能3]
    - [技能4]
...
- [第一本选中的五级魔典]

## 技能统计结果
按上面的技能统计方法把所有技能统计结果进行汇总
```
