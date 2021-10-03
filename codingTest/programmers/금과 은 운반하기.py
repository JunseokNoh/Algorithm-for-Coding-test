import sys

def solution(a, b, g, s, w, t):
    answer = sys.maxsize
    start, end = 0, 400000000000000
    size = len(g)

    while start <= end :
        mid = (start + end) // 2
        print(mid)
        gs_g, gs_s = 0,0
        sg_s, sg_g = 0,0

        for i in range(size):
            #step1 mid 시간 동안 트럭이 운반할 수 있는 횟수
            cycle = ((mid - t[i]) // (t[i] * 2)) + 1
            total = cycle * w[i]

            #step2 금을 일단 다 옮기고 남은 공간이 있으면 은을 옮김
            gs_g += g[i] if g[i] < total else total
            gs_s += min(s[i], total - g[i]) if g[i] < total else 0

            # step3 은을 일단 다 옮기고 남은 공간이 있으면 금을 옮김
            sg_s += s[i] if s[i] < total else total
            sg_g += min(g[i], total - s[i]) if s[i] < total else 0

        # step4
        # 금을 먼저 옮겼을 때의 금의 양이 a보다 크거나 같고
        # 은을 먼저 옮겼을 때의 은의 양이 b보다 크거나 같으면서
        # 금을 먼저 옮겼을 때의 금의 양과, 은의 양의 합이 a+b보다 크다면 답이 될 수 있음
        if gs_g >= a and sg_s >= b and gs_g + gs_s >= a+b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid+1
    return answer


if __name__ == "__main__":
    #print(solution(10,10,[100],[100],[7],[10]))
    print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]))
