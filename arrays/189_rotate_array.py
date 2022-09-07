# -*- coding:utf-8 -*-
# @FileName  :189_rotate_array.py
# @Time      :2022/9/7 11:08
# @Author    : yuhaiping


def rotate_array_1(nums, k):
    """
    轮转数组 切片方法

    :param nums:
    :param k:
    :return:
    """
    n = len(nums)
    k = k % n
    # 这里为啥不用 nums = nums[n-k:] + nums[:n-k]？
    # 我的理解: 函数内部 对 nums 重新赋值 相当于开辟了新的内存地址，对外部传过来的参数 并没有修改
    # 使用 nums[:] ，则是在外部的参数的内存地址上进行修改，并没有开辟新的内存地址
    nums[:] = nums[n-k:] + nums[:n-k]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    s = 1
    rotate_array_1(a, s)
    print(a)
