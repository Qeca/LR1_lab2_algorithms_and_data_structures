import unittest
from linked_list import LinkedList

class TestLinked_list(unittest.TestCase):

    def test_init(self):
        llist = LinkedList()
        self.assertEqual(f'{llist}','[]')

    def test_llist_int(self):
        llist = LinkedList()
        for i in range(1, 11):
            llist.append(i)
        self.assertEqual(f'{llist}', '[1,2,3,4,5,6,7,8,9,10]')

    def test_llist_str(self):
        llist = LinkedList()
        for i in ['one','two','three','four','five','six','seven','eight','nine','ten']:
            llist.append(i)
        self.assertEqual(f'{llist}', "[one,two,three,four,five,six,seven,eight,nine,ten]")

    def test_insert(self):
        llist = LinkedList()
        for i in range(1, 6):
            llist.append(i)
        llist.insert(0,55)
        self.assertEqual(f'{llist}', '[55,1,2,3,4,5]')
        llist.insert(3,55)
        self.assertEqual(f'{llist}','[55,1,2,3,55,4,5]')
        llist.insert(len(llist) -1,55)
        self.assertEqual(f'{llist}','[55,1,2,3,55,4,5,55]')

if __name__ == '__main__':
    unittest.main()
