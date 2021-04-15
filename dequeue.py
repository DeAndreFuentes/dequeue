#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2=[]
 
    
 
    def enqueue(self, data):
        self.stack1.append(data)
 
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


q = Queue()
q.enqueue("First")
q.enqueue("Second")
q.enqueue("Third")
print(q.dequeue())
print(q.dequeue())


# In[ ]:




