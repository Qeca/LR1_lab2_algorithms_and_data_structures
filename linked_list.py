class LinkedList:

    class __Node:

        def __init__(self, element=None, next_node=None) -> None:
            self.element = element
            self.next_node = next_node


    def __init__(self, head=None, length=0) -> None:
        if head != None and length != 0:
            raise ValueError("В инициализатор не суй ничего")
        self.__head = head
        self.__length = length



    def append(self, element) -> None:
        if not self.__head:
            self.__head = self.__Node(element)
            return element
        node = self.__head

        while node.next_node:
            node = node.next_node

        node.next_node = self.__Node(element)
        self.__length += 1

    @property
    def out(self) -> str:
        node = self.__head
        llist_string = '['
        while node.next_node:
            llist_string += f'{node.element},'
            node = node.next_node
        llist_string += f'{node.element}]'
        return llist_string

    def insert(self,element,index: int):
        if index < 0:
            raise IndexError("Вставка по отрицательному индексу не предусмотрена")
        elif index > self.__length:
            raise IndexError("Выход за границы списка")
        i = 0
        node = self.__head
        while i < index:
            prev_node = node
            node = node.next_node
            i += 1
        prev_node.next_node = self.__Node(element, next_node=node)
        self.__length += 1
        return element

    def get_elem(self,index):
        if index < 0:
            raise IndexError("Получение элемента по отрицательному индексу не предусмотрено")
        elif index > self.__length:
            raise IndexError("Выход за границы списка")
        i = 0
        node = self.__head
        prev_node = self.__head
        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        return node.element

    def size(self) -> int:
        return self.__length + 1

    def delete(self, index):
        if index < 0:
            raise IndexError("Удаление по отрицательному индексу не предусмотрено")
        elif index > self.__length:
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


llist = LinkedList()

