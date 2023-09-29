import typing

T = typing.TypeVar('T')


class Stack(typing.Generic[T]):
    class __Node(typing.Generic[T]):

        def __init__(self, element: T = None, next_node: typing.Optional['Stack[T]'] = None):
            self.element: T = element
            self.next_node: typing.Optional['Stack[T]'] = next_node

    def __init__(self):
        self.__head = None
        self.__length = 0

    def __str__(self) -> str:
        if self.__length == 0:
            return '[]'
        else:
            node = self.__head
            stack_string = '['
            while node.next_node:
                stack_string += f' {node.element},'
                node = node.next_node
            stack_string += f' {node.element} ]'
            return stack_string

    def __len__(self) -> int:
        return self.__length

    def __add__(self, other: 'Stack') -> 'Stack':
        temp = Stack()
        node = self.__head
        counter = 0
        while node:
            temp.__append(node.element)
            node = node.next_node
            counter += 1

        for i in range(len(other)):
            temp.__append(other.__get_elem(i))

        return temp

    def __lt__(self, other: 'Stack') -> bool:
        if self.__length < len(other):
            return True
        else:
            return False

    def __le__(self, other: 'Stack') -> bool:
        if self.__length <= len(other):
            return True
        else:
            return False

    def __eq__(self, other: 'Stack') -> bool:
        if self.__length == len(other):
            return True
        else:
            return False

    def __ne__(self, other: 'Stack') -> bool:
        if self.__length != len(other):
            return True
        else:
            return False

    def __gt__(self, other: 'Stack') -> bool:
        if self.__length > len(other):
            return True
        else:
            return False

    def __ge__(self, other: 'Stack') -> bool:
        if self.__length >= len(other):
            return True
        else:
            return False

    def __append(self, element: T) -> None:

        if not self.__head:
            self.__head = self.__Node(element)

        else:
            node = self.__head

            while node.next_node:
                node = node.next_node

            node.next_node = self.__Node(element)

        self.__length += 1

    def __get_elem(self, index: int) -> T:
        node = self.__head
        counter = 0
        while node:
            if counter == index:
                return node.element
            node = node.next_node
            counter += 1

    def append(self, data) -> None:
        self.__head = self.__Node(data, next_node=self.__head)
        self.__length += 1

    def pop(self) -> None:
        temp = self.__head
        self.__head = temp.next_node
        del temp
        self.__length -= 1

    def title_up(self) -> T:
        return self.__head.element

    def title_down(self) -> T:
        node = self.__head
        counter = 0
        while node:
            if counter == self.__length - 1:
                return node.element
            node = node.next_node
            counter += 1
