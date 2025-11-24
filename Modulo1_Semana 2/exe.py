nums = [23, 22, 10, 100, 10, 11, 12, 14, 100]
# animals= ["lion", "cat", "snake", "turtle", "bee"]
# def enum(lista, comienzo):
#     for indice, i in enumerate (lista, start = comienzo):
#         indice = i
#         print (indice)
# mi_lista= ["cat", "shark", "monkey", "dragonfly"]
# print(mi_lista)
# mi_lista.append("Bird")
# print(mi_lista)
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)
first = nums.index(10)
print(first)
nums.insert(23,4)
nums.append(24)
print(nums)
first = nums.count(100)
print(first)
first = nums.copy()
nums.clear()
nums = first
print(nums)
