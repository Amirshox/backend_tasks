"""
Pythonda tartiblanmagan elementlardan iborat bo’lgan ro’yxat (list) berilgan. N ta eng katta va eng kichik
elementlarni chiqaruvchi dastur yozing. (eng optimal usulda)
"""


class Solution:
    def __init__(self, numbers: list, n: int):
        self.numbers = numbers
        self.n = n

    def solve(self) -> tuple[list, list]:
        sorted_numbers = self.quick_sort(self.numbers)
        return sorted_numbers[:self.n], sorted_numbers[-self.n:]

    def quick_sort(self, numbers: list) -> list:
        if len(numbers) <= 1:
            return numbers
        pivot = numbers[0]
        less = [i for i in numbers[1:] if i <= pivot]
        greater = [i for i in numbers[1:] if i > pivot]
        return self.quick_sort(less) + [pivot] + self.quick_sort(greater)


s = Solution([-12, 3, 33, 12, 99, -88, 2, 45], 2)
print(s.solve())
