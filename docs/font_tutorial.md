# 字体优化与自定义教程

> 本文档旨在指导玩家如何为《红色警戒3》及《起义时刻》更换自定义中文字体。


## 目录

- [一、为什么直接换字体经常会失败？](#一为什么直接换字体经常会失败)
- [二、简中包方案：chineseS.big（基础替换，本项目采用）](#二简中包方案chinesesbig基础替换本项目采用)
- [三、繁中包方案：chineseT.big（完美字重高级玩法）](#三繁中包方案chinesetbig完美字重进阶玩法)
- [四、推荐工具](#四推荐工具)

***

## 一、为什么直接换字体经常会失败？

在红警3中，加载字体并非简单的“替换同名文件”就能生效。目前的两种中文包，其字体校验机制截然不同：

1. **按文件名读取（ **`English.big/ChineseS.big`** **）**：引擎只认 `red alert.ttf` 这个名字和路径，不关心字体内部数据。
2. **按字体属性读取（**`chineseT.big`** **）**：引擎不仅认文件名，还会读取 TTF 字体内部 `name` 表中的属性名（必须叫“文鼎新中黑”）。

只要用错了对应包的修改方法，游戏内的文字就会直接变成一堆下划线。

***

## 二、本项目 Release 方案：英文包/简中包“零配置”替换（推荐）

这是最简单、合规的替换方式，不需要修改字体的任何内部数据。本项目的Release包采用此方案。由于本项目提供的 Release 语言包（.big）中**已经预先建好了正确的路径格式并内置了主字体与扩展字体**，你可以直接对本项目的 .big 文件进行修改。

### 2.1 替换步骤

1. 准备好你想用的 TTF 字体文件。
2. 将其重命名为 `red alert.ttf`（中间有一个空格）。
3. 使用 BIG 封包工具（如 **FinalBIG**），打开 `ChineseS.big`或`English.big`。
4. 将你改好名的 `red alert.ttf` 导入包内，路径写 `data\fonts\red alert.ttf`，替换原文件。
5. 保存包文件，放入游戏目录替换即可。

***

## 三、繁体中文包方案：chineseT.big

`chineseT.big` 并非只能用来显示繁体！
通过将简体中文的文本（`gamestrings.csf`）与 修改过属性的简体中文字体一同打包进 `chineseT.big`，游戏会调用官方原生的字体渲染通道。其最大优势是：**字重渲染极其完美**（该用粗体的地方是粗体，常规体绝对是常规体），效果远胜于 `chineseS.big` 的粗暴调用。

如果你追求极致的 UI 观感，可以尝试以下方法：

> 修改字体内部属性仅供玩家个人在本地研究与优化体验，请勿将修改后的属性伪装字体公开发布，以免违反开源/商业字体的授权协议。

1. 准备好你想用的新字体，粗体字体改名为 `bhei01b.ttf`，常规字体改名为 `bhei00m.ttf`。
2. 下载并打开免费字体编辑器 **FontForge**。
3. 在 FontForge 中打开要修改的字体文件。
4. 点击 Element - Font Info。
5. 在PS Element选项页面中，按以下表格替换字段：

   | 字段 | 粗体 (bhei01b) | 常规 (bhei00m) |
   | :--- | :--- | :--- |
   | Fontname | `LinGothic-Bold` | `NewGothic-Medium` |
   | Family Name | `AR Heiti Bold B5` | `AR Heiti2 Medium B5` |
   | Name For Humans | `AR Heiti Bold B5` | `AR Heiti2 Medium B5` |
   | Weight | `Bold` | `Book` |
   | Version | `2.60` | `2.60` |
   | sfnt Revision | `5` | `5` |
   | Copyright | `(c) Copyright 1994-2004, Arphic Technology Co., Ltd.` | `(c) Copyright 1994-2004, Arphic Technology Co., Ltd.` |

   > 建议删除原字体的所有 Name 记录，仅保留上述替换后的字段，避免属性冲突。

6. 切换到TTF Names选项卡，按以下表格替换字段：

   | 语言 / 字段 | 粗体 (bhei01b) | 常规 (bhei00m) |
   | :--- | :--- | :--- |
   | Chinese (PRC) / Family | `文鼎粗黑` | `文鼎新中黑` |
   | Chinese (PRC) / Styles (SubFamily) | `Regular` | `Regular` |
   | Chinese (PRC) / UniqueID | `文鼎粗黑` | — |
   | Chinese (PRC) / Fullname | `文鼎粗黑` | `文鼎新中黑` |
   | Chinese (PRC) / Version | `Version 2.60` | `Version 2.60` |
   | Chinese (PRC) / Trademark | `Arphic is a registered trademark of Arphic Technology Co., Ltd.` | `Arphic is a registered trademark of Arphic Technology Co., Ltd.` |
   | Chinese (PRC) / Copyright | `(c) Copyright 1994-2004, Arphic Technology Co., Ltd.` | `(c) Copyright 1994-2004, Arphic Technology Co., Ltd.` |
   | English (US) / Family | `AR Heiti Bold B5` | `AR Heiti2 Medium B5` |
   | English (US) / Styles (SubFamily) | `Regular` | `Regular` |
   | English (US) / UniqueID | `AR Heiti Bold B5` | `AR Heiti2 Medium B5` |
   | English (US) / Fullname | `AR Heiti Bold B5` | `AR Heiti2 Medium B5` |
   | English (US) / Version | `Version 2.60` | `Version 2.60` |
   | English (US) / Copyright | `(c) Copyright 1994-2004, Arphic Technology Co., Ltd.` | `(c) Copyright 1994-2004, Arphic Technology Co., Ltd.` |

   > 建议删除原字体的所有 TTF Names 记录，仅保留上述替换后的条目。

7. 导出生成新的 TTF 文件。
8. 使用 FinalBIG，打开 `chineseT.big` 。将`bhei01b.ttf`、`bhei00m.ttf`导入包内，路径分别写 `data\fonts\bhei01b.ttf`、`data\fonts\bhei00m.ttf`，替换原文件。

进入游戏后，引擎会误以为加载了官方的“文鼎新中黑”，但实际渲染出的是你注入的优质简体字体，且粗细分明。



***

## 六、推荐工具

- **FinalBIG**：用于解包和打包红警3的 `.big` 文件
	- 下载地址：[https://www.moddb.com/downloads/finalbigv2](https://www.moddb.com/downloads/finalbigv2)
- **FontForge**：用于进行第三章的开源跨平台字体编辑器。
	- 下载地址：[https://github.com/fontforge/fontforge/releases](https://github.com/fontforge/fontforge/releases)

