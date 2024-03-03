#my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
def solution(my_string):
    answer = 0
    a = ''
    b = ''
    my_string += " "
    for i in my_string:
        if i.isdigit():
            a += i
            
        elif i == " ":
            if a:
                if b == '' or b == "+":
                    answer += int(a)
                    a = ''
                else:
                    answer -= int(a)
                    a = ''
                
        else:
            if i == "+":
                b = '+'
            else:
                b = "-"
    return answer
