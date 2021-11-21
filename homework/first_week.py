
'''
第一题：合并两个有序列表（可以直接查看链接）
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
https://leetcode-cn.com/problems/merge-two-sorted-lists/
解题思路：使用双指针
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
         #创建一个虚拟节点
         dummy=ListNode(-1)
         head=dummy
         p1=l1
         p2=l2
         while p1 is not None or p2 is not None:
            if not p2 or (p1 and p1.val<p2.val):
                head.next=p1
                p1=p1.next
            else:
                head.next=p2
                p2=p2.next
            head=head.next
         return dummy.next


'''
第二题：加一（可以直接查看链接）
https://leetcode-cn.com/problems/plus-one/submissions/
'''
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        for i in range(n, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            elif digits[i] < 9:
                digits[i] += 1
                return digits
        return [1] + digits


















