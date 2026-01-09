# 
arr = list(map(int, input().split()))

def solution(arr):
    arr.sort(reverse=True)
    new_list = set(arr)
    return new_list
# 맞긴 한데 이렇게 구현하면 결과가 set으로 나옴

print(solution(arr))

# Q. list 유지하려면 어떻게 해야할까?
def solution2(arr):
    list(set(arr))
    arr.sort(reverse = True)
    return arr

print("리스트 유지: ", solution2(arr))