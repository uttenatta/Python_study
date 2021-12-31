def flatten(data):
    new = []
    print(new)
    for item in data:
        if type(item) == list:
            new += flatten(item)
            print(new)
        else:
            new.append(item)
            print(new)
    return new

example = [[1,2,3], [4,[5,6]], 7, [8,9]]
print("원본", example)
print()
print()

print("변환되는 과정을 보여줍니다.")
flatten(example)

print()
print()
print("변환", flatten(example))

