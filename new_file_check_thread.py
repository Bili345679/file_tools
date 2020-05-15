import hashlib
import threading
import os

import p
import file_info

public_file_block = ""

md5_hash	    = hashlib.md5()
# sha1_hash	    = hashlib.sha1()
# sha224_hash	    = hashlib.sha224()
# sha256_hash	    = hashlib.sha256()
# sha384_hash	    = hashlib.sha384()
# sha512_hash	    = hashlib.sha512()
# blake2b_hash	= hashlib.blake2b()
# blake2s_hash	= hashlib.blake2s()
# sha3_224_hash	= hashlib.sha3_224()
# sha3_256_hash	= hashlib.sha3_256()
# sha3_384_hash	= hashlib.sha3_384()
# sha3_512_hash	= hashlib.sha3_512()

def reset():
    global public_file_block
    public_file_block = ""

    global md5_hash
    md5_hash = None
    md5_hash = hashlib.md5()

    global sha1_hash
    sha1_hash = None
    sha1_hash = hashlib.sha1()

    global sha224_hash
    sha224_hash = None
    sha224_hash = hashlib.sha224()

    global sha256_hash
    sha256_hash = None
    sha256_hash = hashlib.sha256()

    global sha384_hash
    sha384_hash = None
    sha384_hash = hashlib.sha384()

    global sha512_hash
    sha512_hash = None
    sha512_hash = hashlib.sha512()

    global blake2b_hash
    blake2b_hash = None
    blake2b_hash = hashlib.blake2b()

    global blake2s_hash
    blake2s_hash = None
    blake2s_hash = hashlib.blake2s()

    global sha3_224_hash
    sha3_224_hash = None
    sha3_224_hash = hashlib.sha3_224()

    global sha3_256_hash
    sha3_256_hash = None
    sha3_256_hash = hashlib.sha3_256()

    global sha3_384_hash
    sha3_384_hash = None
    sha3_384_hash = hashlib.sha3_384()

    global sha3_512_hash
    sha3_512_hash = None
    sha3_512_hash = hashlib.sha3_512()


def check_file_block(file_name, block_size = 8910720 * 2):
    # print(p.sc(file_info.dp(file_name), "Y"), end="")
    global public_file_block
    file = open(file_name, mode="rb")
    checking_size = 0
    file_size = os.path.getsize(file_name)
    while True:
        print_str = p.get_num_of_num(checking_size, file_size, auto_color=True, hlhs= True, percentage=True) + "    "
        print(print_str, end="")
        for i in range(len(print_str) - 11):
            print("\b", end="")
        print(end="", flush=True)
        checking_size += block_size

        file_block = file.read(block_size)

        public_file_block = file_block

        thread_check_dict = {}
        thread_check_dict["md5"]        = md5_class()
        thread_check_dict["sha1"]       = sha1_class()
        thread_check_dict["sha224"]     = sha224_class()
        thread_check_dict["sha256"]     = sha256_class()
        thread_check_dict["sha384"]     = sha384_class()
        thread_check_dict["sha512"]     = sha512_class()
        thread_check_dict["blake2b"]    = blake2b_class()
        thread_check_dict["blake2s"]    = blake2s_class()
        thread_check_dict["sha3_224"]   = sha3_224_class()
        thread_check_dict["sha3_256"]   = sha3_256_class()
        thread_check_dict["sha3_384"]   = sha3_384_class()
        thread_check_dict["sha3_512"]   = sha3_512_class()

        for each_check_thread in thread_check_dict:
            thread_check_dict[each_check_thread].start()

        for each_check_thread in thread_check_dict:
            thread_check_dict[each_check_thread].join()

        if(len(file_block) < block_size):
            break

    file_check_result_dict = dict()
    file_check_result_dict["md5"]       = md5_hash.hexdigest()
    file_check_result_dict["sha1"]      = sha1_hash.hexdigest()
    file_check_result_dict["sha224"]    = sha224_hash.hexdigest()
    file_check_result_dict["sha256"]    = sha256_hash.hexdigest()
    file_check_result_dict["sha384"]    = sha384_hash.hexdigest()
    file_check_result_dict["sha512"]    = sha512_hash.hexdigest()
    file_check_result_dict["blake2b"]   = blake2b_hash.hexdigest()
    file_check_result_dict["blake2s"]   = blake2s_hash.hexdigest()
    file_check_result_dict["sha3_224"]  = sha3_224_hash.hexdigest()
    file_check_result_dict["sha3_256"]  = sha3_256_hash.hexdigest()
    file_check_result_dict["sha3_384"]  = sha3_384_hash.hexdigest()
    file_check_result_dict["sha3_512"]  = sha3_512_hash.hexdigest()

    file.close()
    reset()

    return file_check_result_dict

# 线程部分

class md5_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        md5_hash.update(public_file_block)


class sha1_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sha1_hash.update(public_file_block)


class sha224_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sha224_hash.update(public_file_block)


class sha256_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sha256_hash.update(public_file_block)


class sha384_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sha384_hash.update(public_file_block)


class sha512_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sha512_hash.update(public_file_block)


class blake2b_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        blake2b_hash.update(public_file_block)


class blake2s_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        blake2s_hash.update(public_file_block)


class sha3_224_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sha3_224_hash.update(public_file_block)


class sha3_256_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sha3_256_hash.update(public_file_block)


class sha3_384_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sha3_384_hash.update(public_file_block)


class sha3_512_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sha3_512_hash.update(public_file_block)
