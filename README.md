## 介绍
该项目是一个MCP+SKills的AI试验项目。主要想看看AI可否对于策略游戏进行指导和辅助。奇迹时代4 中的魔典是游戏中非常重要的一个元素，玩家可以通过魔典来提升自己的属性，从而获得更强的战斗力。魔典的选择和技能的选择，对于玩家来说是一个非常重要的决策。AI可以帮助玩家进行魔典的选择和技能的选择。有任何想法和建议，欢迎提issue。

相关魔典数据来源:
https://aow4.paradoxwikis.com/Tomes

## 安装
- 使用UV
```
$ git clone <repo>
$ cd aow4_mcp
$ uv sync
```

- 配置redis server

直接使用docker创建redis server
```
$ docker run -d -p 6379:6379 redis
```

## Agent Skills 安装
- aow4_tome 为Agent Skills插件，按使用的Agent工具，安装至对应的目录

## MCP server 配置 

```json
{
  "mcpServers": {
    "AOW4_Tomes": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/aow4_mcp",
        "run",
        "aow4_mcp.py"
      ],
      "disabled": false,
      "timeout": 60
    }
  }
}
```

## 使用

在Agent工具中，配置MCP server 及 Skills

```
@ 奇迹时代4
种族点数： 秩序+2；暗影+1;  物质+1
起始魔典：纪律
如何构建最佳魔典BUILD

@AI: 用户想知道如何构建最佳魔典BUILD。

根据available_skills中有一个aow4_tome技能，描述是：
"当询问奇迹时代4(AOW4)魔典(Tome)信息，或者询问相关魔典问题，魔典出发什么技能；提供初始魔典后，后续魔典如何选择；最佳的魔典选择路径，最优的魔典选择路径"
...
```
具体查看[sample1](https://github.com/kenzhu/aow4_mcp/main/samples/test1.md)

## CLI
- list-tomes: 列出所有魔典
```
$ uv run aow4-tome list-tomes
                  AOW4 Tomes                  
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┓
┃ Category ┃ Name                     ┃ Tier ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━┩
│ Astral   │ Evocation                │  I   │
│          │ Warding                  │  I   │
│          │ Scrying                  │  II  │
│          │ Summoning                │  II  │
│          │ Amplification            │ III  │
│          │ Teleportation            │ III  │
│          │ Astral Convergence       │  IV  │
│          │ The Astral Mirror        │  IV  │
│          │ The Arch Mage            │  V   │
```

- show tome: 显示魔典的详细信息
```
$ uv run aow4-tome show --json "Evocation"
{
  "name": "Evocation",
  "tier": 1,
  "category": "Astral",
  "summary": "Tier I - Grants excellent and cheap attack spells to any aspiring wizard.",
  "tome_skills": [
    {
      "name": "Lightning Focus",
      "tier": 1,
      "type": "Unit enchantment",
      "effects": "Makes base Magic attacks of enchanted units: Deal +2 Lightning Damage. Gains base 30% chance of
inflicting Electrified, a damage-over-time effect. Effects are increased for non-repeating attacks.\nAffected 
unit types: Support Unit Battle Mage Unit"
    },
  ... ]
...
}
```

## 主要文件 

- **aow4_mcp.py**: MCP server
- **src/cli.py**: Typer CLI interface
- **src/config.py**: Configuration settings
