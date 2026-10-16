# 上线与迁移一致性 · release-migration-parity

[English](README.md) | [技能正文](SKILL.md) | [维护者：kevin-12-ou](https://github.com/kevin-12-ou)

本地验收没问题，上线后弹窗样式却变了，旧新版数据不互通；或者迁移到小程序时悄悄漏掉原有功能。这个技能围绕已验收体验做对照。

这是给 AI 编程助手读取的 **Agent Skill（指令与参考材料）**。包内不包含后台服务、安装执行钩子或模型；Python 脚本仅用于开发时检查包结构；安装后由助手按需读取，实际操作仍受宿主工具权限和用户授权约束。

## 能帮你做什么

- 以用户已验收的实际源码和工作区状态为基准。
- 查清路由、CSS、Portal、身份、存储和平台 API 的适配点。
- 跨平台先跑通一条包含保存和重开的完整路径。
- 绑定最终源码、构建、发布版本和回退位置，分别说明各层验证。

## 安装

需要 Git 和支持 Agent Skills 的 AI 助手。使用下面的 Skills CLI 命令还需要 Node.js/npm；CLI 是外部安装工具，运行前请自行审阅。安装本包不需要 API Key、数据库或付费账号，所用 AI 助手本身可能收费。

```sh
npx skills add kevin-12-ou/release-migration-parity --skill release-migration-parity
```

CLI 会让你选择助手和安装范围。建议先装到测试项目中检查效果。以下是 Codex 的项目级安装示例，不带 `--global`：

```sh
npx skills add kevin-12-ou/release-migration-parity --skill release-migration-parity --agent codex --copy
```

手动安装：下载本仓库，将完整目录保留为 `release-migration-parity`，放到助手支持的技能目录中，例如 `.agents/skills/release-migration-parity/`。保留参考文件，不能只复制 README；以助手文档为准。

## 直接这样问

```text
Use $release-migration-parity. Publish the accepted experimental version while preserving its dialogs, theme, data semantics, and existing entry points. Verify the actual deployed flow and provide a rollback reference.
```

```text
用 $release-migration-parity。把已验收实验版上线，保留弹窗、主题、数据语义和既有入口。验证实际线上流程，并说明回退位置。
```

```text
Use $release-migration-parity. Port this working web app to a WeChat Mini Program. Preserve the web version, compare platform constraints, and verify one edit-save-reopen path before expanding.
```

```text
用 $release-migration-parity。把这个可用网页迁到微信小程序，保留网页原版，核对平台差异，先验证一条编辑、保存、重开的完整路径。
```

显式点名更清楚；自动选择由模型和客户端决定，不保证每次命中。本包采用通用 [Agent Skills 格式](https://agentskills.io/specification)，在 Codex、Claude Code 等支持该格式的工具中可供读取；未宣称所有客户端的实际行为均已测试。技能正文以中文为主。

## 边界与数据

不承诺零 bug，也不要求跨平台源码相同。编译通过、HTTP 可访问、浏览器交互和真机行为是不同层次的证据。

包内没有凭据或个人项目记录。是否读取项目、写文件、联网或执行命令，取决于任务和助手权限；公开技能本身不会提供隔离或强制拦截。

## 更新、停用与贡献

通过 Skills CLI 安装时可用 `npx skills check` 检查更新、`npx skills update` 更新已安装技能；更新前审阅差异。停用可在助手设置中禁用，或移走安装的技能目录；先备份自己新增的内容。

问题和改进建议请提交到 [Issues](https://github.com/kevin-12-ou/release-migration-parity/issues)，提供去除隐私的最小例子。维护说明见 [CONTRIBUTING.md](CONTRIBUTING.md)，公开包检查见 [VALIDATION.md](VALIDATION.md)。

## 同一维护者的其他技能

- [从概念到行动教练](https://github.com/kevin-12-ou/concept-to-action-coach) — 听过术语，也能复述定义，但仍不知道什么时候需要它、该怎么开始。这个技能把解释接到一个能完成、能验收的小行动上。
- [成功方案复用与经验库](https://github.com/kevin-12-ou/dont-repeat-yourself) — 脚本已经跑通、坑也踩过了，换个项目却又从头找。这个技能把成功结果整理成可搜索的小配方，并在下次使用前核验适用条件。
- [开源项目安装评估与上手指南](https://github.com/kevin-12-ou/deploy-onboarding-guide) — 只说“部署好了”不够。用户还需要知道它具体干什么、需不需要 API 或付费账号、会改哪里，以及第一次怎么用。

由 [kevin-12-ou](https://github.com/kevin-12-ou) 维护，整理自个人 AI 辅助工作流。采用 [MIT](LICENSE) 许可；来源说明见 [NOTICE.md](NOTICE.md)。
