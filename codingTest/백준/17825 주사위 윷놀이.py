dice = list(map(int,input().split()))
game = [i+1 for i in range(33)]
#0~20 까지 쭉 직진
game[5], game[10] = 21,
print(game)