#사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다. 
#사분면은 아래와 같이 1부터 4까지 번호를매깁니다.
def solution(dot):
    answer = 0
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] > 0 and dot[1] < 0:
        answer = 4
    elif dot[0] < 0 and dot[1] < 0:
        answer = 3
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2