def getInput(txt, f=True):
    while True:
        try:
            temp = float(input(txt)) if f else int(input(txt))
            return temp
        except:
            t = "Float" if f else "Integer"
            print("Please enter a %s value" % (t))

def getBMR(weight, height, age):
    genders = ("m", "f")
    sex = ""
    while True:
        sex = input("Sex M or F: ").lower()
        if sex not in genders:
            print("Please Type M or F")
        else:
            break
    if sex == "m":
        BMR = float((10 * weight) + (6.25 * height) - (5 * age) + 5)
    else:
        BMR = float((10 * weight) + (6.25 * height) - (5 * age) - 161)
    return BMR

def getActivityLevel():
    activities = {"very light": 1.3, "light": 1.55, "moderate": 1.65, "heavy": 1.8, "very heavy": 2.0}
    level = ""
    while True:
        level = input("Input level of activity today (Very light, Light, Moderate, Heavy, Very Heavy): ").lower()
        if level not in activities:
            print("Please enter Level of Activity (Very Light, Light, Moderate, Heavy, Very Heavy")
        else:
            return activities[level]

def getTDEE(BMR, activityLevel):
    TDEE = float((BMR * activityLevel))
    return TDEE

def getGoal():
    goal = {"healthy inactive": .4, "recreational excerciser": .75, "building muscle": .9, "growing teen athlete": 1.0}
    level = ""
    while True:
        level = input(
            "Input your Excersise Goal from the list provided, Healthy inactive, Recrational Excerciser, Building Muscle, Growing teen athlete: ").lower()
        if level not in goal:
            print("Please enter a string from the list provided")
        else:
            return goal[level]


weight = (getInput("Weight in lbs: ")*.45)
height = (getInput("Height in inches: ")*2.54)
age = getInput("Age in years: ", False)

BMR = getBMR(weight, height, age)
activityLevel = getActivityLevel()
TDEE = getTDEE(BMR, activityLevel)
goal = getGoal()

proteinIntake = int(goal * (weight * (2.2)))
fatIntake = int(.20 * TDEE)
carbIntake = int(TDEE - (proteinIntake + fatIntake))

print("Weight: " + str(weight) + "\n" + "Height: " + str(height) + "\n" + "Age: " + str(age) + "\n" + "BMR: " +
      str(BMR) + "\n" + "Activity Level: " + str(activityLevel) + "\n" + "TDEE: " + str(TDEE) + "\n" + "\n" +
      "Calorie Intake: " +str(int(TDEE)) + " calories" + "\n" + "Carbohydrate Intake: " + str(int(carbIntake/4)) +
      " grams" + "\n" + "Protein Intake: " + str(proteinIntake) + " grams" + "\n" + "Fat Intake: " +
      str(int(fatIntake/9)) + " grams")