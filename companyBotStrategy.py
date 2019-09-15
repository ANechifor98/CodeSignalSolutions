def companyBotStrategy(trainingData):
    average = 0
    validpair = 0
    for pair in trainingData:
        if pair[1] == 1:
            average += pair[0]
            validpair += 1
    if validpair == 0:
        return 0
    else:
        average = average / validpair
        return average

if __name__ == "__main__":
    trainingData = [[4,-1], 
 [0,0], 
 [5,-1]]
    print(companyBotStrategy(trainingData))
