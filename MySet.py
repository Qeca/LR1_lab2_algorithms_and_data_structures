from linked_list import LinkedList, T, LL
import typing

MS = typing.TypeVar('MySet')
F = typing.TypeVar('F', int, bool)


class MySet:
    def __init__(self, llist=None):
        if llist == None:
            self.__llist = LinkedList()
            i = 0
            j = len(self.__llist)
            while i < j - 1:
                if self.__llist[i] == self.__llist[i + 1]:
                    self.__llist.pop(i)
                    j -= 1
                    if i > 0:
                        i -= 1
                else:
                    i += 1
        else:
            self.__llist = llist
            i = 0
            j = len(self.__llist)
            while i < j - 1:
                if self.__llist[i] == self.__llist[i + 1]:
                    self.__llist.pop(i)
                    j -= 1
                    if i > 0:
                        i -= 1
                else:
                    i += 1
        self.__my_set = self.__llist
        self.__length = len(self.__llist)

    def __getitem__(self, index: int) -> T:
        for i in range(len(self.__my_set)):
            if i == index:
                return self.__my_set[i]

    def __len__(self) -> int:
        return self.__length

    def __repr__(self) -> str:
        if self.__length == 0:
            return '{}'
        else:
            k = '{'
            for i in range(self.__length - 1):
                k += f'{self.__my_set[i]},'
            k += f'{self.__my_set[self.__length - 1]}' + '}'
        return k

    def add(self, data: T) -> None:
        if data not in self.__my_set:
            self.__my_set.append(data)
            self.__length += 1

    def pop(self, index: int) -> T:
        self.__length -= 1
        return self.__my_set.pop(index)

    def union(self, my_set_1: MS) -> None:
        my_set_2 = MySet()
        if len(my_set_1) >= len(self.__my_set):
            for i in range(len(my_set_1)):
                if my_set_1[i] not in self.__my_set:
                    self.__my_set.append(my_set_1[i])
                    self.__length += 1

        else:
            for j in range(self.__length):
                if self.__my_set[j] not in my_set_1:
                    my_set_1.append(self.__my_set[j])
                    self.__length += 1
            self.__my_set = my_set_1

    def intersect(self, my_set_1: MS) -> None:
        if len(my_set_1) >= len(self.__my_set):
            my_set_2 = MySet()
            for i in range(len(my_set_1)):
                if my_set_1[i] in self.__my_set:
                    my_set_2.add(my_set_1[i])
            self.__my_set = my_set_2
            self.__length = len(my_set_2)
        else:
            my_set_2 = MySet()
            for i in range(len(self.__my_set)):
                if self.__my_set[i] in my_set_1:
                    my_set_2.add(self.__my_set[i])
            self.__my_set = my_set_2
            self.__length = len(my_set_2)

    def find_bin(self, value: T) -> F:
        mid = len(self.__my_set) // 2
        low = 0
        high = len(self.__my_set) - 1

        while self.__my_set[mid] != value and low <= high:
            if value > self.__my_set[mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        if low > high:
            return False
        else:
            return mid
    def find(self, value: T) -> F:

        for i in range(len(self.__my_set)):
            if self.__my_set[i] == value:
                return i
        else:
            return False
