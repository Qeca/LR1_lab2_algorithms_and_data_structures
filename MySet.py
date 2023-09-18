from linked_list import LinkedList

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


    def __getitem__(self, index):
        for i in range(len(self.__my_set)):
            if i == index:
                return self.__my_set[i]

    def __len__(self):
        return self.__length

    def __repr__(self):
        if self.__length == 0:
            return '{}'
        else:
            k = '{'
            for i in range(self.__length-1):
                k += f'{self.__my_set[i]},'
            k += f'{self.__my_set[self.__length-1]}' + '}'
        return k

    def add(self, data):
        if data not in self.__my_set:
            self.__my_set.append(data)
            self.__length += 1

    def pop(self,index):
        self.__length -= 1
        return self.__my_set.pop(index)

    def union(self, my_set_1: LinkedList):
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















