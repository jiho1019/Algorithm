# 선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]]
# 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.
def solution(lines):
    answer = 0
    a = []
    b = []
    for i in range(len(lines)):
        for j in range(lines[i][0],lines[i][1]):
            a.append(j)
        lines[i] = a
        a = []
    print(lines)
    b.append(list(set(lines[0]) & set(lines[1])))
    b.append(list(set(lines[2]) & set(lines[1])))
    b.append(list(set(lines[0]) & set(lines[2])))
    return len(set(sum(b, [])))