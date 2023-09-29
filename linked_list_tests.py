import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_init(self):
        llist = LinkedList()
        self.assertEqual(f'{llist}', '[]')

    def test_append_and_str_int(self):
        llist = LinkedList()
        for i in range(1, 11):
            llist.append(i)
        self.assertEqual(f'{llist}', '[1,2,3,4,5,6,7,8,9,10]')

    def test_append_and_str_str(self):
        llist = LinkedList()
        for i in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']:
            llist.append(i)
        self.assertEqual(f'{llist}', "[one,two,three,four,five,six,seven,eight,nine,ten]")

    def test_setitem(self):
        llist = LinkedList()
        for i in range(1, 4):
            llist.append(i)
        llist[0] = 100
        self.assertEqual(f'{llist}', '[100,2,3]')

    def test_len(self):
        llist = LinkedList()
        for i in range(11):
            llist.append(i)
        llist1 = LinkedList()
        for i in range(16):
            llist1.append(i)
        llist2 = LinkedList()
        for i in range(25):
            llist2.append(i)
        self.assertEqual(len(llist), 11)
        self.assertEqual(len(llist1), 16)
        self.assertEqual(len(llist2), 25)

    def test_pop(self):
        llist = LinkedList()
        for i in range(11):
            llist.append(i)
        llist.pop(3)
        self.assertEqual(f'{llist}', '[0,1,2,4,5,6,7,8,9,10]')

    def test_copy(self):
        l = LinkedList()
        for i in range(11):
            l.append(i)
        l_1 = l.copy()
        self.assertEqual(f'{l_1}', f'{l}')


if __name__ == '__main__':
    unittest.main()
