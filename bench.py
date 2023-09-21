import timeit
import time

from linked_list import LinkedList
from MySet import MySet
llist = LinkedList()


for i in range(1,10000+1):
    llist.append(i)
start_time = timeit.default_timer()
my_set = MySet(llist)
print(timeit.default_timer() - start_time)

start_time_1 = timeit.default_timer()
my_set.find_bin(10000)
print(timeit.default_timer() - start_time_1)

start_time_2 = timeit.default_timer()
a = 10000 in my_set
print(timeit.default_timer() - start_time_2)


























