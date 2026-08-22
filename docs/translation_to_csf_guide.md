# 从翻译文本到游戏语言包：构建指南

>本指南旨在帮助有需要的朋友，将本仓库中的翻译文本（`ra3_uprising_cn_diff.txt`）转换成游戏可识别的 `.csf` 语言文件，以便进行二次修改或整合进自己的项目中。

---

## 准备工作

你需要准备以下内容：

1. **本仓库的翻译文本**：即 `text/ra3_uprising_cn_diff.txt` 文件。
2. **一个能将 `.txt` 转换为 `.ini` 的脚本**：我提供的转换脚本（位于 `tools/` 目录下），用于将 `diff.txt` 整理成标准的 `.ini` 文件格式。
3. **`Ra2CsfToolsGUI` 工具**：一个强大的 CSF 与 INI 互转工具。
   - **下载地址**：[https://github.com/SadPencil/Ra2CsfToolsGUI/releases/](https://github.com/SadPencil/Ra2CsfToolsGUI/releases/)

---

## 核心步骤：从 `.txt` 到 `.csf`

整个过程分为两步：

### 第一步：将 `.txt` 转换为 `.ini`

> 开始之前，请先下载Python。

1. 将 `ra3_uprising_cn_diff.txt` 和转换脚本（[to_ini.py](scripts/to_ini.py)）放在同一个文件夹。
2. 运行脚本。
3. 脚本运行后会生成一个 `.ini` 文件。

---

### 第二步：使用 `Ra2CsfToolsGUI` 将 `.ini` 转换为 `.csf`

1. 用`Ra2CsfToolsGUI` 工具打开刚才的`.ini`文件。
2. 点击**保存为 .CSF 文件...”** ，指定你想要生成的 `.csf` 文件的保存位置，并将文件名改为`game strings.csf`。

---

## 将生成的 `.csf` 文件用于游戏

生成新的csf文件后，你就可以按照 [安装指南](install_guide.md) 中的说明，将其封装进big文件，用它替换游戏 `data` 文件夹中的原文件了。