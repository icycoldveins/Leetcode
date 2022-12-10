""" 
You are given two non-empty linked lists 
representing two non-negative integers. 
The digits are stored in reverse order, 
and each of their nodes contains a single 
digit. Add the two numbers and return the sum 
as a linked list.
You may assume the 
two numbers do not contain any leading 
zero, except the number 0 itself.


 """

""" 
 two non empty linked list representing non negative int
 reverse order
 nodes contain a single digit
 add the two numbers and return sum as a linked list 

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# give explanation
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # self.l1 = l1
        # self.l2 = l2
        # self.l3 = l3
        l3 = ListNode(0)
        curr = l3
        carry = 0
        while l1 or l2 or carry:
            # if 
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
        return l3.next
