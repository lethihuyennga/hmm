# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:29:48 2024

@author: PC
"""

from collections import Counter

def question_24(nums: list[int]) -> int:
    # Đếm số lần xuất hiện của từng phần tử
    dem = Counter(nums)
    # Trả về phần tử có tần suất lớn hơn n / 2
    return max(dem, key=dem.get)
nums=[3, 2, 3,4,5,4,4,5,4]
print(question_24(nums))