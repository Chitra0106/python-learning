from hmac import new

ScoreList = [10000,800,300,400,500,600,700,200,900]
#HighestScore = max(ScoreList)
Hihhscore = 0
sum = 0
for score in ScoreList:
    sum += score
    if score > Hihhscore:
        Hihhscore = int(score)
print(Hihhscore)
print(sum)



