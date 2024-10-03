import math
son = {1,1,3,13,21}
result = {2,3,23,4,21}
result1  = min(son)
result2  = max(son)
print(result1,result2)
print(sorted(son))
# son_list = list(son)
# print(son_list)
for i in son:
    if i % 2 ==0 :
        print(f"juft son {i}")
    elif i % 2 ==1:
        print(f"toq{i}")
son.pop()
print(son)
son.add(44)
print(son)
son.remove(3)
print(son)
new_set = son.union(result)
print(new_set)
son.update({100})
print(son)