# 레스토랑에서 여러개의 테이블에 나누어 앉으려고 함.
# 한 사람만 앉는 경우는 없도록 하고 싶음.
# 한개의 테이블에 앉을 수 있는 사람 수는 최대 10명
# 100명의 사람이 하나 이상의 테이블에 나누어 앉는 패턴을 구하시오

min = 2 # min_number_of_person
max = 10 # max_number_of_person
total = 100 # total_number_of_person

memo = {}

def problem(n_remaining, n_seated):
    key = str([n_remaining, n_seated])

    if key in memo:
        return memo[key]
    if n_remaining < 0:
        return 0
    if n_remaining == 0:
        return 1

    count = 0
    for i in range(n_seated, max+1):
        count += problem(n_remaining - i, i)

    memo[key] = count
    return count

print(problem(total, min))
