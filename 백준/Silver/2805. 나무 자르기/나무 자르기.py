import sys
input = sys.stdin.readline


n,m = map(int, input().split())
alist = list(map(int, input().split()))
start =0
end = max(alist)# 최대 높이
while start<=end:
    sum = 0
    mid = (start+end)//2
    for i in range(n):
        if alist[i]>mid: # 음수 값이 들어가면 안됨
            s = alist[i]-mid
            sum = sum+s
        if sum>m: # 더하는 도중 이미 필요한 나무 m를 넘으면 종료 후 그 값 사용
            break
    if sum <m:
        end = mid-1
    else:
        result = mid # m을 만족하면 우선 그 높이 저장
        start = mid+1 # 더 높은 높이 탐색 후 else에 안걸리면 또 저장

print(result)