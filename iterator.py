class FlatIterator():

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.needed_list = []
        self.counter = 0
        while self.counter < len(self.list_of_list):
            self.needed_list += self.list_of_list[self.counter]
            self.counter += 1
        self.counter1 = 0
        return self

    def __next__(self):
        if self.counter1 >= len(self.needed_list):
            raise StopIteration
        else:
            element = self.needed_list[self.counter1]
            self.counter1 += 1
        return element
