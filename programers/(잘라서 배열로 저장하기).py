#문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.
def solution(my_str, n):
    answer = []
    a = ''
    b = my_str
    my_str = list(my_str)
    for i in range(0,len(my_str)):
        a += my_str[i]
        if (i+1) % n == 0:
            answer.append(a)
            a = ''
        if i == len(my_str):
            answer.append(a)
    if len(my_str) % n != 0:
        answer.append(b[-(len(my_str) % n):])
    return answer