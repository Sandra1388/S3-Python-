'''
You are given the head of a linked list,
which contains a series of integers separated by 0's.
The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in
between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeNodes(self, head):

        dummy = ListNode(0)
        tail = dummy

        current = head.next      # Skip the first 0
        total = 0

        while current:

            if current.val == 0:
                tail.next = ListNode(total)
                tail = tail.next
                total = 0
            else:
                total += current.val

            current = current.next

        return dummy.next
