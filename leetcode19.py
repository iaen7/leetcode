def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if head == None:
        return
    node = head
    Count = 1
    while node.next != None:
        Count += 1
        node = node.next
    PlusNo = Count - n
    if PlusNo < 0:
        return 
    elif PlusNo == 0:
        head = head.next
    else:
        node = head
        for i in range(0,PlusNo-1):
            node = node.next
        node.next = node.next.next
    return head

nums = [1,2]
print removeNthFromEnd(nums,1)
