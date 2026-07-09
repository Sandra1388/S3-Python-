'''
Given the head of a singly linked list,
return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        c = 0
        current = head
        while current is not None:
            c += 1
            current = current.next
        mid = (0+c) // 2
        
        current = head
        for i in range(mid):
            current = current.next

        return current
