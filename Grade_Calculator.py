'''
Write a program to calculate students's avg test scores and grades
'''

nameList = []
scoreList = []
scoreList1 = []
# studentScoreList = []
emptyList = []
gradeList = []

def grade(avgTestScore):
    
    if (avgTestScore>90):
        return "A"
    elif (avgTestScore >=85):
        return "A-"
    elif (avgTestScore >=80):
        return "B"
    elif (avgTestScore >=75):
        return "B-"
    elif (avgTestScore >= 70):
        return "C" 
    elif (avgTestScore >= 65):
        return "C-" 
    else:
        return "F"
        
def averageTestScore(scoreList):
    global avgTestScore
    avgTestScore = sum(scoreList)/len(scoreList)
    return avgTestScore
    
def printresult():
    print("Avg score of " + student + "is : ",avgTestScore)
    print("Grade obtained by "+ student + " is : ",end='' )
    return gradesObtained
    
    
studentsCount = int(input("How Many Students : "))
testCount = int(input("How many tests? : "))
for i in range (studentsCount):
    student = input ("Student "+ str(i+1) + " Name : ")
    for j in  range (testCount):
        testScores = int(input("Test "+ str(j+1) + " Score : " ))
        scoreList.append(testScores)
    scoreList1.append(testScores)
    testScoresavg = averageTestScore(scoreList)
    gradesObtained = grade(avgTestScore)
    result = printresult()
    print (result)
    gradeList.append(gradesObtained)
    emptyList.append(scoreList1)
    nameList.append(student)
    
    

print("Stdent names : " ,nameList)
print("result : ", emptyList)
print(gradeList)

# for a, *b in emptyList:
#       print(a, ' '.join(map(str,b)))
print ("Student \t\t Marks \t\t\t grade")
for n,e,g in zip(nameList,emptyList,gradeList):
     print(str(n) + '\t\t\t' + str(e) + '\t\t' + str(g))
