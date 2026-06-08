# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head

        while curr:
            temp= curr.next # 2nd node's address
            curr.next=prev # here reversed i.e first node.next = None hogya

            prev = curr  # pehly prev = None tha ab prev = node1 (object) hojyga

            curr = temp # here pehly jo curr = head tha ab wo curr = node2 hojyga

        return prev
        
        