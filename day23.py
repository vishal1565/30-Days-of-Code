    def levelOrder(self,root):
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            print(node.data, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)