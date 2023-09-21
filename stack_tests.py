import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_str_and_append(self):
        stack = Stack()
        stack.append('Евгений Онегин')
        stack.append("Вий")
        stack.append('Война и мир')
        stack.append('Сто лет одиночества')
        stack.append('Полковнику никто не пишет')
        self.assertEqual(f'{stack}',
                         '[ Полковнику никто не пишет, Сто лет одиночества, Война и мир, Вий, Евгений Онегин ]')  # add assertion here

    def test_len(self):
        stack = Stack()
        stack.append('Евгений Онегин')
        stack.append("Вий")
        stack.append('Война и мир')
        stack.append('Сто лет одиночества')
        stack.append('Полковнику никто не пишет')
        self.assertEqual(len(stack), 5)

    def test_add(self):
        stack = Stack()
        stack.append('Евгений Онегин')
        stack.append("Вий")
        stack_1 = Stack()
        stack_1.append('Война и мир')
        stack_1.append('Сто лет одиночества')
        stack_1.append('Полковнику никто не пишет')
        self.assertEqual(f'{stack + stack_1}',
                         '[ Вий, Евгений Онегин, Полковнику никто не пишет, Сто лет одиночества, Война и мир ]')

    def test_comparisons(self):
        stack = Stack()
        stack.append('Евгений Онегин')
        stack.append("Вий")
        stack_1 = Stack()
        stack_1.append('Война и мир')
        stack_1.append('Сто лет одиночества')
        stack_1.append('Полковнику никто не пишет')
        self.assertEqual(stack > stack_1,False)
        self.assertEqual(stack < stack_1, True)
        self.assertEqual(stack == stack_1, False)
        self.assertEqual(stack != stack_1, True)
        self.assertEqual(stack <= stack_1, True)
        self.assertEqual(stack >= stack_1,False)

    def test_pop(self):
        stack = Stack()
        stack.append('Евгений Онегин')
        stack.append("Вий")
        stack.append('Война и мир')
        stack.append('Сто лет одиночества')
        stack.append('Полковнику никто не пишет')
        stack.pop()
        self.assertEqual(f'{stack}', '[ Сто лет одиночества, Война и мир, Вий, Евгений Онегин ]')

    def test_title_up(self):
        stack = Stack()
        stack.append('Евгений Онегин')
        stack.append("Вий")
        stack.append('Война и мир')
        stack.append('Сто лет одиночества')
        stack.append('Полковнику никто не пишет')
        self.assertEqual(f'{stack.title_up()}', 'Полковнику никто не пишет')

    def test_title_down(self):
        stack = Stack()
        stack.append('Евгений Онегин')
        stack.append("Вий")
        stack.append('Война и мир')
        stack.append('Сто лет одиночества')
        stack.append('Полковнику никто не пишет')
        self.assertEqual(f'{stack.title_down()}','Евгений Онегин')


if __name__ == '__main__':
    unittest.main()
