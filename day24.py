    def removeDuplicates(self,head):
        #Write your code here
        current = head
        num = current.data
        while current.next is not None:
            if current.next.data == num:
                current.next = current.next.next
            else:
                current = current.next
                num = current.data
        return head