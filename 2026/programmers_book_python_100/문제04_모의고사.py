# 260114(수)
# 수포자 문제 찍기

# 1번 패턴 : 12345 12345...
# 2번 패턴 : 21232425 21232425...
# 3번 패턴 : 3311224455 3311224455...

# 정답 배열 answers가 주어졌을 때 가장 많은 문제 맞힌 사람을 배열에 담아 반환하는 solution 함수
# 여럿이면 오름차순 정렬
# e.g. answers = [1,2,3,4,5]
#      return = [1]
# 입력, 출력 둘 다 배열 형태

# idea : 정답 맞추면 해당 cnt를 증가시키고 최종적으로 cnt랑 최고점이랑 비교해서 제일 큰거 출력
def solution(answers):

    patterns = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]

    cnt = [0] * 3
    for i, answer in enumerate(answers): 
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                cnt[j] += 1 # 패턴별로 점수 증가

    # 최고점 저장
    max_score = max(cnt) 

    max_list =[]

    for k, score in enumerate(cnt): # 점수 저장한 배열에서 인덱스 추출
        if max_score == score: # 최고점이면
            max_list.append(k + 1) # 배열에 추가 (출력값은 1, 2, 3을 기대하므로 0부터 시작하는 배열 인덱스를 고려해 +1)
    return max_list

# 테스트케이스
print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))


'''
key point.
1. enumerate 활용해 배열의 index와 value를 동시에 반환
2. 정답 배열 answers를 기준으로 찍기 패턴과 비교
3. cnt = [0] * 3 배열 선언 후 반복문 통해 증가시키는 것으로 코드 확장성 높임 (기존 아이디어 : cnt += 1, cnt2 += 1 ...)
4. .append() 활용해 최종 결과물 반환
'''