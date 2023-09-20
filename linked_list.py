from typing import TypeVar, Generic, Optional, Callable, Type

T = TypeVar('T')


class LinkedList(Generic[T]):
    class __Node(Generic[T]):

        def __init__(self, element: T = None, next_node: Optional['LinkedList[T]'] = None):
            self.element: T = element
            self.next_node: Optional['LinkedList[T]'] = next_node

    def __init__(self):
        self.__head = None
        self.__length = 0

    def append(self, element: T) -> None:

        if not self.__head:
            self.__head = self.__Node(element)

        else:
            node = self.__head

            while node.next_node:
                node = node.next_node

            node.next_node = self.__Node[T](element)

        self.__length += 1

    def __getitem__(self, index: int) -> None:
        if index < 0:
            raise IndexError("Вставка по отрицательному индексу не предусмотрена")
        elif index > self.__length:
            raise IndexError("Выход за границы списка")
        node = self.__head
        counter = 0
        while node:
            if counter == index:
                return node.element
            node = node.next_node
            counter += 1

    def copy(self) -> 'LinkedList':
        temp = LinkedList()
        node = self.__head
        counter = 0
        while node:
            temp.append(node.element)
            node = node.next_node
            counter += 1
        return temp

    def __str__(self) -> str:
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

    def insert(self, index: int, element: T) -> T:
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

    def get_elem(self, index: int) -> T:
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

    def __len__(self) -> int:
        return self.__length

    def pop(self, index: int) -> T:
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

    def pop_front(self) -> None:
        temp = self.__head
        self.__head = temp.next_node
        del temp
        self.__length -= 1

    def clear(self) -> None:
        while self.__length:
            self.pop_front()

    def push_front(self, data: T) -> None:
        self.__head = self.__Node[T](data, next_node=self.__head)
        self.__length += 1

    def __setitem__(self, index: int, value: T) -> None:
        if index < 0:
            raise IndexError("Вставка по отрицательному индексу не предусмотрена")
        elif index >= self.__length:
            raise IndexError("Выход за границы списка")
        node = self.__head
        counter = 0
        while node:
            if counter == index:
                node.element = value
            node = node.next_node
            counter += 1

        self.__length += 1
