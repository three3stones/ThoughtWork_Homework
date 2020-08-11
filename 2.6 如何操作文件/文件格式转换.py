"""
测试文件student.csv中包含了一组学生的信息，以csv格式保存，字段之间用,分割。
请完成以下任务：
    1. 编写python程序读取此文件的内容，并转换为json格式输出到student.json中。
"""

def convert_file_format(input_file_path: str, output_file_path: str,
                        input_format: str = 'csv', output_format: str = 'json'):
    import json
    input_file = input_file_path + "/student." + input_format
    output_file = output_file_path + "/student." + output_format
    
    fo = open(input_file, 'r', newline='', encoding='utf-8')         # 打开csv文件
    fw = open(output_file, 'w', encoding='utf-8')  # 打开json文件
    
    # 按行读取
    ls = []
    for line in fo:
        line = line.replace("\n", "")       # 将换行换成空
        ls.append(line.split(","))          # 以，为分隔符

    # 转换为字典形式
    for i in range(1, len(ls)):             # 遍历文件的每一行内容，除了列名
        ls[i] = dict(zip(ls[0], ls[i]))     # ls[0]为列名，所以为key,ls[i]为value,

    # 写入到json文件
    json.dump(ls[1:], fw, sort_keys=True, indent=4)

    # 关闭文件
    fo.close()
    fw.close()

convert_file_format("C:/Users/10920/Desktop/代码/IO操作", "C:/Users/10920/Desktop/代码/IO操作")

