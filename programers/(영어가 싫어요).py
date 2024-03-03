#영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔
# return 하도록 solution 함수를 완성해 주세요.
def solution(numbers):
    answer = 0
    a = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    b = ""
    for i in numbers:
        b += i
        if b in a:
            answer = answer * 10 + a.get(b)
            b = ""
    return answer