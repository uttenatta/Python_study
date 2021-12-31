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

# 변환과정을 출력해보면....
# []
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3]
# []
# [4]
# []
# [5]
# [5, 6]
# [4, 5, 6]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6, 7]
# []
# [8]
# [8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 
# 이렇게 출력되는데, 결국은 리스트 안에 리스트가 있는 경우, 재귀함수가 다시 호출되면서, 
# 처음에 만들어진 new[]와는 다른 새로운 메모리 영역에 another new[]가 만들어지면서, 그것이 리스트끼리 합쳐지고, 
# 리스트가 아니라, 그냥 element가 있는 경우에는, append되어 flatten이 완성된다.
# 리스트 안에 리스트, 또 그안에 리스트가 있는 경우에는 new another new[]가 만들어지고, 그것이 바로 상위의 another new[]와 합쳐지고,
# 리스트가 완성된다.

