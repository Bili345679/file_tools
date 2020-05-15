import time
import os
# import psutil

os.system("")

#   获得带有颜色的时间字符串
def tc(color = "G"):
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    color_time_str = sc(time_str, font_color=color)
    return "[" + color_time_str + "] "

#   转换字符串为带颜色的字符串
#   font_color  颜色
#       D   Dark        黑色
#       R   Red         红色
#       G   Green       绿色
#       Y   Yellow      黄色
#       B   Blue        蓝色
#       V   Violet      紫色
#       L   Light_blue  淡蓝色
#       GR  GRey        灰色
#   bg_color    背景色
#       D   Dark        黑色
#       R   Red         红色
#       G   Green       绿色
#       Y   Yellow      黄色
#       B   Blue        蓝色
#       V   Violet      紫色
#       L   Light_blue  淡蓝色
#       GR  GRey        灰色
def sc(string, font_color = "N", bg_color = "N"):
    if font_color == "D":   # Dark          黑色
        font_color_code = 30
    elif font_color == "R": # Red           红色
        font_color_code = 31
    elif font_color == "G": # Green         绿色
        font_color_code = 32
    elif font_color == "Y": # Yellow        黄色
        font_color_code = 33
    elif font_color == "B": # Blue          蓝色
        font_color_code = 34
    elif font_color == "V": # Violet        紫色
        font_color_code = 35
    elif font_color == "L": # Light_blue    淡色
        font_color_code = 36
    elif font_color == "GR": # Grey    淡色
        font_color_code = 37
    else:                   # Null          无色
        font_color_code = 0

    if bg_color == "D":     # dark          黑色
        bg_color_code = 40
    elif bg_color == "R":   # red           红色
        bg_color_code = 41
    elif bg_color == "G":   # green         绿色
        bg_color_code = 42
    elif bg_color == "Y":   # yellow        黄色
        bg_color_code = 43
    elif bg_color == "B":   # blue          蓝色
        bg_color_code = 44
    elif bg_color == "V":   # Violet        紫色
        bg_color_code = 45
    elif bg_color == "L":   # Light_blue    淡色
        bg_color_code = 46
    elif bg_color == "GR":  # Grey          淡色
        bg_color_code = 47
    else:                   # Null          无色
        bg_color_code = 0

    color_string = "\033[0"
    if font_color_code:
        color_string += ";" + str(font_color_code)
    if bg_color_code:
        color_string += ";" + str(bg_color_code)
    color_string += "m"

    color_string += str(string)

    color_string += "\033[0m"

    return color_string

def how_many_memery_can_i_user():
    virtual_memory = psutil.virtual_memory()
    free_memory = virtual_memory.free

def replace_char(string):
    string = string.replace("\\", "\\\\")
    string = string.replace("\'", "\\\'")
    string = string.replace("\"", "\\\"")
    string = string.replace("\n\n", "\\n")
    string = string.replace("\r\n", "\\n")
    string = string.replace("\n", "\\n")
    string = string.replace("\t", "\\t")
    return string

def get_num_of_num(new_num, all_num, auto_color = False, new_num_color = "N", all_num_color = "N", percentage = False, hlhs = False):
    if auto_color:
        color_choice = new_num / all_num
        if color_choice < 0.2:
            new_num_color = "B"
        elif color_choice < 0.4:
            new_num_color = "V"
        elif color_choice < 0.6:
            new_num_color = "R"
        elif color_choice < 0.8:
            new_num_color = "Y"
        else:
            new_num_color = "G"

    if hlhs:
        result = new_num / all_num * 100
        if result >= 100:
            full_block = "##########"
            empty_block = ""
        elif result > 90:
            full_block = "#########"
            empty_block = "-"
            result = result - 90
        elif result > 80:
            full_block = "########"
            empty_block = "--"
            result = result - 80
        elif result > 70:
            full_block = "#######"
            empty_block = "---"
            result = result - 70
        elif result > 60:
            full_block = "######"
            empty_block = "----"
            result = result - 60
        elif result > 50:
            full_block = "#####"
            empty_block = "-----"
            result = result - 50
        elif result > 40:
            full_block = "####"
            empty_block = "------"
            result = result - 40
        elif result > 30:
            full_block = "###"
            empty_block = "-------"
            result = result - 30
        elif result > 20:
            full_block = "##"
            empty_block = "--------"
            result = result - 20
        elif result > 10:
            full_block = "#"
            empty_block = "---------"
            result = result - 10
        else:
            full_block = ""
            empty_block = "----------"

        if result > 9:
            not_full_block = "9"
        elif result > 8:
            not_full_block = "8"
        elif result > 7:
            not_full_block = "7"
        elif result > 6:
            not_full_block = "6"
        elif result > 5:
            not_full_block = "5"
        elif result > 4:
            not_full_block = "4"
        elif result > 3:
            not_full_block = "3"
        elif result > 2:
            not_full_block = "2"
        else:
            not_full_block = "1"

        hlhs = "[" + full_block + not_full_block + empty_block + "] "
    else:
        hlhs = ""

    if percentage:
        return sc(hlhs + '%.2f' % (new_num/all_num*100), new_num_color) + "%"
    else:
        return  sc(hlhs + str(new_num), new_num_color) + "/" + sc(str(all_num), all_num_color)

def get_need_time(used_time, over, all, color = "N"):
    if over:
        need_time = all / over * used_time - used_time
        return get_time_from_second(need_time, color=color)
    else:
        return ""

def get_speed_from_time_and_size(time, size, color = "N"):
    if time:
        speed = size / time
        if speed > 1024 * 1024 * 1024 *1024:
            speed =  sc("%.3f" % (speed / 1024 / 1024 / 1024 / 1024), color) + "TB/s"
        elif speed > 1024 * 1024 * 1024:
            speed = sc("%.3f" % (speed / 1024 / 1024 / 1024), color) + "GB/s"
        elif speed > 1024 * 1024:
            speed = sc("%.3f" % (speed/ 1024 / 1024), color) + "MB/s"
        elif speed > 1024:
            speed = sc("%.3f" % (speed / 1024), color) + "KB/s"
        else:
            speed = sc("%.3f" % (speed), color) + "B/s"
        return speed
    else:
        return ""

def get_time_from_second(second, color = "N"):
    d = int(second / 86400)
    second = second - d * 86400
    h = int(second / 3600)
    second = second - h * 3600
    m = int(second / 60)
    second = second - m * 60
    s = int(second)
    ms = ("%.3f" % (second - int(second))).replace("0.", "")

    if d:
        d = sc(d, color) + "D."
    else:
        d = ""
    if d or h:
        h = sc(h, color) + "H."
    else:
        h = ""
    if d or h or m:
        m = sc(m, color) + "M."
    else:
        m = ""
    if d or h or m or s:
        s = sc(s, color) + "S."
    else:
        s = ""
    ms = sc(ms, color) + "MS."

    return d+h+m+s+ms