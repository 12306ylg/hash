import logging
import os
import random
import hashlib
import time
import sys
from io import BytesIO
import psutil

psutil.Process(psutil.Process().pid).nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志输出格式
    filename="hash.log",  # log日志输出的文件位置和文件名
    format="%(asctime)s-%(levelname)-3s:%(message)s",  # 日志输出的格式
    datefmt="%Y-%m-%d %H:%M:%S",  # 时间输出的格式
)


def hashboom(thread_id: int):
    while True:
        HAHA = b""
        HAHA2 = b""
        for progress in range(random.randint(1, 256)):
            HAHA += os.urandom(65536)
            HAHA2 += os.urandom(65536)
            # print(thread + ":" + str(progress) + "\n")
        f1 = open(f"F1.{thread_id}", "wb+")
        f2 = open(f"F2.{thread_id}", "wb+")
        f1.write(HAHA)
        f2.write(HAHA2)
        f1.close
        f2.close
        hd1 = hashlib.sha256()
        hd2 = hashlib.sha256()
        hd1.update(f1.read())
        hd2.update(f2.read())
        hash1 = hd1.hexdigest()
        hash2 = hd2.hexdigest()
        if hash1 == hash2:
            print("成功")
            with open("matched", "+a") as FIN:  # input("ENTER:")
                FIN.write(f"{hash1}\n")
            exit(0)
        else:
            f1.write("")
            f2.write("")
            logging.info(f"{hash1}-{hash2}")


hashboom(int((sys.argv[1:])[0]))  #
