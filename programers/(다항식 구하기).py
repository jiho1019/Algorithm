#한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
#덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 
#return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.
def solution(a):
    x = 0
    y = 0
    a = a.split(" + ")
    print(a)
    for i in range(len(a)):
        if a[i][-1] == 'x':
            if a[i][0] != 'x':
                x += int(a[i][:-1])
            else:
                x += 1
        else:
            y += int(a[i])
            
    if y == 0:
        if x == 0:
            return str(0)
        else:
            if x == 1:
                return 'x'
            return str(x) + 'x'
    
    else:
        if x == 0:
            return str(y)
        else:
            if x == 1:
                return "x + " + str(y)
            return str(x) + "x + " + str(y)