import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_init(self):
        llist = LinkedList()
        self.assertEqual(f'{llist}', '[]')

    def test_append_and_repr_int(self):
        llist = LinkedList()
        for i in range(1, 11):
            llist.append(i)
        self.assertEqual(f'{llist}', '[1,2,3,4,5,6,7,8,9,10]')

    def test_append_and_repr_str(self):
        llist = LinkedList()
        for i in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']:
            llist.append(i)
        self.assertEqual(f'{llist}', "[one,two,three,four,five,six,seven,eight,nine,ten]")

    def test_insert(self):
        llist = LinkedList()
        for i in range(1, 6):
            llist.append(i)
        llist.insert(0, 55)
        self.assertEqual(f'{llist}', '[55,1,2,3,4,5]')
        llist.insert(3, 55)
        self.assertEqual(f'{llist}', '[55,1,2,3,55,4,5]')
        llist.insert(len(llist) - 1, 55)
        self.assertEqual(f'{llist}', '[55,1,2,3,55,4,5,55]')

    def test_getitem(self):
        llist = LinkedList()
        for i in range(11):
            llist.append(i)
        self.assertEqual(llist[0], 0)
        self.assertEqual(llist[1], 1)
        self.assertEqual(llist[10], 10)

    def test_setitem(self):
        llist = LinkedList()
        for i in range(1, 4):
            llist.append(i)
        llist[0] = 100
        self.assertEqual(f'{llist}', '[100,2,3]')

    def test_get_elem(self):
        llist = LinkedList()
        for i in range(11):
            llist.append(i)
        self.assertEqual(llist.get_elem(2), 2)
        self.assertEqual(llist.get_elem(3), 3)
        self.assertEqual(llist.get_elem(4), 4)
        self.assertEqual(llist.get_elem(5), 5)

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

    def test_pop_front(self):
        llist = LinkedList()
        for i in range(11):
            llist.append(i)
        llist.pop_front()
        self.assertEqual(f'{llist}', '[1,2,3,4,5,6,7,8,9,10]')

    def test_clear(self):
        llist = LinkedList()

        for i in range(11):
            llist.append(i)
        self.assertEqual(f'{llist}', '[0,1,2,3,4,5,6,7,8,9,10]')
        llist.clear()
        self.assertEqual(f'{llist}', '[]')

    def test_push_front(self):
        llist = LinkedList()

        for i in range(11):
            llist.append(i)
        llist.push_front(55)
        self.assertEqual(f'{llist}', '[55,0,1,2,3,4,5,6,7,8,9,10]')


if __name__ == '__main__':
    unittest.main()
