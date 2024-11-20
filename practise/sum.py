class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class MySolution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode()
        cur = ret
        carry = 0
        while (l1 or l2):
            # 计算 l1 的值和 l2 的值
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum = l1_val + l2_val + carry
            # 计算进位
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None
        if carry == 1:
            cur.next = ListNode(1)
        return ret.next

# test
s = MySolution()
l1 = ListNode(4)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(6)
ret = s.addTwoNumbers(l1, l2)

r = []
while ret:
    r.append(ret.val)
    ret = ret.next

print(r)