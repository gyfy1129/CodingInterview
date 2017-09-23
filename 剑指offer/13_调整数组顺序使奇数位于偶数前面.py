# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        n = len(array)
        num1 = []
        num2 = []
        for i in range(0, n):
            if array[i] % 2 == 0:
                num2.append(array[i])
            else:
                num1.append(array[i])
        num1.extend(num2)
        return num1


if __name__ == '__main__':
    num = [5, 3, 7, 3, 6, 4, 2, 0, 7, 4, 2]
    bat = Solution()
    print bat.reOrderArray(num)
