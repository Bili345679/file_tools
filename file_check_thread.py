import hashlib
import threading
import p

public_file_block = ""

def check_file_block(file_block):
    global public_file_block
    public_file_block = file_block
    # print(public_file_block)
    file_check_dict = dict()

    thread_check_dict = dict()
    thread_check_dict["md5"] = md5_class()
    thread_check_dict["sha1"] = sha1_class()
    thread_check_dict["sha224"] = sha224_class()
    thread_check_dict["sha256"] = sha256_class()
    thread_check_dict["sha384"] = sha384_class()
    thread_check_dict["sha512"] = sha512_class()
    thread_check_dict["blake2b"] = blake2b_class()
    thread_check_dict["blake2s"] = blake2s_class()
    thread_check_dict["sha3_224"] = sha3_224_class()
    thread_check_dict["sha3_256"] = sha3_256_class()
    thread_check_dict["sha3_384"] = sha3_384_class()
    thread_check_dict["sha3_512"] = sha3_512_class()

    for each_check_thread in thread_check_dict:
        thread_check_dict[each_check_thread].start()

    for each_check_thread in thread_check_dict:
        thread_check_dict[each_check_thread].join()

    for each_check_thread in thread_check_dict:
        file_check_dict[each_check_thread] = thread_check_dict[each_check_thread].check

    return file_check_dict


class md5_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "md5_check_start")
        self.check = hashlib.md5(public_file_block).hexdigest()
        print(p.tc("Y") + "md5_check_over")


class sha1_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "sha1_check_start")
        self.check = hashlib.sha1(public_file_block).hexdigest()
        print(p.tc("Y") + "sha1_check_over")


class sha224_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "sha224_check_start")
        self.check = hashlib.sha224(public_file_block).hexdigest()
        print(p.tc("Y") + "sha224_check_over")


class sha256_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "sha256_check_start")
        self.check = hashlib.sha256(public_file_block).hexdigest()
        print(p.tc("Y") + "sha256_check_over")


class sha384_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "sha384_check_start")
        self.check = hashlib.sha384(public_file_block).hexdigest()
        print(p.tc("Y") + "sha384_check_over")


class sha512_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "sha512_check_start")
        self.check = hashlib.sha512(public_file_block).hexdigest()
        print(p.tc("Y") + "sha512_check_over")


class blake2b_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "blake2b_check_start")
        self.check = hashlib.blake2b(public_file_block).hexdigest()
        print(p.tc("Y") + "blake2b_check_over")


class blake2s_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "blake2s_check_start")
        self.check = hashlib.blake2s(public_file_block).hexdigest()
        print(p.tc("Y") + "blake2s_check_over")


class sha3_224_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "sha3_224_check_start")
        self.check = hashlib.sha3_224(public_file_block).hexdigest()
        print(p.tc("Y") + "sha3_224_check_over")


class sha3_256_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "sha3_256_check_start")
        self.check = hashlib.sha3_256(public_file_block).hexdigest()
        print(p.tc("Y") + "sha3_256_check_over")


class sha3_384_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "sha3_384_check_start")
        self.check = hashlib.sha3_384(public_file_block).hexdigest()
        print(p.tc("Y") + "sha3_384_check_over")


class sha3_512_class(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.check = ""

    def run(self):
        print(p.tc("Y") + "sha3_512_check_start")
        self.check = hashlib.sha3_512(public_file_block).hexdigest()
        print(p.tc("Y") + "sha3_512_check_over")