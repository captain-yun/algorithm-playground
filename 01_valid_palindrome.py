# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며 영문자와 숫자만을 대상으로 한다.
import re

# class Solution:
#     def isPalindrome(self, s: str):
#         s.lower()
#         p = re.compile()
#         p.match(s)
#         print(s)
def isPalindrome(s: str):
    s = s.lower()
    # s_after = ''
    # p = re.compile("[a-z0-9]")
    # for ch in s:
    #     s_after += p.match(ch).group() if p.match(ch) else ''

    s_after = re.sub('[^a-z0-9]', '', s)

    print(s_after == s_after[::-1])
    return s_after == s_after[::-1]

if __name__ == "__main__":
    isPalindrome("A man, a plan, a canal: Panama")

# Regular Expression

# Answers in the book #
# # 1.
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         # 팰린드롬 여부 판별
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
#
#         return True
#
# # 2.
# import collections
# from typing import Deque
#
#
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # 자료형 데크로 선언
#         strs: Deque = collections.deque()
#
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
#
#         return True
#
# #3.
# import re
#
#
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         # 정규식으로 불필요한 문자 필터링
#         s = re.sub('[^a-z0-9]', '', s)
#
#         return s == s[::-1]  # 슬라이싱