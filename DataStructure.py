from Node import Node
from multipledispatch import dispatch

class DataStructure:


    def __init__(self, size):
        self.size = size
        self.last_element = None
        self.first_element = None
        self.elements_contained = 0
        self.next_key = 0
    
    @dispatch(object)
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
            self.delete_oldest_element()

    @dispatch(Node)
    def put_element(self, node: Node):
        #backup node used to assign its next and previous nodes if the key already existed
        node_backup =self.get_element(node.get_key())
        if node_backup is not None:
            if node.get_key() != self.first_element.get_key():
                node_backup.previous_node.next_node = node_backup.next_node
            else:
                self.first_element = node_backup.next_node
                self.first_element.previous_node = None
            node_backup.next_node.previous_node = node_backup.previous_node
            node.previous_node = self.last_element
            self.last_element.next_node= node
            self.last_element = node
        else:
            node.previous_node = self.last_element
            self.last_element.next_node= node
            self.last_element = node
            self.elements_contained += 1
            if self.elements_contained > self.size:
                self.delete_oldest_element()
    
    def delete_oldest_element(self):
        self.first_element = self.first_element.next_node
        self.first_element.previous = None
        self.elements_contained -= 1

    def print_list(self):
        node = self.first_element
        while (node is not None):
            print(node, end =" "),
            node = node.next_node
    
    def get_element(self, key):
        node = self.first_element
        while (node is not None):
            if (node.get_key()==key):
                return node
            else:
                node = node.next_node
        return None


