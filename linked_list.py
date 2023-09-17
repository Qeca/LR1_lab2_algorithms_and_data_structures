class LinkedList:

    class __Node:

        def __init__(self, element=None, next_node=None) -> None:
            self.element = element
            self.next_node = next_node


    def __init__(self) -> None:
        self.__head = None
        self.__length = 0


    def append(self, element) -> None:

        if not self.__head:
            self.__head = self.__Node(element)

        else:
            node = self.__head

            while node.next_node:
                node = node.next_node

            node.next_node = self.__Node(element)

        self.__length += 1


    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Вставка по отрицательному индексу не предусмотрена")
        elif index >= self.__length:
            raise IndexError("Выход за границы списка")
        node = self.__head
        counter = 0
        while node:
            if counter == index:
                return node.element
            node = node.next_node
            counter += 1

        self.__length += 1

    def __repr__(self):
        if self.__length == 0:
            return '[]'
        else:
            node = self.__head
            llist_string = '['
            while node.next_node:
                llist_string += f'{node.element},'
                node = node.next_node
            llist_string += f'{node.element}]'
            return llist_string

    def insert(self,index,element: int):
        if index < 0:
            raise IndexError("Вставка по отрицательному индексу не предусмотрена")
        elif index > self.__length + 1:
            raise IndexError("Выход за границы списка")
        if index == 0:
            self.push_front(element)
            return element
        else:
            i = 0
            node = self.__head
            prev_node = self.__head
            while i <= index:
                prev_node = node
                node = node.next_node
                i += 1
            prev_node.next_node = self.__Node(element, next_node=node)
            self.__length += 1
            return element

    def get_elem(self,index):
        if index < 0:
            raise IndexError("Получение элемента по отрицательному индексу не предусмотрено")
        elif index > self.__length + 1:
            raise IndexError("Выход за границы списка")
        i = 0
        node = self.__head
        prev_node = self.__head
        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        return node.element

    def __len__(self):
        return self.__length

    def pop(self, index):
        if index < 0:
            raise IndexError("Удаление по отрицательному индексу не предусмотрено")
        elif index > self.__length + 1:
            raise IndexError("Выход за границы списка")
        if index == 0:
            self.__head = self.__head.next_node

        node = self.__head
        i = 0
        prev_node = node
        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = node.next_node
        element = node.element

        del node

        self.__length -= 1
        return element

    def pop_front(self):
        temp = self.__head
        self.__head = temp.next_node
        del temp
        self.__length -= 1

    def clear(self):
        while self.__length:
            self.pop_front()


    def push_front(self, data):
        self.__head = self.__Node(data, next_node=self.__head)
        self.__length += 1


llist = LinkedList()
