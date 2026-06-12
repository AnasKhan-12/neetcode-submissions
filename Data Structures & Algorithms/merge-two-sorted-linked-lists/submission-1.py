# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we will create a dummy node with value 0 at the and after sorting we will eliminate this node

        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:

            if list1.val < list2.val: #at first i did only list<list2 which is wrong beaware
               
                curr.next= list1  #curr.next stores the address of the node 2 or other words stores the address of node 2 which is a object

                # now change list1 to the next node in the list else loop will terminate
                list1 = list1.next

            # what if list2 is smaller than list1

            else:
                curr.next = list2 # we set the .next of dummy node to list2 if its smaller than list1

                # list2's first node sorted....now update list2 as you did in if block

                list2 = list2.next

            # now as curr is pointing to first node we need to update it make it first node and make it point to second (which going to come after second iteration of while loop)
            # this is also in inside loop

            curr=curr.next

        # the loop stops when one list gets completed and last node is pointing to None
        # so if the other list is still remaining we attach it to our new list
        # if list1.next=None while loop exits and below condition returns list2 and curr.next points to list2 then

        curr.next = list1 or list2
        return dummy.next








