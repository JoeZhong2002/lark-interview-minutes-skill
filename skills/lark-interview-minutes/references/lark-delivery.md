# 飞书交付

## 创建文档

优先用 XML，保留清晰的标题、列表、表格和 callout：

```bash
lark-cli docs +create \
  --api-version v2 \
  --as user \
  --content @minutes.xml
```

`minutes.xml` 必须是当前工作目录下的相对路径。

## 内容映射

- 文档标题：`<title>`。
- 一级至三级章节：`<h1>`、`<h2>`、`<h3>`。
- 结论与动作：`<ul>` / `<ol>`。
- 结构化比较：`<table>`，表头用 `light-gray`。
- 免责声明和待确认：`<callout>`。
- Mermaid 图：`<whiteboard type="mermaid">...</whiteboard>`。
- 复杂图：按 `lark-doc` 和 `design-lark-chart` 创建可编辑画板。

## 验收命令

```bash
lark-cli docs +fetch \
  --api-version v2 \
  --doc <DOCUMENT_ID> \
  --scope outline --max-depth 3 --detail with-ids \
  --as user

lark-cli whiteboard +query \
  --whiteboard-token <TOKEN> \
  --output_as code --as user

lark-cli whiteboard +query \
  --whiteboard-token <TOKEN> \
  --output_as image --output ./preview.png --overwrite \
  --as user
```

检查：

- 章节是否齐全且顺序正确。
- 表格是否有完整表头和行数据。
- 画板是否能回读 Mermaid/PlantUML 代码。
- 真实预览图是否存在文字裁切、节点重叠、画布过高或信息缺失。
- 最终链接是否属于用户可访问的飞书组织域名。

## 最终回复

简要说明：

- 文档已创建。
- 添加了哪些图示。
- 已完成目录、源码和视觉回读。
- 提供可点击的飞书文档 URL。
