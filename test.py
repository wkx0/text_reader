def test():
    with open(r'D:\Downloads\小说\《南宋第一卧底》.txt', 'r') as file:
        # 读取前10个字符
        data = file.read(10)
        print("读取的数据:", data)

        # 获取当前文件指针的位置
        position = file.tell()
        print("当前文件指针位置:", position)

        # 将文件指针移动到之前读取的位置
        file.seek(position)

        # 重新读取文件内容
        # data2 = file.read()
        # print("重新读取的数据:", data2)


if __name__ == '__main__':
    test()
