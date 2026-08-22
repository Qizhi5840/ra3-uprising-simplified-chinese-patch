from pyBIG import refpack
import sys

def decompress_ea_file(input_file, output_file):
    print(f"正在读取 RefPack 压缩文件: {input_file}")
    with open(input_file, 'rb') as f:
        compressed_data = f.read()
    
    # 检查是否有标准的 RefPack 文件头
    if not refpack.has_refpack_header(compressed_data):
        print("警告: 该文件似乎不包含标准的 RefPack 头部，但我们仍会尝试强行解压...")
    
    try:
        # 调用 pyBIG 内置的 refpack 解压
        decompressed_data = refpack.decompress(compressed_data)
        
        with open(output_file, 'wb') as f:
            f.write(decompressed_data)
        print(f"解压成功！已保存为标准的 CSF 明文文件: {output_file}")
        
    except Exception as e:
        print(f"解压失败，报错信息: {e}")

if __name__ == "__main__":
    # 使用示例:
    # python decode_refpack.py compressed_english.csf decrypted_english.csf
    if len(sys.argv) >= 3:
        decompress_ea_file(sys.argv[1], sys.argv[2])
    else:
        print("用法: python decode_refpack.py <输入乱码csf> <输出正常csf>")