    def insert(self,head,data): 
        node = Node(data)

        current = head
        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            head = node
        return head