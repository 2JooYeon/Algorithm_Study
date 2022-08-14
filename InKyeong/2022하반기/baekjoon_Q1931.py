#기본 입력값 N과 arr에 저장
N = int(input())
arr = []
for i in range (0, N) :
  m, n = map(int, input().split(" "))
  arr.append((m, n))

# key point) 튜플[1]번째인 끝나는 시간 기준으로 정렬하고 만약 같다면 튜플[0]번째인 시작 시간 기준으로 정렬
arr = sorted(arr, key=lambda x: (x[1], x[0]))

# 정답 초기값
answer = 1
endtime = arr[0][1]

# 계산
for i in range(1, N):
  if arr[i][0] >= endtime :
    answer += 1
    endtime = arr[i][1]

# 정답 구함
print(answer)