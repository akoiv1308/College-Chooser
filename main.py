'''
Questions:
1)Do you want to play sports? Baylor University
2)Do you want to stay home or live in dorm? Dorm: New York University, Stay Home: Brooklyn College
3)In what college do you want to be: private or public? Private: MIT, Public: Brooklyn
4)What field of study do you want to be in? 
5)Do you prefer the city or the country? Cornell
'''
collegeScore = [0,0,0,0,0]
collegeNames = ["Baylor University", "Dartmouth College", "Brooklyn College", "MIT", "Eastern Michigan University"]


Question1 = "Do you want to stay home or live in a dorm? \n1. Dorm \n2. Stay home"

answer1 = int(input(Question1))
if answer1 == 1:
  collegeScore[4] += 1
  collegeScore[3] += 1
  collegeScore[0] += 1
else:
  collegeScore[1] += 1
  collegeScore[2] += 1

for i in range(5):
  print(collegeNames[i], "\t", collegeScore[i])

Question2 = "Do you want to play sports?\n1. Yes \n2. No"

answer2 = int(input(Question2))
if answer2 == 1:
  collegeScore[0] += 1
  collegeScore[4] += 1
else:
  collegeScore[1] += 1
  collegeScore[2] += 1
  collegeScore[3] += 1                           

for i in range(5):
  print(collegeNames[i], "\t", collegeScore[i]) 

Question3 = "In what college do you want to go?\n1. Public \n2. Private"

answer3 = int(input(Question3))
if answer3 == 1:
  collegeScore[2] += 1
  collegeScore[4] += 1
else:
  collegeScore[1] += 1
  collegeScore[0] += 1
  collegeScore[3] += 1

for i in range(5):
  print(collegeNames[i], "\t", collegeScore[i])

Question4 = "Do you prefer the city or the country college?\n1. City \n2. Country"

answer4 = int(input(Question4))
if answer4 == 1:
  collegeScore[2] += 1
  collegeScore[3] += 1
  collegeScore[0] += 1
  collegeScore[4] += 1
else:
  collegeScore[1] += 1

for i in range(5):
  print(collegeNames[i], "\t", collegeScore[i])

Question5 = "What field of study do you want to be in?\n1. Technology/Engineering \n2. Athletic Training \n3. Art History \n4. Biology/Psychology" 

answer5 = int(input(Question5)) 
if answer5 == 1:
  collegeScore[3] += 1
elif answer5 == 2:
  collegeScore[0] += 1
  collegeScore[4] += 1
elif answer5 == 3:
  collegeScore[1] += 1
elif answer5 == 4:
  collegeScore[2] += 1
  
highScore = 0

for i in range(len(collegeScore)):
  if collegeScore[i] >= highScore:
    highScore = collegeScore[i]
    finalCollege = collegeNames[i]

for i in range(5):
  print(collegeNames[i], "\t", collegeScore[i])

print("Best college for you is :  " + finalCollege)