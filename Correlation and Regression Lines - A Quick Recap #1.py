import math as m

def mean(data):
    return sum(data)/len(data)
 
def var(data):
    sum = 0
    for i in range (len(data)):
        sum = sum +(data[i] - mean(data))**2
    return sum
    
def cov(dt1, dt2):
    sum = 0
    for i in range(len(dt1)):
        sum += (dt1[i] - mean(dt1)) * (dt2[i] - mean(dt2))
    return sum

Physics_Scores = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
History_Scores = [10.0,  25.0,  17.0, 11.0,  13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

mean_Physics_Scores = mean(Physics_Scores)
mean_History_Scores = mean(History_Scores)

var_Physics_Scores = var(Physics_Scores)
var_History_Scores = var(History_Scores)

cov = cov(Physics_Scores, History_Scores)
std = m.sqrt(var_Physics_Scores * var_History_Scores)

r = cov / std

print(round(r, 3))
