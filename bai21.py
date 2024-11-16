# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:46:22 2024

@author: PC
"""

def question_21(nums: list[int], target: int):
    dagap=set()
    for num in nums:
        soconlai=target-num
        if soconlai in dagap:
            return(num,soconlai)
        dagap.add(num)
    return None
nums=[1,2,3,4,5]
target=10
print(question_21(nums, target))