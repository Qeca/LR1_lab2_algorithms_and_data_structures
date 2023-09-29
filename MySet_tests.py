import unittest
from MySet import MySet
from linked_list import LinkedList


class MySetTests(unittest.TestCase):
    def test_init(self):
        llist = LinkedList()
        for i in range(5):
            llist.append(i)
        my_set = MySet()
        self.assertEqual(f'{my_set}', '{}')
        my_set = MySet(llist)
        self.assertEqual(f'{my_set}', '{0,1,2,3,4}')

    def test_add_and_print(self):
        my_set = MySet()
        for i in range(5):
            my_set.add(i)
        self.assertEqual(f'{my_set}', '{0,1,2,3,4}')

    def test_union(self):
        my_set = MySet()
        my_set1 = MySet()
        for i in range(5):
            my_set.add(i)
        for i in range(6, 10):
            my_set1.add(i)
        self.assertEqual(f'{my_set.union(my_set1)}', '{6,7,8,9,0,1,2,3,4}')

    def test_intersect(self):
        my_set = MySet()
        my_set1 = MySet()
        for i in range(5):
            my_set.add(i)
        for i in range(3, 10):
            my_set1.add(i)
        self.assertEqual(f'{my_set.intersect(my_set1)}', '{3,4}')

    def test_find_bin(self):
        my_set = MySet()
        for i in range(5):
            my_set.add(i)
        self.assertEqual(f'{my_set.find_bin(2)}','2')

    def test_contains(self):
        my_set = MySet()
        for i in range(5):
            my_set.add(i)
        self.assertEqual(2 in my_set,True)

    def test_remove(self):
        my_set = MySet()
        for i in range(5):
            my_set.add(i)
        my_set.remove(3)
        self.assertEqual(f"{my_set}",'{0,1,2,4}')

if __name__ == '__main__':
    unittest.main()
