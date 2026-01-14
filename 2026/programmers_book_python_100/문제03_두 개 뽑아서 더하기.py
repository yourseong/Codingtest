# 260113(화)
# 정수 배열 numbers 주어짐. numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를
# 배열에 오름차순으로 담아 반환하는 solution() 함수 완성하기 (중복 제거)

# 만약 numbers의 길이가 4라면
# numbers[0]+numbers[1], numbers[0]+numbers[2], numbers[0]+numbers[3] // 0 고정, 뒤에 더하는 숫자 증가

def solution(numbers):
    newarr = []
    for i in range(len(numbers)): # i가 0일 떄
        for j in range(i+1, len(numbers)):
            newarr.append(numbers[i] + numbers[j]) # 0 + 1, 1 + 2, 2 + 3, 3+4, 4+5...
    newarr = sorted(set(newarr))
    return newarr

#TEST 코드
print(solution([2, 1, 3, 4, 1])) # 반환값 : [2, 3, 4, 5, 6, 7]
print(solution([5, 0, 2, 7])) # 반환값 : [2, 5, 7, 9, 12]
