import os
import tkinter as tk
from tkinter import simpledialog, messagebox




def load_profile(user):
    file_name = user + "_profile.txt"
    if os.path.exists(file_name):
        file = open(file_name, "r")
        data = file.read()
        file.close()
        return data
    else:
        return None

def user_info():

    user = simpledialog.askstring("Input", "Enter your name:")
    user_profile_data = load_profile(user)
    if user_profile_data:
        messagebox.showinfo("Success", "User profile loaded successfully!\n" + user_profile_data)
        return None
    else:
        messagebox.showwarning("Warning", "User profile not found.")
    
        while True:
            age = simpledialog.askstring("Input", "What is your age: ")
            if age.isdigit() and int(age) > 0:
                age = int(age)
                break
            else:
                messagebox.showwarning("Warning", "Invalid input! Age must be a number greater than 0.")

        while True:  
            sex = simpledialog.askstring("Input","What is your sex (male or female): ")
            if sex.lower() == 'male' or sex.lower() == 'female':
                sex = sex.lower()
                break
            else:   
                messagebox.showwarning("Warning", "Invalid input! Input must either be male or female.")

        while True:
            measuring_system = simpledialog.askstring("Input", "Do you use the Metric System or the Imperial System: ")
            if measuring_system.lower() == 'imperial':
                measuring_system = measuring_system
                break
            elif measuring_system.lower() == 'metric':
                measuring_system = measuring_system.lower()
                break
            else:
                messagebox.showwarning("Warning", "Invalid input! Input must be 'imperial' or 'metric'.")

        if measuring_system == 'imperial':
            while True:
                weight = simpledialog.askstring("Input", "What is your weight in pounds: ")
                if weight.isdigit() and int(weight) > 0:
                    weight = int(weight)/2.205
                    break
                else:
                    messagebox.showwarning("Warning", "Invalid input! Weight must be a number greater than 0.")
            while True:
                height = simpledialog.askstring("Input", "What is your height in inches: ")
                if height.isdigit() and int(height) > 0:
                    height = int(height)* 2.54
                    break
                else:
                    messagebox.showwarning("Warning", "Invalid input! Height must be a number greater than 0.")
        else:
            while True:
                weight = simpledialog.askstring("Input", "What is your weight in kilograms: ")
                if weight.isdigit() and int(weight) > 0:
                    weight = int(weight)
                    break
                else:
                    messagebox.showwarning("Warning", "Invalid input! Weight must be a number greater than 0.")

            while True:
                height = simpledialog.askstring("Input", "What is your height in centimeters: ")
                if height.isdigit() and int(height) > 0:
                    height = int(height)
                    break
                else:
                    messagebox.showwarning("Warning", "Invalid input! Height must be a number greater than 0.")
                

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
    
    return (int(bmr_result,)), user
    

def calculate_activity(bmr_result): 
    while True:
        activity_level = simpledialog.askstring("Input", "What is your activity level (none, little, moderate, lots, extra): ")
        if activity_level.lower() in ['none', 'little', 'moderate', 'lots', 'extra']:
            break
        else:
            messagebox.showwarning("Warning", "Invalid input! Pleaase choose a word from the provided list.")

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
        goals = simpledialog.askstring("Input", "Do you want to lose, maintain, or gain weight: ")
        if goals.lower() in ['lose', 'maintain','gain']:
            break
        else:
            messagebox.showwarning("Warning", "Invalid input! please choose one of the words provided in the prompt.")

    if goals == 'lose':
        calories = activity_level_num - 500
    elif goals == 'maintain':
        calories = activity_level_num
    elif goals == 'gain':
        while True:
            gain = float(simpledialog.askstring("Input", "Gain 0.5 or 1 pound per week?: "))
            if gain == 0.5 or gain == 1 or gain == .5:
                gain = gain
                break
            else:
                messagebox.showwarning("Warning", "Invalid input! Please enter either '0.5' or '1'.")
        if gain == 0.5: 
            calories = activity_level_num + 250
        elif gain == 1:
            calories = activity_level_num + 500

    messagebox.showinfo("Info","\nin order to " + goals + " weight, your daily caloric goals should be: " + str(int(calories)))
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


    messagebox.showinfo("Info", "Your macronutrient breakdown is recommended as below\n Carbohydrates: " + str(int(carbs)) + "grams\n Protein: " + str(int(protein)) + "grams\n Fats:" + str(int(fat)) + "grams")
    return carbs, protein, fat

def save_profile(user, bmr_result, calories, carbs, protein, fat):
    file_name = user + "_profile.txt"
    profile_file = open(file_name, "w")
    profile_file.write("Name: " + user + "\n")
    profile_file.write("BMR: " + str(bmr_result) + "\n")
    profile_file.write("Calories: " + str(int(calories)) + "\n")
    profile_file.write("Macros:\n")
    profile_file.write("  Carbs: " + str(int(carbs)) + " grams\n")
    profile_file.write("  Protein: " + str(int(protein)) + " grams\n")
    profile_file.write("  Fat: " + str(int(fat)) + " grams\n")
    profile_file.close()


root = tk.Tk()
root.withdraw()


bmr_result, user = user_info()
if bmr_result:
    activity_level, activity_level_num = calculate_activity(bmr_result)
    calories = gain_or_lose(activity_level_num)
    carbs, protein, fat = calculate_macros(calories, activity_level)

    while True:
        answer = simpledialog.askstring("Input", "Do you want to save your data? (yes or no): \n")
        if answer.lower() == 'yes':
            save_profile(user, bmr_result, calories, carbs, protein, fat)
            messagebox.showinfo("Success", "Profile saved successfully!")
            break
        elif answer.lower() == 'no':
            messagebox.showinfo("Info", "You have chosen to not save your profile.")
            break
        else:
            messagebox.showwarning("Warning", "Invalid input! Please enter 'yes' or 'no'.")
