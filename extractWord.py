# coding=utf-8
# 正则库
import re
# 用于给dict排序
import operator

# 读取文件的路径
src_file_path = 'C:\\Users\\think\\Desktop\\cedt.txt'
# 保存文件的路径
dst_file_path = './result.txt'

# 保存单词的dict
word_map = {}
# 编译正则模版
rx = re.compile(r"▶ <b>(.*?)</b>")
# 打开文件 指定编码utf-8 否则乱码
with open(src_file_path, 'r', encoding='utf-8') as f:
    # 读取一行
    line = f.readline()
    # 循环读取整个文件
    while line:
        # 用正则表达式匹配当前行得到结果 返回为一个list
        res_arr = rx.findall(line)
        # 将结果list中的单词依次放入dict
        for key in res_arr:
            # dict的key为需要的单词，value不重要
            word_map[key] = ''
        line = f.readline()
# 给结果dict按字典顺序排序
sorted_x = sorted(word_map.items(), key=operator.itemgetter(0))
# 打开保存文件
with open(dst_file_path, 'w', encoding='utf-8') as f:
    # 遍历结果dict将key依次存入
    for key, value in sorted_x:
        f.write(key + '\n')
