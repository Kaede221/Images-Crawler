"""
可以生成一串长度为n的随机字符串，完全随机
"""
import string
import random


def get_random_str(length: int) -> str:
    return ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(length))
