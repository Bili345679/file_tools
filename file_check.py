import os
import time
import json
import hashlib

import p
import file_info
import tool_file
import new_file_check_thread

def get_all_file_check(file_list, path):
    start_time = time.time()
    print(p.tc("Y") + " get_all_file_check " + p.sc(path, "Y"))
    check_dict = dict()
    num = 1
    all_file_size = file_info.get_file_size_sum(file_list)
    checked_size = 0
    for each_file in file_list:
        spend_time = time.time() - start_time
        print("\r" + p.tc("Y") + " check_file "
                + p.get_speed_from_time_and_size(spend_time, checked_size, "G") + " "
                + p.get_need_time(spend_time, checked_size, all_file_size, "G") + " "
                + p.get_num_of_num(checked_size, all_file_size, auto_color=True, percentage=True) + " "
                + p.get_num_of_num(num, len(file_list), auto_color=True)
                + " ", end="")
        check_dict[each_file.replace(path, "")] = new_file_check_thread.check_file_block(each_file)
        num += 1
        checked_size += os.path.getsize(each_file)
    spend_time = time.time() - start_time
    print("\r" + p.tc("G") + " all_file_check_over    spend_time:"
          + p.get_time_from_second(spend_time, "G")
          + "    speed:" + p.get_speed_from_time_and_size(spend_time, all_file_size, "G")
          + "        ")
    return check_dict

def set_file_check(path):
    print(p.tc("B") + " set_file_check " + p.sc(path, "B"))
    print(p.tc("Y") + " get_file_list " + p.sc(path, "Y"))
    file_list = file_info.get_file_list(path)
    file_ckeak_list = get_all_file_check(file_list, path)
    ckf_file_name = tool_file.set_ckf_file(path, file_ckeak_list)
    print(p.tc("Y") + " set_file_check_over " + p.sc(path, "G"))
    return ckf_file_name

# check_from_file 校验参考文件
# check_to_file
def check_file_check(path, check_from_file = False, check_to_file = False):
    print(p.tc("B") + " check_file_check " + p.sc(path, "B"))
    if check_from_file:
        old_file = check_from_file()
    else:
        old_file = tool_file.get_ckf_file(path)
    old_file_info_dict = tool_file.get_dict_from_file(old_file)
    if check_to_file:
        new_file = check_to_file
        new_file_info_dict = tool_file.get_dict_from_file(new_file)
    else:
        print(p.tc("Y") + " get_file_list " + p.sc(path, "Y"))
        file_list = file_info.get_file_list(path)
        new_file_info_dict = get_all_file_check(file_list, path)
    new_file_info_dict_copy = new_file_info_dict.copy()
    error_file_list = list()
    lose_file_list = list()
    new_file_list = list()

    for each_old_info in old_file_info_dict:
        if each_old_info in new_file_info_dict:
            if not new_file_info_dict.pop(each_old_info) == old_file_info_dict[each_old_info]:
                error_file_list.append(each_old_info)
        else:
            lose_file_list.append(each_old_info)

    for each_new_file in new_file_info_dict:
        new_file_list.append(each_new_file)

    print(p.tc("G") + " check_file_check_over " + p.sc(path, "G"))
    return {"new_check_result"  : new_file_info_dict_copy,
            "error_file_list"   : error_file_list,
            "lose_file_list"    : lose_file_list,
            "new_file_list"     : new_file_info_dict}

def print_cheak_file_cheak_result(result):
    print("error_file_list")
    error_flag = False
    for each_error_file in result["error_file_list"]:
        print("\t" + p.sc(each_error_file, "R"))
        error_flag = True
    if not error_flag:
        print(p.sc("no error", "G"))
    print()

    print("lose_file_list")
    lose_flag = False
    for each_lose_file in result["lose_file_list"]:
        print("\t" + p.sc(each_lose_file, "R"))
        lose_flag = True
    if not lose_flag:
        print(p.sc("no lose", "G"))
    print()

    print("new_file_list")
    new_flag = False
    for each_new_file in result["new_file_list"]:
        print("\t" + p.sc(each_new_file, "Y"))
        new_flag = True
    if not new_flag:
        print(p.sc("no new", "G"))
    print()

    if error_flag or lose_flag or new_flag:
        return True
    else:
        return False

def start():
    print(p.sc("文件校验系统", "B"))
    print(p.sc("使用说明:", "Y"))
    print(p.sc("生成校验文件:", "Y"), end="")
    print("输入根目录没有" + p.sc("校验文件", "G") + "的文件夹地址")
    print(p.sc("校验文件:", "Y"), end="")
    print("将" + p.sc("校验文件", "G") + "放入需校验文件夹的根目录")
    print(p.sc("校验文件", "G") + "的命名格式是" + p.sc("需校验文件夹根目录名_时间戳.345679_file_check", "G"))
    path = input("请输入地址：")

    old_file = tool_file.get_ckf_file(path)
    if old_file:
        print(p.tc("G") + "检测到校验文件，进行文件校验，若要保存新的校验文件，需等候文件校验结束后，选择\"保存新的校验结果\",会比直接生成校验文件多花费极少极少的时间")
        res = check_file_check(path)
        ckf = res["new_check_result"]
        ckr = dict()
        ckr["error_file_list"]  = res["error_file_list"]
        ckr["lose_file_list"]   = res["lose_file_list"]
        ckr["new_file_list"]    = res["new_file_list"]
        if print_cheak_file_cheak_result(ckr):
            save_result = input(p.tc("R") + "是否保存异常文件列表(y/n)(默认保存):")
            if save_result == "N" or save_result == "n":
                print(p.tc("R") + "不保存异常文件列表")
            else:
                print(p.tc("R") + "正在保存异常文件列表", end="")
                ckr_file_name = tool_file.set_ckr_file(path, ckr)
                print("\r" + p.tc("R") + "保存异常文件列表完毕 \t" + p.sc(ckr_file_name, "R"))
        else:
            print(p.tc("G") + "没有发现异常文件")

        save_check = input(p.tc("G") + "是否保存新的校验结果(y/n)(默认保存):")
        if save_check == "N" or save_check == "n":
                print(p.tc("G") + "不保存新的校验结果")
        else:
            print(p.tc("G") + "正在保存新的校验结果", end="")
            ckr_file_name = tool_file.set_ckr_file(path, ckf)
            print("\r" + p.tc("G") + "保存新的校验结果完毕 \t" + p.sc(ckr_file_name, "G"))

        del_tool_file = input(p.tc("G") + "是否删除所有工具文件(y/n)(默认不删除):")
        if del_tool_file == "Y" or del_tool_file == "y":
            print(p.tc("G") + "正在删除所有工具文件", end="")
            tool_file.del_tool_file(path)
            print("\r" + p.tc("G") + "已删除所有工具文件")
        else:
            print(p.tc("G") + "不删除所有工具文件")

    else:
        print(p.tc("G") + "未检测到校验文件，生成校验文件")
        set_file_check(path)

if __name__ == '__main__':
    start()