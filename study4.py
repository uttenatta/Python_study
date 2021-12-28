def flatten(data):
    new = []
    for item in data:
        if type(item) == list:
            new += flatten(item)
        else:
            new.append(item)
    return new

example = [[1,2,3], [4,[5,6]], 7, [8,9]]
print("원본", example)
print("변환", flatten(example))

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list1 + list2)