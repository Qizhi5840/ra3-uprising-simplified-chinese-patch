"""
把 merged.txt 转换为 222.ini（SadPencil Ra2CsfFile.Ini 格式）
格式：
  [SadPencil.Ra2CsfFile.Ini]
  IniVersion=2
  CsfVersion=3
  CsfLang=8

  [KEY]
  Value=中文翻译

  ...
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 翻译比对文件路径，可按需修改文件名
INPUT_FILE = os.path.join(BASE_DIR, "diff.txt")
# 输出ini文件路径，可按需修改文件名
OUTPUT_FILE = os.path.join(BASE_DIR, "gamestrings.ini")

KEY_RE = re.compile(r'^\[(.+)\]\s*$')


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

    while i < n:
        line = lines[i]
        stripped = line.rstrip('\r\n')
        m = KEY_RE.match(stripped)
        if m:
            key = m.group(1)
            zh = ''
            if i + 2 < n:
                zh = lines[i + 2].rstrip('\r\n')

            out_lines.append(f'[{key}]\n')
            out_lines.append(f'Value={zh}\n')
            out_lines.append('\n')
            count += 1
        i += 1

    with open(OUTPUT_FILE, 'w', encoding='utf-8-sig') as fout:
        fout.writelines(out_lines)

    print(f"完成！共写入 {count} 个条目到{OUTPUT_FILE}")


if __name__ == '__main__':
    main()
