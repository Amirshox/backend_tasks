"""
Tuple tipidagi ma’lumotlar to’plami saqlanayotgan o’zgaruvchi argument sifatida berilganda o’zgaruvchining xotiradan
egallayotgan hajmi (size) ni qaytaradigan funksiya yozing.
"""

import sys


def get_size_from_memory(elements: tuple):
    return f"{sys.getsizeof(elements)} bytes"


tpl = (1, 2, 3)
print(get_size_from_memory(tpl))
