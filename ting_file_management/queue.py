class Queue:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        first_value = self.data[0]
        self.data = self.data[1:]
        return first_value

    def search(self, index):
        if type(index) is not int or index >= len(self.data) or index < 0:
            raise IndexError
        return self.data[index]