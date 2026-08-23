# -*- coding: utf-8 -*-
"""
把 merged_v2.txt 转换为 222.ini（SadPencil Ra2CsfFile.Ini 格式）

merged_v2.txt 格式（fix_merged.py 产出，每个 key 一个块，块间空行）：
  [KEY]
  Value=<en_value>
  ValueLine2=<en_v2>
  ...
  Value=<zh_value>          <- 第二个 Value= 开始就是 ZH 块
  ValueLine2=<zh_v2>
  ...
  <空行>

本脚本只取每个 [KEY] 的 ZH 块（第二个 Value= 及其后的 ValueLineN=），原样写入 222.ini。

输出 222.ini 格式：
  [SadPencil.Ra2CsfFile.Ini]
  IniVersion=2
  CsfVersion=3
  CsfLang=8

  [KEY]
  Value=<zh_value>
  ValueLine2=<zh_v2>
  ValueLine3=<zh_v3>
  ...

  [KEY2]
  ...

直接双击运行，无参数
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "diff.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "gamestrings.ini")

KEY_RE = re.compile(r'^\[(.+)\]\s*$')
VALUE_RE = re.compile(r'^Value=(.*)$')
VALUELINE_RE = re.compile(r'^ValueLine(\d+)=(.*)$')


def flush(out_lines, key, zh_lines):
    """把一个 [key] 的 ZH 块写入 out_lines。zh_lines 是 [(label, value), ...]，
    label 是 "Value" 或 "ValueLine2" 等。"""
    if not zh_lines:
        return 0
    out_lines.append(f'[{key}]\n')
    for label, val in zh_lines:
        out_lines.append(f'{label}={val}\n')
    out_lines.append('\n')
    return 1


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"错误：找不到 {INPUT_FILE}")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8-sig') as fin:
        lines = fin.readlines()

    out_lines = []
    # 头部
    out_lines.append('[SadPencil.Ra2CsfFile.Ini]\n')
    out_lines.append('IniVersion=2\n')
    out_lines.append('CsfVersion=3\n')
    out_lines.append('CsfLang=8\n')
    out_lines.append('\n')

    count = 0
    n = len(lines)
    i = 0

    current_key = None
    value_count = 0  # 本块内见到的 Value= 次数：1=EN 的 Value，2=ZH 的 Value
    zh_lines = []  # 本块的 ZH 行：(label, value)

    while i < n:
        raw = lines[i]
        line = raw.rstrip('\r\n')  # 保留前后空白
        s = line.strip()  # 仅用于识别 section 头和空行

        m = KEY_RE.match(s)
        if m:
            # 刷掉上一个 key
            if current_key is not None:
                count += flush(out_lines, current_key, zh_lines)
            # 开始新块
            current_key = m.group(1)
            value_count = 0
            zh_lines = []
            i += 1
            continue

        # 还没进入任何 [key] 就先跳过
        if current_key is None:
            i += 1
            continue

        # 空行 = 本块结束
        if s == "":
            if current_key is not None:
                count += flush(out_lines, current_key, zh_lines)
            current_key = None
            value_count = 0
            zh_lines = []
            i += 1
            continue

        # Value=
        mv = VALUE_RE.match(line)
        if mv:
            value_count += 1
            if value_count >= 2:
                # 第二个 Value= 开始就是 ZH 块
                zh_lines.append(("Value", mv.group(1)))
            # 否则是 EN 的 Value=，跳过
            i += 1
            continue

        # ValueLineN=
        mvl = VALUELINE_RE.match(line)
        if mvl:
            if value_count >= 2:
                # ZH 块的 ValueLineN=
                zh_lines.append((f"ValueLine{mvl.group(1)}", mvl.group(2)))
            # 否则是 EN 块的 ValueLineN=，跳过
            i += 1
            continue

        # 其他行（理论上不会出现）跳过
        i += 1

    # 文件末尾若没空行收尾，刷掉最后一个 key
    if current_key is not None:
        count += flush(out_lines, current_key, zh_lines)

    with open(OUTPUT_FILE, 'w', encoding='utf-8-sig') as fout:
        fout.writelines(out_lines)

    print(f"完成！共写入 {count} 个条目到 {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
