#덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
#수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(quiz):
    answer = []
    for i in range(0,len(quiz)):
        quiz[i] = quiz[i].split("=")
        quiz[i][0] = quiz[i][0].replace(" ","")
        quiz[i][1] = quiz[i][1].replace(" ","")
        if int(eval(quiz[i][0])) == int(quiz[i][1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer