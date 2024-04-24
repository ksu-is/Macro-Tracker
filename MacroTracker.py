def user_info():
    age = int(input('What is your age: '))
    gender = input('What is your gender: ')
    weight = int(input('What is your weight in pounds : '))
    weight = weight/2.205
    height = int(input('What is your height in inches: '))
    height = height * 2.54

    if gender == 'male':
        c1 = 5
        hm = 10 * weight
        wm = 6.25 * height
        am = 5 * age
        bmr_result = hm + wm - am + c1
    elif gender == 'female':
        c1 = 161
        hm = 10 * weight
        wm = 6.25 * height
        am = 5 * age
        bmr_result = hm + wm - am - c1
    #BMR = (10 x weight) + (6.25 x height) – (5 x age) + 5 (male)
    #BMR = (10 x weight) + (6.25 x height) – (5 x age) - 161 (female)
    return (int(bmr_result,))
    

def calculate_activity(bmr_result): 
    activity_level = input('What is your activity level (none, little, moderate, lots, extra): ')

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
    goals = input('Do you want to lose, maintain, or gain weight: ')

    if goals == 'lose':
        calories = activity_level_num - 500
    elif goals == 'maintain':
        calories = activity_level_num
    elif goals == 'gain':
        gain = int(input('Gain 1 or 2 pounds per week? Enter 1 or 2: '))
        if gain == 1: 
            calories = activity_level_num + 500
        elif gain == 2:
            calories = activity_level_num + 1000

    print('\nin order to ', goals, 'weight, your daily caloric goals should be', int(calories), '!')
    return calories
    

def calculate_macros(calories, activity_level):
    #activity_level = input('What is your activity level (none, light, moderate, or heavy): ')

    if activity_level == 'none':
        carbs = (calories * .5)/4
        protein = (calories * .2)/4
        fat = (calories * .3)/9

    print('\nYour macronutrient breakdown is recommened as below\n Carbohydrates:', carbs, 'grams\n Protein:', protein, 'grams\n Fats:', fat,'grams' )


activity_level, activity_level_num = calculate_activity(user_info())
calculate_macros(gain_or_lose(activity_level_num), activity_level)

    
