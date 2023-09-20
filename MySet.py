from linked_list import LinkedList, T
from typing import TypeVar, Generic, Optional, Callable, Type


class MySet(Generic[T]):

    def __init__(self, llist: Optional['LinkedList[T]'] = None):
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
        return self.__my_set[index]

    def __len__(self) -> int:
        return self.__length

    def __str__(self) -> str:
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

    def union(self, my_set_1: 'MySet') -> 'MySet':
        temp = MySet(self.__my_set.copy())
        temp_1 = MySet(my_set_1.copy())
        if len(temp_1) >= len(temp):
            for i in range(len(temp_1)):
                if temp_1[i] not in temp:
                    temp.add(temp_1[i])
            return temp


        else:
            for j in range(len(temp)):
                if temp not in temp_1:
                    temp_1.add(temp[j])
            temp = temp_1
            return temp

    def copy(self) -> 'LinkedList':
        return self.__my_set.copy()

    def intersect(self, my_set_1: 'MySet') -> "MySet":
        temp = MySet(self.__my_set.copy())
        temp_1 = MySet(my_set_1.copy())
        if len(temp_1) >= len(temp):
            my_set_2 = MySet()
            for i in range(len(temp_1)):
                if temp_1[i] in temp:
                    my_set_2.add(my_set_1[i])
            temp = my_set_2
            return temp
        else:
            my_set_2 = MySet()
            for i in range(len(temp)):
                if temp[i] in temp_1:
                    my_set_2.add(temp[i])
            temp = my_set_2
            return temp

    def find_bin(self, value: T) -> T:
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

    def __contains__(self, value: T) -> bool:
        for i in range(len(self.__my_set)):
            if self.__my_set[i] == value:
                return True
        else:
            return False
