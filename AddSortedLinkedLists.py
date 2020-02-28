# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = currList = ListNode(None)
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry, remainder = divmod(val1 + val2 + carry, 10)  # here carry is the quotient
            currList.next = ListNode(remainder)
            currList = currList.next
        return root.next
