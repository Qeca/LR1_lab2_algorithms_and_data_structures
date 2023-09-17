class LinkedList:

    class Node:

        def __init__(self, element=None, next_node=None):
            self.element = element
            self.next_node = next_node

    def __init__(self, __head = None):
        self.__head = __head

    def append(self, element):
        if not self.__head:
            self.__head = self.Node(element)
            return element
        node = self.__head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

    @property
    def out(self) -> str:
        node = self.__head
        llist_string = '['
        while node.next_node:
            llist_string += f'{node.element},'
            node = node.next_node
        llist_string += f'{node.element}]'
        return llist_string


llist = LinkedList()

llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
print(llist.out)