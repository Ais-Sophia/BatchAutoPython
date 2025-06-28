import os
import sys

def rename(prefix="file", digits=3):
    # 获取当前目录下所有文件（排除自身脚本）
    files = [f for f in os.listdir() if os.path.isfile(f) and f != __file__]
    files.sort(key=lambda x: os.path.getctime(x))  # 按创建时间排序（可替换为其他逻辑）
    
    max_digits = len(str(len(files)))        # 动态计算所需位数（至少3位）
    pad_digits = max(digits, max_digits)     # 保证最小位数为设定值（默认3）
    
    for idx, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]  # 保留原始扩展名
        new_name = f"{prefix}{idx:0{pad_digits}d}{ext}"
        
        # 避免覆盖冲突
        if os.path.exists(new_name):
            print(f"错误：文件名冲突 {new_name}，已终止")
            return
            
        os.rename(filename, new_name)
        print(f"重命名: {filename} → {new_name}")

if __name__ == "__main__":
    # 自定义参数（前缀、位数）
    rename(prefix="", digits=4)