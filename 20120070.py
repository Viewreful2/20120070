def a1(B) :
    for i in range(0,5) :
        if (B[i][0] +B[i][1] +B[i][2] +B[i][3] +B[i][4]) == 5:
            return True;
    return False;

def a2(B):
    for i in range(0,5) :
        if (B[0][i] +B[1][i] +B[2][i] +B[3][i] +B[4][i]) == 5:
            return True;
    return False;

def a3(B):
    count = 0
    for i in range(0,5) :
        if B[i][i] == 1:
            count = count +1
    if count == 5 :
        return True;

    count = 0
    for i in range(0,5):
        if B[i][4-i] == 1:
            count = count +1
    if count == 5 :
        return True;
    
    return False;


def a4(B):
    if (B[0][0] +B[0][4] +B[4][0] +B[4][4]) == 4:
        return True;
    
    return False;    



row = 5#행의 길이
col = 5#열의 길이

Apap = []#내가 만드는 빙고 게임의 게임판
B = []
T = int(input())#얼만큼 빙고 게임을 한 것인지 의미

for t in range(0,T):#T만큼 빙고 게임을 합시다.
    Apap = []
    B = []
    for i in range(0, row):#행의 길이만큼 돌면서
        row_input = input().split()#인풋을 받고
        row_input = [int(j) for j in row_i