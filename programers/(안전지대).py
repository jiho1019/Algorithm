#다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
#지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
#지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.
def solution(board):
    def check(board,x,y,n):
        dx = [1,1,1,-1,-1,-1,0,0]
        dy = [0,1,-1,1,0,-1,1,-1]
        for i in range(0,8):
            hx = x + dx[i]
            hy = y + dy[i]
            if 0 <= hx and hx < n and 0 <= hy and hy < n:
                if board[hx][hy] != 1:
                    board[hx][hy] = 2
    answer = 0
        
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                check(board,i,j,len(board))

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                answer +=1

    return answer
    