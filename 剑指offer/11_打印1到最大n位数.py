# -*- coding:utf-8 -*-
class Solution:
    def print_number(self, n):

        number = 1
        for i in range(1,n+1):
            number = 10 * number
        for i in range(1,number):
            print i,




if __name__ == '__main__':
    bat = Solution()
    bat.print_number(2)