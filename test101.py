
class ListNode(object):
  def __init__(self, x, nxt = None):
    # print(x)
    self.value = x
    # self.next = None
    self.next = nxt

# def insertValueIntoSortedLinkedList(l, value):
#     return f'Node({repr(self.value)})'
    

head = ListNode(45)
o = ListNode(88)
head.next = o
print(head.value)
print(head.next.value)
# print([1, 3, 4, 6], 5)
# head = ListNode(45)
# o = ListNode(88)
# head.next = o
# print(head.value)
# print(o)
# print(head.next)
# o= ListNode(88)
# p = ListNode(2)
