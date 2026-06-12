# Lark Interview Minutes Skill

一个面向 Codex 的飞书专家访谈纪要 Skill：把会议逐字稿和访谈框架整理成完整纪要，执行三轮原稿回读查漏，按需加入表格、流程图、Roadmap 或思维导图，并最终创建可共享的飞书云文档。

## 能做什么

- 按用户给定的访谈框架组织逐字稿，而不是只做泛化摘要。
- 三轮检查原稿，补齐遗漏信息，核对数字、口径、冲突和未回答项。
- 只在真正适合时使用表格、流程图、Roadmap、思维导图等可视化。
- 检查飞书 CLI、官方飞书 Skills 和图表 Skill 是否已安装。
- 使用飞书 CLI 创建云文档，并回读文档和画板完成验收。

## 安装

让 Codex 安装此仓库中的 Skill：

```text
请从 GitHub 仓库 JoeZhong2002/lark-interview-minutes-skill 安装
skills/lark-interview-minutes
```

也可以使用 Codex 的 `skill-installer`，仓库为 `JoeZhong2002/lark-interview-minutes-skill`，路径为 `skills/lark-interview-minutes`。

安装后重启 Codex，使新 Skill 生效。

## 依赖

本 Skill 会主动检查以下依赖，并在缺少时先征得用户同意再安装：

- [larksuite/cli](https://github.com/larksuite/lark-cli)：飞书 CLI 与官方飞书 Skills。
- [fuxiaoai/lark-chart-skill](https://github.com/fuxiaoai/lark-chart-skill)：复杂图表与飞书画板能力。
- Python 3：运行本地依赖检查脚本。

飞书账号仍需按 CLI 指引完成应用配置和 `docs,drive` 用户授权。

## 使用

向 Codex 提供逐字稿文件和访谈框架，例如：

```text
按照下面的访谈框架整理这份逐字稿，完成三轮回读查漏，
在适合的位置加入表格、流程图或 Roadmap，并输出飞书云文档。
```

Skill 会依次执行：依赖检查、材料解析、框架整理、三轮回读、可视化选择、飞书文档创建和交付验收。

## 隐私提示

会议逐字稿通常包含敏感信息。请确认当前飞书应用、云文档权限和组织共享范围符合你的数据管理要求。本仓库不包含任何真实访谈材料、账号密钥或访问令牌。

## 许可证

本项目使用 [Apache License 2.0](LICENSE)。外部依赖遵循各自仓库的许可证，本项目不打包或重新分发这些依赖。
