# 练习16.读写文件
#根据课程使用cmd直接写不合适ide，而且使用python 2.x ，我常用为3.10顾不采纳教学篇章内容

import os

def main():
    """更简洁的文件操作示例"""
    fliename = "demo.txt"
    # 创建文件
    with open(fliename, "w") as f:
        line1 = input("line1?")
        line2 = input("line2?")
        line3 = input("line3?")
        print(f"we're going to write {fliename}")
        f.write(f"{line1}\n{line2}\n{line3}")
        # f.write("文件操作示例\n第一行\n第二行\n")
    print("文件创建成功")

    # 读取文件



    print("\n文件内容:")
    with open("demo.txt", "r") as f:
        print(f.read())

    # 删除文件
    os.remove("demo.txt")
    print("\n文件已删除")


if __name__ == "__main__":
    main()