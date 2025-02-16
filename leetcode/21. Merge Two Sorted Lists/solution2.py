# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return None

        result_list = []
        while list1 or list2:
            if list1 is None and list2 is not None:
                result_list.append(list2.val)
                list2 = list2.next
            elif list1 is not None and list2 is None:
                result_list.append(list1.val)
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    result_list.append(list1.val)
                    list1 = list1.next
                else:
                    result_list.append(list2.val)
                    list2 = list2.next

        # print(result_list)
        next_node = ListNode(result_list[-1], None)
        for i in result_list[-2::-1]:
            result_linked_list = ListNode(i, next_node)
            next_node = result_linked_list
        return result_linked_list
