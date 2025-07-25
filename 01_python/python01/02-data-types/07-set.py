my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}
print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1}


my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}
# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}
# 차집합
print(my_set_1 - my_set_2)  # {1, 2}
# 교집합
print(my_set_1 & my_set_2)  # {3}


# add - set에 요소를 추가(이미 존재하는 요소는 추가되지 않음)
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set)  # {'b', 2, 3, 1, 4, 'c', 'a'}
my_set.add(4)
print(my_set)  # {'b', 2, 3, 1, 4, 'c', 'a'}


# remove - set에서 요소를 제거(존재하지 않는 요소는 KeyError 발생)
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)  # {'b', 3, 1, 'c', 'a'}
my_set.remove(10) # KeyError
print(my_set)  # {'b', 3, 1, 'c', 'a'}
