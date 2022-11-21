score = [2,4,22,10,6]

swapped = True

while(swapped):
    swapped = False
    for i in range(len(score)):
        for j in range(len(score) - 1 ):
            if score[j] > score[j+1]:
                temp = score[j+1]
                score[j+1] = score[j]
                score[j] = temp
                swapped = True

print(score)
