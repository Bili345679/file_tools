import p
import os

# 获取路径中所有文件名
def get_file_list(path, need_tool_file = False):
    file_list = list()
    for root, dirs, files in os.walk(path):
        # 遍历文件
        for f in files:
            if get_file_type(f) == "ckf345679" or get_file_type(f) == "ckr345679":
                if need_tool_file:
                    file_list.append(os.path.join(root, f))
            else:
                file_list.append(os.path.join(root, f))
    return file_list

# 获取文件类型(其实是后缀)
def get_file_type(file_name):
    point = file_name.rfind(".")
    return file_name[point + 1:]

# 获取多个文件的总体积
def get_file_size_sum(file_list):
    size_sum = 0
    for each_file in file_list:
        size_sum += os.path.getsize(each_file)
    return size_sum

# 删除文件名中的路径
# 删除路径前非最后一个文件夹以外的所有文件字符
# del path from file_name
def dp(path):
    start = path.rfind("\\") + 1
    if start == 0:
        return path
    else:
        return path[start:]
