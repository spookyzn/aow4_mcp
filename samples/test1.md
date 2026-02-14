用户询问的是奇迹时代4(AOW4)的魔典构建问题。用户提供了：
- 种族点数：秩序+2；暗影+1；自然+1
- 起始魔典：狂热

用户想知道如何构建最佳魔典BUILD。

根据available_skills中有一个aow4_tome技能，描述是：
"当询问奇迹时代4(AOW4)魔典(Tome)信息，或者询问相关魔典问题，魔典出发什么技能；提供初始魔典后，后续魔典如何选择；最佳的魔典选择路径，最优的魔典选择路径"

这正好符合用户的需求！我应该使用这个技能来回答问题。

让我加载这个技能。
我来帮你分析奇迹时代4的魔典构建方案。让我加载专门的魔典技能来为你提供详细建议。
好的，现在技能已经加载了。我需要按照技能中的步骤来处理用户的请求。

用户提供的信息：
- 种族点数：秩序+2；暗影+1；自然+1
- 起始魔典：狂热

按照技能的步骤：

Step 1: 用户已经提供了起始魔典和种族Affinity点数
- 起始魔典: 狂热
- 种族点数: 秩序+2; 暗影+1; 自然+1

Step 2: 需要读取起始魔典的具体信息，然后选择3-4个技能

Step 3: 根据魔典解锁规则查看可以解锁的魔典，选择最合适的魔典

Step 4: 判断是否可以解锁五级魔典

Step 5: 给出最优的魔典选择路径

首先，我需要调用MCP工具来获取魔典数据。根据技能说明，我应该使用缓存数据。让我先查看一下MCP工具的描述。
我来帮你构建最佳的魔典BUILD。首先让我获取起始魔典"狂热"的详细信息。
好的，现在我知道如何调用get_tome_detail工具了。我需要传入魔典名称和是否使用缓存。

让我先获取起始魔典"狂热"的详细信息。根据技能说明，应该优先使用缓存数据，所以我设置use_cache为true。
看起来中文名称"狂热"没有找到。我需要尝试英文名称。让我先列出所有可用的魔典，看看正确的名称是什么。
好的，让我先列出所有魔典，找到"狂热"对应的英文名称。
-
好的，我找到了所有魔典列表。"狂热"应该对应的是"Zeal"，它是一级秩序魔典。

现在我需要：
1. 获取Zeal魔典的详细信息
2. 根据技能说明选择3-4个技能
3. 然后根据魔典解锁规则，选择后续魔典

用户的种族点数是：
- 秩序(Order): +2
- 暗影(Shadow): +1
- 自然(Nature): +1

起始魔典：Zeal (秩序一级魔典)

让我先获取Zeal魔典的详细信息。
好的，我获得了Zeal魔典的详细信息。现在我需要按照技能的规则，选择3-4个技能。

根据技能描述，我需要按奇迹时代4专家推荐的技能选择规则来选取技能。虽然没有具体的规则说明，但从魔典信息来看，我应该优先考虑：
1. 单位附魔(Unit enchantment) - 这个很重要
2. 新法术，特别是召唤法术
3. 增益法术

Zeal魔典的技能：
1. Condemnation - 伤害/减益法术
2. Summon Zealot - 召唤法术
3. Fanatical Workforce - 城市法术
4. Legion of Zeal - 单位附魔 (影响Shield Unit, Polearm Unit, Fighter Unit, Ranged Unit, Shock Unit, Skirmisher Unit)
5. Inspiring Chant - 增益法术

我应该选择：
- Legion of Zeal (单位附魔，很重要)
- Summon Zealot (召唤法术，提供战斗单位)
- Inspiring Chant (增益法术，与Zeal特性协同)
- Condemnation (伤害/减益法术，可以给敌人施加Condemned状态，与Zealot协同)

现在，根据魔典解锁规则：
- 已解锁魔典：1本 (Zeal)
- 当前Affinity点数：秩序+2; 暗影+1; 自然+1 (种族点数) + 秩序+2 (Zeal魔典) = 秩序+4; 暗影+1; 自然+1

我需要选择第二本魔典。

解锁二级魔典需要2本魔典，但目前已解锁魔典只有1本。因此，我只能选择一级魔典作为下一步。

考虑到我的Affinity分布，我可以选择：
- 秩序类的一级魔典，如Faith
- 暗影类的一级魔典，如Necromancy或Cryomancy
- 自然类的一级魔典，如Beasts或Roots

根据目前的发展路径，我将继续探索这些一级魔典，为后续的魔典解锁做准备。

用户的种族点数和魔典提供的Affinity点数是分开的。种族点数固定为秩序+2、暗影+1、自然+1，而魔典只提供+2点。

解锁魔典的关键在于累积的Affinity点数：
- 一级魔典无需额外要求
- 二级魔典需要2本已解锁魔典
- 三级魔典需要4本已解锁魔典和3点相关Affinity
- 四级魔典需要6本已解锁魔典和6点相关Affinity

我需要重新审视技能规则。

对于混合魔典，解锁要求略有不同：
- 一级Hybrid魔典随时可解锁
- 二级Hybrid魔典需2本已解锁魔典
- 三级Hybrid魔典需4本已解锁魔典和3点混合Affinity

目前可选魔典：
- 一级普通魔典：任何一级魔典
- 一级Hybrid魔典：需要特定Affinity组合

我的Affinity组合：
- 秩序+暗影：可选Revenant
- 秩序+自然：可选Prosperity
- 暗影+自然：无对应Hybrid魔典

推荐方向：
- 首选Discipline或Revenant，因为秩序点数最高
- Discipline提供物质+秩序，适合强化单位
- Revenant结合秩序与暗影，战术潜力强
根据你的种族点数和起始魔典，我来为你构建最佳魔典路径。

## 起始配置
- **种族点数**：秩序+2；暗影+1；自然+1
- **起始魔典**：Zeal (狂热)
- **当前Affinity**：秩序+4；暗影+1；自然+1

## Step 1: 起始魔典Zeal技能选择

从Zeal魔典中选择以下技能：

1. **Legion of Zeal** (单位附魔) - 给近战和远程单位提供Zeal特性，增加精神伤害
2. **Summon Zealot** (召唤法术) - 召唤狂热者单位，对被谴责的敌人有加成
3. **Inspiring Chant** (增益法术) - 提高士气，对有Zeal的单位额外强化
4. **Condemnation** (伤害/减益法术) - 对敌人造成精神伤害并施加谴责状态

让我获取下一本魔典的详细信息：
好的，我获得了Discipline和Faith魔典的信息。

现在让我分析一下这两本魔典：

**Discipline (物质+秩序)**:
1. Mantra of Purification - 治疗法术
2. Monk - 单位(战斗单位)
3. Empowered Strikes - 单位附魔(Shield, Polearm, Fighter, Skirmisher)
4. Focus Aim - 单位附魔(Ranged, Support, Battle Mage)
5. Inner Mastery - 种族改造(状态抗性+1，治疗+20%)

**Faith (秩序+2)**:
1. Faithful Whispers - 持续城市法术
2. Wrath of the Faithful - 伤害法术
3. Staves of Mending - 单位附魔(Support Unit)
4. Army Heal - 友军治疗法术
5. Convent - 城市建筑
6. Summon Lesser Light Spirit - 召唤法术

从Zeal魔典的单位附魔来看，它影响Shield, Polearm, Fighter, Ranged, Shock, Skirmisher单位。

Discipline的单位附魔：
- Empowered Strikes: Shield, Polearm, Fighter, Skirmisher (与Zeal有4个重叠！)
- Focus Aim: Ranged, Support, Battle Mage (与Zeal有1个重叠)

Faith的单位附魔：
- Staves of Mending: Support Unit (与Zeal没有重叠)

看起来Discipline与Zeal的协同性更好！因为它们的单位附魔有大量重叠。

所以我选择Discipline作为第二本魔典。

选择Discipline的技能：
1. Empowered Strikes - 单位附魔，与Zeal协同


2. Focus Aim - 单位附魔，增强远程单位
3. Mantra of Purification - 治疗法术
4. Inner Mastery - 种族改造

Affinity点数发生了变化：
- 秩序点数从4增加到5
- 物质点数从0增加到1
- 暗影点数保持1
- 自然点数保持1

已解锁魔典数量增加到2本。这意味着可以开始解锁二级魔典。

解锁条件需要满足：
- 二级普通魔典需要2本已解锁魔典
- 二级Hybrid魔典需要2本已解锁魔典

选择二级魔典时，优先考虑单位附魔的魔典，并寻找与已有魔典中单位附魔技能交集最大的选项。

三级魔典解锁更复杂，需要：
- 已解锁4本魔典
- 特定Affinity达到3点以上

目前已解锁魔典仅2本，还不满足三级魔典解锁条件，需要继续解锁二级魔典。

正在探索可能的二级魔典选项，特别关注不同类型的魔典特性。

目前已经解锁了秩序、物质、暗影和自然四种属性。

二级秩序魔典包括The Beacon、The Inquisition和Virtue，每个都提供秩序属性加成。混合类型魔典如The Construct、Fey Mists和Shades也很有趣，它们结合了不同的属性特点。

我将优先考虑秩序属性魔典，因为目前秩序属性已经达到5点，是最高值。

我计划获取The Beacon、The Inquisition或Virtue的详细信息。
好的，我获得了三本二级魔典的信息：

**The Beacon (秩序+2)**:
1. Conjure Divine Beacon - 战斗召唤法术
2. Covenant of the Faith - 持续城市法术
3. Summon Blessed Soul - 召唤法术
4. Mighty Meek - 单位附魔(Tier I Units, Tier II Units)
5. Chaplain - 单位

**Virtue (秩序+2)**:
1. House of Charity - 城市建筑
2. Heroic Stand - 增益法术
3. Virtuous Spirit - 种族改造
4. Summon Vigil - 召唤法术
5. Paladin - 单位

**The Construct (物质+1, 秩序+1)**:
1. Cascading Command: Defend - 增益法术
2. Cascading Command: Reposition - 增益法术
3. Bronze Golem - 单位
4. Compounding Defense - 单位附魔(Shield, Polearm, Fighter)
5. Linked Minds - 种族改造

现在让我分析单位附魔的重叠：

**Zeal的单位附魔**：Shield, Polearm, Fighter, Ranged, Shock, Skirmisher

**The Beacon的单位附魔**：
- Mighty Meek: Tier I Units, Tier II Units (这是一个范围，应该包括所有一级和二级单位)

**Virtue**：没有单位附魔

**The Construct的单位附魔**：
- Compounding Defense: Shield, Polearm, Fighter (与Zeal有3个重叠！)

从单位附魔的重叠来看：
- The Construct与Zeal有3个重叠(Shield, Polearm, Fighter)


- The Beacon是覆盖所有一级和二级单位
- Virtue没有单位附魔

我正在追踪已解锁的魔典和Affinity点数。目前已解锁Zeal和Discipline两本魔典，累计Affinity点数为秩序5、物质1、暗影1和自然1。接下来需要继续解锁二级魔典。

解锁二级魔典后，我会评估不同选项的潜在影响。The Beacon和Virtue提供秩序+2，可能将秩序点数提升至7。The Construct则提供物质+1和秩序+1，可能调整点数构成。我需要比较这些选项的性价比和战略价值。

关键是寻找单位附魔和种族改造的协同效应。The Construct和Discipline的组合看起来很有吸引力，因为它们共享物质和秩序亲和力，并且在单位附魔和种族改造方面有重叠。The Beacon虽然全面覆盖单位等级，但战略深度可能稍显不足。

我将优先选择能最大化单位协同性和战略潜力的魔典。

接下来需要深入评估第三本魔典的具体贡献和战略价值。
-
太好了！The Inquisition魔典与Zeal魔典有非常好的协同！

**The Inquisition (秩序+2)**:
1. Inquisitor - 单位
2. Mass Condemnation - 伤害/减益法术(施加Condemned状态)
3. Burden of Guilt - 敌军法术
4. Tribunal - 城市建筑
5. Inquisitor's Mark - 单位附魔
6. Summon Lightbringer - 召唤法术

关键点：
- **Mass Condemnation**: 施加Condemned状态，与Zeal魔典的Zealot单位协同(Zealot对Condemned敌人有加成)
- **Inquisitor's Mark**: 单位附魔，与Zeal的单位附魔有重叠

这是一个完美的协同！因为：
1. Zeal的Summon Zealot召唤的Zealot对Condemned敌人有优势
2. The Inquisition的Mass Condemnation可以施加Condemned状态
3. The Inquisition的Inquisitor也可以施加Condemned和Stunned
4. Inquisitor's Mark的单位附魔与Zeal有重叠

所以我选择The Inquisition作为第三本魔典！

选择The Inquisition的技能：
1. Mass Condemnation - 伤害/减益法术，与Zealot协同
2. Inquisitor's Mark - 单位附魔，与Zeal协同
3. Inquisitor - 单位
4. Summon Lightbringer - 召唤法术

解锁The Inquisition后：
- 已解锁魔典：3本
- Affinity点数：秩序+7; 物质+1; 暗影+1; 自然+1

接下来需要解锁第四本魔典，才能解锁三级魔典(需要4本已解锁魔典)。

我将比较几个候选魔典：
- The Beacon: 秩序+2，单位附魔覆盖全面
- Virtue: 秩序+2，种族改造独特
- The Construct: 物质+1，秩序+1，与Discipline有协同

Virtue看起来很有吸引力，因为它的种族改造可能会带来独特的战略优势。我需要进一步分析它的具体能力和潜在影响。

不同魔典的选择将影响我的种族发展和战斗策略。

Virtue的种族改造提供强大的战斗增益，尤其是低血量时的防御提升。The Beacon则全面覆盖单位增益。我将权衡种族改造与单位附魔的战术价值。

解锁The Beacon后，我的阵营将获得秩序+9的属性，目前已解锁4本魔典。下一步是寻找合适的三级魔典，重点是单位附魔协同。

当前可用三级魔典包括秩序、暗影和混合类型。秩序类魔典有Sanctuary和Subjugation，暗影类有The Cold Dark和Torment。混合类魔典需要特定亲和力点数，如The Cleansing Flame和Prophecies。我的秩序点数已达+9，为解锁这些魔典提供了有利条件。
-
太棒了！The Cleansing Flame简直是完美的选择！

**The Cleansing Flame (秩序+1, 混沌+1)**:
1. Pureflame Staves - 单位附魔(施加Condemned状态和创造Cleansing Flames)
2. Temple of the Pyre - 城市建筑
3. Zealous Ignition - 增益法术(赋予Zeal或强化已有Zeal，对敌人施加Condemned)
4. Consecrating Firestorm - 世界法术
5. Flame Blessed Champions - 单位附魔
6. Pyre Templar - 单位

关键协同：
1. **Zealous Ignition**: 赋予Zeal特性，与Zeal魔典完美协同！如果目标已经有Zeal，还会额外强化！
2. **Pureflame Staves**: 施加Condemned状态，与Zealot和The Inquisition完美协同！
3. **Flame Blessed Champions**: 单位附魔，与Zeal和Discipline的单位附魔重叠！

这简直是完美的选择！因为：
- 与Zeal魔典的Zeal特性协同
- 与The Inquisition的Condemned状态协同
- 单位附魔与之前的魔典重叠

**Sanctuary的单位附魔**：
- Keeper's Mark: Shield, Shock, Skirmisher, Polearm, Fighter (与Zeal有5个重叠)

**Subjugation的单位附魔**：
- Intimidation Aura: Shield, Shock, Skirmisher, Polearm, Fighter (与Zeal有5个重叠)
 
我选择了The Cleansing Flame作为第五本魔典，主要因为它独特地结合了Zeal和Condemned机制。通过解锁这本魔典，我的阵营获得了秩序+10和混沌+1的属性加成，目前已解锁5本魔典。下一步是锁定第六本魔典，以便解锁四级魔典的潜力。

目前可用的四级秩序魔典包括Exaltation、Supremacy和The Archon，以及多个Hybrid魔典选项。由于秩序属性已达到+10，我正处于解锁更高级魔典的有利位置。不过，我需要继续解锁第六本魔典，以完成解锁四级魔典的要求。

我注意到Sanctuary和Subjugation两个三级魔典可以增加秩序属性。Sanctuary的治疗和防御增益可能更适合我的整体战略，特别是考虑到之前的Zeal和The Inquisition选择。我将仔细评估这两个魔典的单位附魔和特性，以确定最佳选择。

接下来我需要查看其他四级魔典的具体信息，以便做出更明智的决定。
-
好的，我获得了四本四级魔典的信息。让我分析一下：

**Exaltation (秩序+2)**:
1. Temple of the Exalted - 城市建筑
2. Ascended Warriors - 友军法术
3. Resurrect Unit - 战斗召唤法术(复活)
4. Shrine of Smiting - 神话单位
5. Angelic Transformation - 主要种族改造(变成天使)

**Supremacy (秩序+2)**:
1. Monument of Supremacy - 城市建筑
2. Condemn Army - 敌军法术(施加Condemned状态！)
3. Exemplar - 单位
4. Anthem of Victory - 增益法术
5. Supreme Magic - 单位附魔(赋予Zeal！)

**The Archon (秩序+2)**:
1. Holy Aura - 单位附魔(Shield, Shock, Skirmisher, Polearm, Fighter)
2. Celestial Guardians - 友军法术
3. Ascended Rebirth - 增益法术(复活)
4. Pure Soul - 种族改造
5. Summon Astra - 召唤神话单位

**Prosperity (秩序+1, 自然+1)**:
1. Grand Protection - 增益法术
2. Blessed Armors - 单位附魔(Shield, Polearm, Shock, Fighter, Skirmisher)
3. Staves of Grace - 单位附魔
4. Garden of Affluence - 城市建筑
5. Summon Prosperity Dragon - 召唤神话单位
 
我发现了几个有趣的协同点。Supremacy魔典特别引人注目，因为它提供了施加Condemned状态的能力，并且还有赋予Zeal的单位附魔。这与我之前的选择非常匹配，尤其是在The Inquisition和The Cleansing Flame的选择上。这些协同可能会极大地增强我的战略优势。

下一步，我将选择Sanctuary魔典，专注于治疗和防御增益。这个魔典将补充我之前的攻击性选择，为我的战略增添必要的防御能力。通过解锁Sanctuary，我还可以获得秩序+12的属性加成，并推进我解锁四级魔典的计划。

Supremacy魔典成为我的终极选择，因为它提供独特的Zeal和Condemned机制。我正在考虑是否能在获得7本魔典后，进一步解锁五级魔典。目前五级魔典的解锁要求似乎需要特定的亲和力点数。
-
太完美了！The God Emperor五级魔典与我的构建完美契合！

**The God Emperor (秩序+2)**:
1. Exalted Champion - 增益法术(伤害+100%，防御+5，抗性+5，状态保护+5)
2. Divine Protection - 友军法术(赋予Resurgence)
3. Wrath of the Emperor - 敌军法术(施加Condemned状态！)
4. Mass Revive - 战斗召唤法术(复活所有有Faithful或Zeal的死亡单位！)

关键协同：
1. **Wrath of the Emperor**: 施加Condemned状态，与Zealot、The Inquisition、The Cleansing Flame、Supremacy完美协同！
2. **Mass Revive**: 复活所有有Faithful或Zeal的单位，与Zeal魔典完美协同！
3. 与所有之前的秩序魔典协同！

这简直是完美的五级魔典！

现在我需要确认解锁条件：
- 解锁五级魔典需要：已解锁8本魔典，且相关Affinity >= 8
- 目前已解锁魔典：7本
- 秩序Affinity：+14

我还需要解锁1本魔典，才能解锁The God Emperor。

我可以解锁任何四级魔典或三级魔典，因为我已经满足了条件。

让我考虑一本四级魔典，作为第八本魔典：
- The Archon: 秩序+2，单位附魔(Shield, Shock, Skirmisher, Polearm, Fighter)


- Exaltation: 秩序+2，主要种族改造(天使变身)
- Prosperity: 秩序+1, 自然+1，单位附魔

我正在评估最佳选择。Exaltation提供了天使变身，可以彻底改变种族特性。Prosperity则增加了自然亲和力。考虑到我强大的治疗和增益能力，Exaltation看起来更具吸引力。

我选择了Exaltation作为第八本魔典。解锁后，我将获得秩序+16的属性加成，并解锁9本魔典。The God Emperor成为我的终极魔典，完美契合神圣秩序与狂热的主题。这个魔典路径体现了信仰力量和神权统治的核心理念。

我将开始整理完整的魔典选择路径，重点关注每个魔典的关键技能。Zeal魔典的Condemnation和Summon Zealot将为我的神圣狂热之路奠定基础。

关键技能包括精神伤害、单位增益和道德提升。

接下来，我需要详细统计所有解锁的技能，分析它们在伤害、召唤、增益和减益等方面的作用。我将系统地梳理每个技能的类型和影响，确保全面把握魔典的战略价值。

目前，我将重点收集和分类这些技能，为后续的战略制定做准备。
根据技能规则，我需要选择第7本和第8本魔典，然后才能解锁五级魔典。让我继续构建最优路径。
好的，我已经获得了Sanctuary和Exaltation的详细信息。现在让我整理完整的魔典构建路径和技能统计。

## 完整的魔典选择路径

1. **Zeal** (秩序+2) - 起始魔典
2. **Discipline** (物质+1, 秩序+1)
3. **The Inquisition** (秩序+2)
4. **The Beacon** (秩序+2)
5. **The Cleansing Flame** (秩序+1, 混沌+1)
6. **Supremacy** (秩序+2)
7. **Sanctuary** (秩序+2)
8. **Exaltation** (秩序+2)
9. **The God Emperor** (秩序+2) - 五级魔典

总计Affinity：
- 秩序：+2(种族) +2(Zeal) +1(Discipline) +2(The Inquisition) +2(The Beacon) +1(The Cleansing Flame) +2(Supremacy) +2(Sanctuary) +2(Exaltation) +2(The God Emperor) = +18
- 物质：+1(Discipline)
- 暗影：+1(种族)
- 自然：+1(种族)
- 混沌：+1(The Cleansing Flame)

现在我需要统计所有技能，按照技能说明中的分类方法。

让我开始统计：

## Unit Enchantment

### Zeal
- **Legion of Zeal**: Shield Unit, Polearm Unit, Fighter Unit, Ranged Unit, Shock Unit, Skirmisher Unit

### Discipline
- **Empowered Strikes**: Shield Unit, Polearm Unit, Fighter Unit, Skirmisher Unit


- **Focus Aim**: Ranged Unit, Support Unit, Battle Mage Unit

### The Inquisition
- **Inquisitor's Mark**: Ranged Unit, Skirmisher Unit

### The Beacon
- **Mighty Meek**: Tier I Units, Tier II Units

### The Cleansing Flame
- **Pureflame Staves**: (所有有魔法攻击的单位)
- **Flame Blessed Champions**: Shield Unit, Shock Unit, Polearm Unit, Fighter Unit

### Supremacy
- **Supreme Magic**: Support Unit, Battle Mage Unit

### Sanctuary
- **Keeper's Mark**: Shield Unit

我注意到单位附魔涵盖了多种类型，从盾牌单位到法师单位，显示出全面的增强策略。这些技能为不同单位类型提供了独特的战斗优势。

### Exaltation
- 无单位附魔

### The God Emperor
- 无单位附魔

单位类型呈现出复杂的分层，需要进一步深入分析单位类型的实际影响范围和战略价值。

### 伤害法术策略
精神伤害法术覆盖多个维度，从单体到范围攻击，展现了战术灵活性。谴责机制成为关键战略元素，通过不同魔典的多重法术实现。

### 召唤单位多样性
召唤单位从狂热者到光明使者，再到净化火焰骑士，构建了一个多元且富有战略深度的战斗单位体系。每个召唤单位都携带着独特的战斗特征。

### 增益法术核心
通过吟唱、英勇姿态等手段，增强单位战斗力。专注瞄准和增益效果形成了一个动态的战术网络，为单位提供关键的战斗优势。

### 治疗与康复
净化咒语和治愈尖塔提供医疗支持，救赎和复活能力确保单位在战场上保持持续作战能力。圣所魔典尤其擅长维护单位生存。

### 减益法术策略
谴责军队、皇帝之怒等法术有效削弱敌方战力。罪恶负担和大规模谴责等手段，通过精神伤害和状态削弱，显著降低敌人战斗潜能。

### 种族转变
内在掌控、美德精神等小种族转变提供微妙但关键的种族属性调整。涂抹人民和纯洁灵魂等法术进一步优化种族特征，增强整体战略适应性。

### 大种族转变
天使转变代表一个重大且深远的种族进化，显著改变种族本质和能力。
让我为你整理完整的最佳魔典BUILD路径。

# 神圣秩序狂热流

## 魔典选择路径

### 1. Zeal (狂热) [秩序+4]
**起始魔典**
- Condemnation (伤害/减益法术) - 15精神伤害，施加Condemned状态
- Summon Zealot (召唤法术) - 召唤对Condemned敌人有优势的狂热者
- Legion of Zeal (单位附魔) - 给近战和远程单位提供Zeal特性
- Inspiring Chant (增益法术) - 提高士气，对有Zeal的单位额外强化

### 2. Discipline (纪律) [秩序+5, 物质+1]
**物质与秩序协同，强化近战**
- Empowered Strikes (单位附魔) - 近战单位伤害+1，第三击有60%眩晕
- Focus Aim (单位附魔) - 远程单位获得必中攻击能力
- Mantra of Purification (治疗法术) - 治疗15临时生命，驱散2个负面状态
- Inner Mastery (种族改造) - 状态抗性+1，治疗接收+20%

### 3. The Inquisition (审判庭) [秩序+7]
**完美协同，强化Condemned机制**
- Mass Condemnation (伤害/减益法术) - 范围施加Condemned状态
- Inquisitor's Mark (单位附魔) - 远程和散兵攻击施加Condemned和Weakened
- Inquisitor (单位) - 可施加Condemned和Stunned的散兵单位
- Summon Lightbringer (召唤法术) - 召唤可转化敌人的光明使者

### 4. The Beacon (灯塔) [秩序+9]
**全面增益，强化所有低级单位**
- Mighty Meek (单位附魔) - 一二级单位获得Faithful、状态抗性+2、精神伤害加成
- Conjure Divine Beacon (战斗召唤) - 召唤治疗和士气增益的灯塔
- Summon Blessed Soul (召唤法术) - 召唤可谴责敌人的盾牌单位
- Chaplain (单位) - 强化盟友的支援单位

### 5. The Cleansing Flame (净化之焰) [秩序+10, 混沌+1]
**核心协同，完美融合Zeal与Condemned**
- Zealous Ignition (增益法术) - 赋予Zeal或强化已有Zeal，对敌人施加Condemned
- Pureflame Staves (单位附魔) - 魔法攻击施加Condemned并创造净化火焰
- Flame Blessed Champions (单位附魔) - 近战攻击施加Burning并创造净化火焰
- Pyre Templar (单位) - 长柄单位，攻击施加Burning

### 6. Supremacy (至高) [秩序+12]
**终极协同，双重核心机制**
- Supreme Magic (单位附魔) - 支援和法师单位获得Zeal，击杀敌人引发爆炸
- Condemn Army (敌军法术) - 对敌军施加Condemned状态
- Anthem of Victory (增益法术) - 全体盟友获得3强化和+15士气
- Exemplar (单位) - 飞行盾牌单位，提高士气

### 7. Sanctuary (圣所) [秩序+14]
**治疗与防御，完善构建**
- Keeper's Mark (单位附魔) - 近战单位获得Faithful，首次受致命伤害时存活
- Salvation (增益法术) - 完全治疗并驱散负面状态
- Anointed People (种族改造) - 状态抗性+3，精神抗性+3
- Summon Light Spirit (召唤法术) - 召唤强力治疗支援单位

### 8. Exaltation (升华) [秩序+16]
**天使变身，神话力量**
- Angelic Transformation (主要种族改造) - 种族变成天使，获得飞行、Faithful
- Shrine of Smiting (神话单位) - 力量随Faithful单位数量增长
- Resurrect Unit (战斗召唤) - 复活死亡单位
- Ascended Warriors (友军法术) - 全体非英雄单位提升1阶

### 9. The God Emperor (神皇) [秩序+18] ⭐五级魔典
**终极形态，神权统治**
- Mass Revive (战斗召唤) - 复活所有有Faithful或Zeal的死亡单位！
- Wrath of the Emperor (敌军法术) - 施加Condemned状态，敌军领土额外+50%伤害
- Exalted Champion (增益法术) - 伤害+100%，防御和抗性+5
- Divine Protection (友军法术) - 全体获得Resurgence(复苏)

---

## 技能统计结果

### 单位附魔统计
**近战单位增强**
- Zeal特性(精神伤害) ✅
- 近战伤害+1，第三击60%眩晕 ✅
- 一二级单位：状态抗性+2，精神伤害加成 ✅
- 近战攻击创造净化火焰并施加Burning ✅
- 首次受致命伤害存活(Steadfast) ✅
- Faithful特性(减少维护费) ✅

**远程单位增强**
- Zeal特性 ✅
- 必中攻击能力 ✅
- 攻击施加Condemned和Weakened ✅
- 一二级单位全面增益 ✅

**法师/支援单位增强**
- 必中攻击能力 ✅
- Zeal特性 ✅
- 击杀引发精神爆炸 ✅

**全体单位增强**
- 状态抗性+1~+6 ✅
- 治疗接收+20% ✅
- Faithful特性(减少维护费) ✅
- 精神抗性+3 ✅
- 首次受致命伤害不死 ✅

### 核心法术机制
**Condemned状态施加** (6个来源)
1. Condemnation
2. Mass Condemnation
3. Inquisitor's Mark
4. Zealous Ignition
5. Pureflame Staves
6. Condemn Army
7. Wrath of the Emperor

**Zeal特性赋予** (3个来源)
1. Legion of Zeal
2. Zealous Ignition
3. Supreme Magic

**复活/治疗机制**
- 瞬间完全治疗
- 复活死亡单位
- 复活所有Faithful/Zeal单位
- 持续治疗增益

### 种族改造
**小种族改造**
- 状态抗性+1，治疗接收+20%
- 低血量时防御和抗性+1，忽略50%伤亡
- 状态抗性+3，精神抗性+3
- 每回合自动驱散1个负面状态

**大种族改造**
- 天使变身：飞行、Faithful、天界单位类型

### 战斗单位
- 狂热者(对Condemned敌人优势)
- 武僧(连击治疗)
- 审判官(施加Condemned和Stunned)
- 光明使者(转化敌人)
- 圣骑士(治疗和神圣打击)
- 火焰圣骑士(施加Burning)
- 圣者(提高士气)
- 光灵(强力治疗)
- 神话圣击神殿(随Faithful数量增强)
- 天使(神话飞行单位)

---

## BUILD名称：神圣秩序狂热流

**核心机制**：
1. **Zeal协同** - 通过多个魔典赋予和强化Zeal特性，大幅增加精神伤害
2. **Condemned连击** - 7个来源施加Condemned状态，与Zealot和审判官完美协同
3. **Faithful经济** - 减少维护费，与神话单位和复活机制协同
4. **不死军团** - 首次受致命伤害存活 + 复活所有Faithful/Zeal单位的终极组合

**游戏风格**：高士气、高精神伤害、复活不死、神权统治

**关键优势**：
- 完美的魔典协同(每个魔典都与之前的选择协同)
- 强大的单位附魔重叠(最大化效益)
- 多重复活机制(容错率极高)
- Condemned状态链(控制与伤害并重)
- 天使种族变身(后期神话力量)