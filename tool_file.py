import os
import time

import p
import file_info

# 获取工具文件list
def get_tool_file(path):
    file_list = file_info.get_file_list(path, need_tool_file=True)
    ckf_list = list()
    ckr_list = list()
    for each_file in file_list:
        file_type = file_info.get_file_type(each_file)
        if file_type == "ckf345679":
            ckf_list.append(each_file)
        elif file_type == "ckr345679":
            ckr_list.append(each_file)
    return {
        "ckf_list" : ckf_list,
        "ckr_lsit" : ckr_list
    }

# 删除文件夹中所有tool_info
def del_tool_file(path):
    file_list = file_info.get_file_list(path, need_tool_file=True)
    for each_file in file_list:
        file_type = file_info.get_file_type(each_file)
        if file_type == "ckf345679" or file_type == "ckr345679":
            os.remove(each_file)

# 获取文件名中的信息
# get_info_from_file
def get_info_from_file(file_name):
    file_name = file_name.replace("#", "")
    file_name = file_info.dp(file_name)

    dict_name_end = file_name.rfind("_")
    dict_name = file_name[0:dict_name_end]

    time_start = dict_name_end + 1
    time_end = file_name.rfind(".")

    time = int(file_name[time_start:time_end])

    return {"dict_name":dict_name, "time":time}

# 获取单个校验文件
def get_ckf_file(path, oldest = True):
    ckf_list = get_tool_file(path)["ckf_list"]
    if ckf_list:
        ckf_name = ""
        ckf_time = 0
        first_flag = True
        if oldest:
            for each_file in ckf_list:
                file_time = get_info_from_file(each_file)["time"]
                dict_name = get_info_from_file(each_file)["dict_name"]
                if dict_name == file_info.dp(path):
                    if first_flag:
                        first_flag = False
                        ckf_name = each_file
                        ckf_time = file_time
                    else:
                        if file_time < ckf_time:
                            ckf_name = each_file
                            ckf_time = file_time
        else:
            for each_file in ckf_list:
                file_time = get_info_from_file(each_file)["time"]
                dict_name = get_info_from_file(each_file)["dict_name"]
                if dict_name == file_info.dp(path):
                    if first_flag:
                        first_flag = False
                        ckf_name = each_file
                        ckf_time = file_time
                    else:
                        if file_time > ckf_time:
                            ckf_name = each_file
                            ckf_time = file_time
        return ckf_name
    else:
        return False

# 生成并写入校验文件
def set_ckf_file(path, result):
    dic_name = file_info.dp(path)
    # print(dic_name)
    time_str = str(int(time.time()))
    ckf_file_name = path + "\\" + "#" + dic_name + "_" + time_str + ".ckf345679"
    # print(ckf_file_name)
    file = open(ckf_file_name, "w", encoding='utf-8')
    file.write(str(result))
    file.close()
    return ckf_file_name

# 生成并写入校验结果文件
def set_ckr_file(path, result):
    dic_name = file_info.dp(path)
    time_str = str(int(time.time()))
    ckf_file_name = path + "/" + "#" + dic_name + "_" + time_str + ".ckr345679"
    file = open(ckf_file_name, "w", encoding='utf-8')
    file.write(str(result))
    file.close()
    return ckf_file_name


# 从文件中获取字典
def get_dict_from_file(file_name):
    file = open(file_name, "r", encoding='utf-8')
    info_str = file.read()
    info_dict = eval(info_str)
    return info_dict