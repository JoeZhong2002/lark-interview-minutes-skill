# 依赖安装

## 检查对象

需要同时具备：

1. `lark-cli` 可执行程序。
2. `larksuite/cli` 提供的 `lark-shared`、`lark-doc`、`lark-whiteboard` 等官方 Skills。
3. `fuxiaoai/lark-chart-skill` 提供的 `design-lark-chart`。

## 安装协议

发现缺失后先告诉用户缺少什么，并请求安装许可。只有用户同意后才执行。

### 官方飞书 CLI 与 Skills

优先遵循仓库最新说明：

```bash
npx @larksuite/cli@latest install
```

如果当前 Agent 需要将 Skills 安装到 Codex，使用 `skill-installer` 从 `larksuite/cli` 的 `skills/lark-*` 路径安装。至少确保 `lark-shared`、`lark-doc`、`lark-whiteboard` 存在。

### 图表 Skill

使用 `skill-installer` 安装：

- Repo：`fuxiaoai/lark-chart-skill`
- Path：`skills/design-lark-chart`

### 安装后

1. 重新运行 `scripts/check_dependencies.py`。
2. 提醒用户重启 Codex 以加载新 Skills。
3. 重新进入本 Skill，并从依赖检查步骤继续。

## 配置与授权

- 未配置：`lark-cli config init --new`。
- 用户身份授权：`lark-cli auth login --domain docs,drive --no-wait --json`。
- 必须按 `lark-shared` 规则同时展示原始 URL 和二维码。
- 用户确认后，由 Agent 执行 `--device-code` 回收授权。
- 不输出 app secret 或 access token。
