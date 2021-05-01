import unittest
from DataStructure import DataStructure
from Node import Node

class TestDataEstructure(unittest.TestCase):

    def setUp(self):
        self.single_data_structure = DataStructure(1)
        self.multiple_data_structure = DataStructure(4)
        for i in range(4):
            self.multiple_data_structure.put_element(i)
        self.very_big_data_structure = DataStructure(5000)

    def test_put_get_method(self):
        self.single_data_structure.put_element("0")
        obtained_node = self.single_data_structure.get_element(0)
        self.assertEqual(obtained_node.content, "0")

    def test_put_get_method_2(self):
        self.single_data_structure.put_element(10)
        obtained_node = self.single_data_structure.get_element(0)
        self.assertEqual(obtained_node.content, 10)

    def test_put_get_method_3(self):
        self.single_data_structure.put_element([1, 2, 3])
        obtained_node = self.single_data_structure.get_element(0)
        self.assertEqual(obtained_node.content, [1, 2, 3])

    def test_put_get_method_4(self):
        self.single_data_structure.put_element(None)
        obtained_node = self.single_data_structure.get_element(0)
        self.assertEqual(obtained_node.content, None)

    def test_get_key_not_in_structure(self):
        self.single_data_structure.put_element("0")
        obtained_node = self.single_data_structure.get_element(50)
        self.assertEqual(obtained_node, None)

    def test_get_method_multiple_keys(self):
        obtained_node = self.multiple_data_structure.get_element(3)
        self.assertEqual(obtained_node.content, 3)

    def test_first_node_reinserted(self):
        inserted_node = Node(0, 0)
        self.multiple_data_structure.put_element(inserted_node)
        obtained_node = self.multiple_data_structure.get_element(0)
        expected_previous_node = self.multiple_data_structure.get_element(3)
        self.assertEqual(obtained_node.previous_node, expected_previous_node)

    def test_third_node_reinserted(self):
        inserted_node = Node(2, 2)
        self.multiple_data_structure.put_element(inserted_node)
        obtained_node = self.multiple_data_structure.get_element(2)
        expected_previous_node = self.multiple_data_structure.get_element(3)
        self.assertEqual(obtained_node.previous_node, expected_previous_node)
    
    def test_foreign_node_inserted(self):
        inserted_node = Node('a', 'a')
        self.multiple_data_structure.put_element(inserted_node)
        obtained_node = self.multiple_data_structure.get_element('a')
        self.assertEqual(obtained_node.content, 'a')

    def test_put_get_methods_stress(self):
        for i in range(10000):
            self.very_big_data_structure.put_element(i)
        obtained_node = self.very_big_data_structure.get_element(9999)
        self.assertEqual(obtained_node.content, 9999)

if __name__ == '__main__':
    unittest.main()