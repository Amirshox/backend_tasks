"""
JSON matnni Dict tipidagi ma’lumotga va aksincha o’giradigan funskiya yozing. * json kutubxonasidan foydalanmasdan.

"""

# jsonni dictga o'girishni yana bir usuli split yoki regaxlar bilan bo'lib chiqib dictga yozib chiqsa bo'ladi.
# Xuddi shu usulda qilmoqchi edim, lekin juda murakkablashib ketdi.
# Shu uchun oddiyroq funksiya ishlatib qilishga qaror qildim :) .

from typing import Union


def parser(arg: Union[str, dict]) -> Union[str, dict]:
    if isinstance(arg, str):
        return eval(arg)
    elif isinstance(arg, dict):
        return str(arg)
    else:
        raise TypeError('Wrong type of argument')


json_test = "{'name': 'John', 'age': '35', 'city': 'New York', 'tests': {'math': 'A', 'physics': 'B'}}"
dict_test = {'name': 'John', 'age': '35', 'city': 'New York', 'tests': {'math': 'A', 'physics': 'B'}}

print(parser(json_test))
print(parser(dict_test))
