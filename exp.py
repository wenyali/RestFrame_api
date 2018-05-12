#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "wenyali"
__mtime__ = "2018/5/8"
# 归并排序
def gui(li):
    if len(li) == 1:
        return li
    mid= int(len(li)//2)
    left = gui(li[:mid])
    right = gui(li[mid:])
    return merge(left,right)

def merge(left,right):
    result = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i] <=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

# 快排
def quick_sort(li,left,right):
    if len(li) == 1:
        return li
    pivot = find_pivot(li,left,right)
    quick_sort(li,left,pivot-1)
    quick_sort(li,pivot+1,right)
    return li

def find_pivot(li,left,right):
    pivot = li[left]
    while left <right:
        while left < right and li[right] > li[left]:
            right-=1
        li[left] = li[right]
        while left < right and li[left] <li[right]:
            left+=1
        li[right] = li[left]
    li[left] = pivot
    return li[left]






if __name__ == "__main__":
    li = [4, 5, 7, 9, 7, 5, 1, 0, 7, -2, 3, -99, 6]
    #print(gui(li))
    #print(quick_sort(li,0,len(li)-1))
    # eval 将字符串解析成函数
    # print(eval("print('hello')"))

