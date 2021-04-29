class Node:
    def __init__(self, key, content):
        self.__key = key
        self.content = content
        self.next_node = None
        self.previous_node = None
    
    def __str__(self):
        return str(self.content)

    def get_key(self):
        return self.__key