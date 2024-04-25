def user_info():
    while True:
        age = input('What is your age: ')
        if age.isdigit() and int(age) > 0:
            age = int(age)
            break
        else:
            print("Invalid input! Age must be a number greater than 0.")

    while True:  
        sex = input('What is your sex (male or female): ')
        if sex.lower() == 'male' or sex.lower() == 'female':
            sex = sex.lower()
            break
        else:   
            print("Invalid input! Input must either be male or female.")

    while True:
        weight = input('What is your weight in pounds : ')
        if weight.isdigit() and int(weight) > 0:
            weight = int(weight)
            break
        else:
            print("Invalid input! Weight must be a number greater than 0.")

    while True:
        height = input('What is your height in inches: ')
        if height.isdigit() and int(height) > 0:
            height = int(height)
            break
        else:
            print("Invalid input! Height must be a number greater than 0.")
                

    weight = weight/2.205        
    height = height * 2.54

    if sex == 'male':
        c1 = 5
        hm = 10 * weight
        wm = 6.25 * height
        am = 5 * age
        bmr_result = hm + wm - am + c1
    elif sex == 'female':
        c1 = 161
        hm = 10 * weight
        wm = 6.25 * height
        am = 5 * age
        bmr_result = hm + wm - am - c1
    #BMR = (10 x weight) + (6.25 x height) – (5 x age) + 5 (male)
    #BMR = (10 x weight) + (6.25 x height) – (5 x age) - 161 (female)
    return (int(bmr_result,))
    

def calculate_activity(bmr_result): 
    while True:
        activity_level = input('What is your activity level (none, little, moderate, lots, extra): ')
        if activity_level.lower() in ['none', 'little', 'moderate', 'lots', 'extra']:
            break
        else:
            print("Invalid input! Pleaase choose a word from the provided list.")

    if activity_level == 'none':
        activity_level_num = 1.2 * bmr_result
    elif activity_level == 'little':
        activity_level_num = 1.375 * bmr_result
    elif activity_level == 'moderate':
        activity_level_num = 1.55 * bmr_result
    elif activity_level == 'lots':
        activity_level_num = 1.725 * bmr_result
    elif activity_level == 'extra':
        activity_level_num = 1.9 * bmr_result

    return activity_level, activity_level_num

def gain_or_lose(activity_level_num):
    while True:
        goals = input('Do you want to lose, maintain, or gain weight: ')
        if goals in ['lose', 'maintain','gain']:
            break
        else:
            print("Invalid input! please choose one of the words provided in the prompt.")

    if goals == 'lose':
        calories = activity_level_num - 500
    elif goals == 'maintain':
        calories = activity_level_num
    elif goals == 'gain':
        while True:
            gain = float(input('Gain 0.5 or 1 pound per week?: '))
            if gain == 0.5 or gain == 1 or gain == .5:
                gain = gain
                break
            else:
                print("Invalid input! Please enter either '0.5' or '1'.")
        if gain == 0.5: 
            calories = activity_level_num + 250
        elif gain == 1:
            calories = activity_level_num + 500

    print('\nin order to', goals, 'weight, your daily caloric goals should be', int(calories),'!')
    return calories
    

def calculate_macros(calories, activity_level):
    

    if activity_level == 'none' or 'little':
        carbs = (calories * .55)/4
        protein = (calories * .2)/4
        fat = (calories * .25)/9
    elif activity_level == 'moderate':
        carbs = (calories * .5)/4
        protein = (calories * .2)/4
        fat = (calories * .3)/9
    elif activity_level == 'lots':
        carbs = (calories * .5)/4
        protein = (calories * .25)/4
        fat = (calories * .25)/9
    elif activity_level == 'extra':
        carbs = (calories * .55)/4
        protein = (calories * .3)/4
        fat = (calories * .25)/9

    print('Your macronutrient breakdown is recommened as below\n Carbohydrates:', int(carbs), 'grams\n Protein:', int(protein), 'grams\n Fats:', int(fat),'grams' )


activity_level, activity_level_num = calculate_activity(user_info())
calculate_macros(gain_or_lose(activity_level_num), activity_level)
    
