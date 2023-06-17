class ringQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.tail = -1
        self.head = 0
        self.size = 0

    def enqueue_code(self, code_char):
        if self.size == self.capacity:
            print("No more character is allowed")
        
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = code_char
            self.size = self.size + 1

    def dequeue_code(self):
        if self.size == 0:
            print("No character found")
            return
        
        else:
            tmp =  self.queue[self.head]
            self.head = (self.head + 1) % self.capacity

        self.size = self.size - 1
        return tmp
    
    def dashboard(self):

        if self.size == 0:
            print("Queue is Empty \n")

        else:
            index = self.head

            for i in range(self.size):
                print(self.queue[index])
                index = (index + 1) % self.capacity

    

    def isFull(self):
        return True if self.size == self.capacity else False
        
    def isEmpty(self):
        return True if self.size == 0 else False
    
    def peek_codes(self):
        print (self.queue[self.head])
        return self.queue[self.head]
    
    def decide_circular(self,code_char):
        if self.isFull():
            self.dequeue_code()
        else:
            self.enqueue_code(code_char)
            self.dashboard()





