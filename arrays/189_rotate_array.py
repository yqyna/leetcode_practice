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


def rotate_array_2(nums, k):
    """
    轮转数组 反转方法

    :param nums:
    :param k:
    :return:
    """

    def reverse(arr, a, b):
        """

        :param arr:
        :param a:
        :param b:
        :return:
        """
        while a < b:
            arr[a], arr[b] = arr[b], arr[a]
            a += 1
            b -= 1
    n = len(nums)
    k = k % n
    reverse(nums, 0, n - k - 1)
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - 1)


if __name__ == '__main__':
    c = [1, 2, 3, 4, 5, 6, 7]
    s = 3
    # rotate_array_1(c, s)  [5, 6, 7, 1, 2, 3, 4]
    rotate_array_2(c, s)  # [5, 6, 7, 1, 2, 3, 4]
    print(c)
