"""
Sizga ikkita tartiblangan ro’yxat (sorted list) berilgan, shu ikkisini birlashtirib yangi ro’yxat (list)
hosil qiluvchi funksiya yarating.
"""


def merge_lists(first_list: list, second_list: list) -> list:
    sorted_list = []
    while first_list and second_list:
        if first_list[0] < second_list[0]:
            sorted_list.append(first_list.pop(0))
        else:
            sorted_list.append(second_list.pop(0))
    sorted_list += first_list
    sorted_list += second_list
    return sorted_list


list1 = [10, 12, 14, 16, 18, 20]
list2 = [11, 13, 15, 17, 19]

print(merge_lists(list1, list2))
