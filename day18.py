class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
    def pushCharacter(self, temp):
        self.stack.append(temp)
    def popCharacter(self):
        temp = self.stack.pop()
        return temp
    def enqueueCharacter(self, temp):
        self.queue.append(temp)
    def dequeueCharacter(self):
        temp = self.queue.pop(0)
        return temp