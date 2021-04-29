import unittest
from DataStructure import DataStructure

class TestDataEstructure(unittest.TestCase):

    def setUp(self):
        self.data_structure = DataStructure(1)

    def test_put_get_method(self):
        #data_structure = DataStructure(1)
        data_structure.put_element("0")
        obtained_node = data_structure.get_element(0)
        self.assertEqual(obtained_node, "0")

    def test_put_get_method_2(self):
        #data_structure = DataStructure(1)
        data_structure.put_element(10)
        obtained_node = data_structure.get_element(0)
        self.assertEqual(obtained_node, 10)

    def test_put_get_method_3(self):
        #data_structure = DataStructure(1)
        data_structure.put_element([1, 2, 3])
        obtained_node = data_structure.get_element(0)
        self.assertEqual(obtained_node, [1, 2, 3])

    def test_get_method_in_position(self):
        data_structure = DataStructure(4)
        for i in range(4):
            data_structure.put_element(i)
        obtained_node = data_structure.get_element(3)
        self.assertEqual(obtained_node, 3)

    def test_put_get_methods_stress(self):
        data_structure = DataStructure(5000)
        for i in range(10000):
            data_structure.put_element(i)
        obtained_node = data_structure.get_element(9999)
        self.assertEqual(obtained_node, 9999)

    def test_get_key_not_in_range(self):
        data_structure = DataStructure(1)
        data_structure.put_element("0")
        obtained_node = data_structure.get_element(50)
        self.assertEqual(obtained_node, None)

if __name__ == '__main__':
    unittest.main()