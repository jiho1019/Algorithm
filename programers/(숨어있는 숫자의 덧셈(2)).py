#문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    answer = 0
    a = []
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            a.append(my_string[i])
        else:
            if a:
                answer += int(''.join(a))
                a=[]
    if a:
        answer += int(''.join(a))
        
    return answer 
            