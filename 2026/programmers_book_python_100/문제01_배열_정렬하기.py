# 260109(금)
# 정수 배열을 오름차순 정렬해서 반환하는 solution 함수 완성하기

# 입력을 받고싶으면 작성
arr = list(map(int, input().split(",")))

def solution(arr):
    arr.sort()
    return arr

print("입력을 받을 때: ", solution(arr))
print("그냥 실행할 때")

# 테스트케이스
print(solution([1,-5,2,4,3])) # 반환값 : [-5, 1, 2, 3, 4]
print(solution([2,1,1,3,2,5,4])) # 반환값 : [1, 1, 2, 2, 3, 4, 5]
print(solution([1,6,7])) # 반환값 : [1, 6, 7]

