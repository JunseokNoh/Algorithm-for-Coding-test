import sys

def solution(gems):
    answer = []
    size = len(set(gems))
    rmap = {gems[0]:1}
    l,r = 0,0
    hist_len = sys.maxsize
    while l < len(gems) and r < len(gems):
        if len(rmap) == size :
            if hist_len > r-l :
                hist_len = r-l
                answer = [l+1,r+1]
            if rmap[gems[l]] == 1 :
                del rmap[gems[l]]
            elif rmap[gems[l]] > 1:
                rmap[gems[l]] -= 1
            l+=1
        else:
            if r + 1 < len(gems) : r += 1
            else: break
            if gems[r] not in rmap.keys():
                rmap[gems[r]] = 1
            else:
                rmap[gems[r]] += 1

    return answer
