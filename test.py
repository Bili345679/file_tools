import hashlib
import new_file_check_thread
import time
import math
import p
import file_info

start = time.time()
print(file_info.get_file_list("D:\\"))
print(time.time() - start)

# print("asd", end="")
# for i in range(10001):
#     print_str = p.get_num_of_num(i, 10000, hlhs=True, auto_color=True)
#     print(print_str, end = "")
#     for a in range(len(print_str) - 19):
#         print("\b", end = "")
#     # print("asd", end="")
#     # print(len(print_str))
#     time.sleep(0.001)
# print()

# print(hashlib.md5(open("testfile_1024_1024_1024.txt", "rb").read()).hexdigest())
# hash = hashlib.md5()
# for i in range(1024):
#     # hash.update(open("testfile.txt", "rb").read())
#     hash.update(open("testfile.txt", "rb").read())
# print(hash.hexdigest())

# file = open("testfile_1024_1024_1024.txt", "w")
# for i in range(1024*1024*1024):
#     file.write("1")
# file.close()

# file_name = "D:\迅雷下载\[Airota&VCB-Studio] Chuunibyou demo Koi ga Shitai!\[Airota&VCB-Studio] Chuunibyou demo Koi ga Shitai! -Take On Me- [Ma10p_1080p]\[Airota&VCB-Studio] Chuunibyou demo Koi ga Shitai! -Take On Me- [Ma10p_1080p][x265_flac].mkv"
#
# file = open(file_name, mode="rb")
# hash = hashlib.md5()
#
# while True:
#     file_block = file.read(1024*1024)
#     hash.update(file_block)
#     if(len(file_block) < 1024*1024):
#         break
# print(hash.hexdigest())

# start_time = time.time()
# check_result_dict = new_file_check_thread.check_file_block("testfile_1024_1024_1024.txt")
# print(check_result_dict)
# # for each_check_result in check_result_dict:
# #     print(each_check_result + " : " + check_result_dict[each_check_result])
# print(time.time() - start_time)
#
# start_time = time.time()
# check_result_dict = new_file_check_thread.check_file_block("testfile_1024_1024_1024.txt", block_size=1024*1024)
# print(check_result_dict)
# print(time.time() - start_time)

# print(new_file_check_thread.check_file_block("testfile_1024_1024_1024.txt"))
# print("md5" + " : " + hashlib.md5(open("testfile.txt", "rb").read()).hexdigest())
# print("sha1" + " : " + hashlib.sha1(open("testfile.txt", "rb").read()).hexdigest())
# print("sha224" + " : " + hashlib.sha224(open("testfile.txt", "rb").read()).hexdigest())
# print("sha256" + " : " + hashlib.sha256(open("testfile.txt", "rb").read()).hexdigest())
# print("sha384" + " : " + hashlib.sha384(open("testfile.txt", "rb").read()).hexdigest())
# print("sha512" + " : " + hashlib.sha512(open("testfile.txt", "rb").read()).hexdigest())
# print("blake2b" + " : " + hashlib.blake2b(open("testfile.txt", "rb").read()).hexdigest())
# print("blake2s" + " : " + hashlib.blake2s(open("testfile.txt", "rb").read()).hexdigest())
# print("sha3_224" + " : " + hashlib.sha3_224(open("testfile.txt", "rb").read()).hexdigest())
# print("sha3_256" + " : " + hashlib.sha3_256(open("testfile.txt", "rb").read()).hexdigest())
# print("sha3_384" + " : " + hashlib.sha3_384(open("testfile.txt", "rb").read()).hexdigest())
# print("sha3_512" + " : " + hashlib.sha3_512(open("testfile.txt", "rb").read()).hexdigest())



# check_lsit = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256", "sha3_384", "sha3_512"]
#
# for e in check_lsit:
#     print("""global %s_hash
# %s_hash = None
# %s_hash = hashlib.%s()
# """ % (e, e, e, e))