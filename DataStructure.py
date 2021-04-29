from Node import Node



class DataStructure:


    def __init__(self, size):
        self.size = size
        self.last_element = None
        self.first_element = None
        self.elements_contained = 0
        self.next_key = 0
    
    def put_element(self, element):    
        added_node = Node(self.next_key, element)
        self.next_key += 1
        if self.first_element == None:
            self.first_element = added_node
            self.last_element = added_node
        else:
            self.last_element.next_node = added_node
            added_node.previous_node = self.last_element
            self.last_element = added_node
        self.elements_contained += 1
        if self.elements_contained > self.size:
            self.first_element = self.first_element.next_node
            self.first_element.previous = None
            self.elements_contained -= 1
    
    def print_list(self):
        node = self.first_element
        while (node is not None):
            print(node, end =" "),
            last = node
            node = node.next_node
    
    def get_element(self, key):
        if self.first_element.get_key() <= key <= self.next_key:
            node = self.first_element
            for i in range(self.first_element.get_key(), key+1):
                if node.get_key() == key:
                    print(node)
                    return node.content
                else:
                    node = node.next_node
            print("Key not found")
            return None
        else:
            print("Key is not inside this list")
            return None
            


