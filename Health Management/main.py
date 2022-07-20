from tkinter import *
import time
from plyer import notification

def main():
    gui_window = Tk()
    gui_window.title("Health Management App")

    Title_Label = Label(gui_window, text = "The Health App \n Developed by Yuvraj and Tarunima", font = ('Bahnschrift 20 bold underline'))
    Title_Label.pack()

    LABEL = Label(gui_window, text = "\n \n What does this application do?", font = ('Cambria 17 bold'))
    LABEL.place(x = 100, y = 100)

    one = Label(gui_window, text = "\n 1. BMI \n  2. BMR", font = ('Cambria 17'))
    one.place(x = 120, y = 180)
    # ------------------------------------------------------------------------------------------------------------------------------------------------------
    def CALCULATE_BMI():
        height_1 = float(HEIGHT_ENTRY.get())
        weight_1 = float(WEIGHT_ENTRY.get())
        bmi = weight_1 / ((height_1/100)**2)
        bmi = round(bmi, 2)
        if bmi < 18.5:
            conclusion_bmi = "Underweight.\nYou need to include some calorie dense food in your diet."
        elif bmi > 18.4 and bmi <= 24.9:
            conclusion_bmi = "Normal.\nWell done. You are having a good diet according to your height and weight."
        elif bmi > 24.9 and bmi <= 29.9:
            conclusion_bmi = "OverWeight.\nOh no.. You need to be more active in order to fall under normal catagory"
        elif bmi > 29.9:
            conclusion_bmi = "Obesity.\nToo bad. You have to include some intense cardio with a proper diet."
        PRINT_BMI = Label(gui_window, text = f"Your BMI is {bmi} and you fall under the category of {conclusion_bmi}", font = ('Corbel 15'))
        PRINT_BMI.place(x = 675, y = 350)

    BMI_LABEL = Label(gui_window, text = "BMI Calculator - Calculate your Body Mass Index", font = ('Centaur 17 underline '))
    BMI_LABEL.place(x = 100, y = 300)

    HEIGHT_LABEL = Label(gui_window, text = "Enter Height (in cm) : ", font = ('Corbel 15'))
    HEIGHT_LABEL.place(x = 150, y = 350)

    HEIGHT_ENTRY = Entry(gui_window, bg = 'white', font = ('Bahnschrift'))
    HEIGHT_ENTRY.place(x = 375, y = 360)

    WEIGHT_LABEL = Label(gui_window, text = "Enter Weight (in Kg) : ", font = ('Corbel 15'))
    WEIGHT_LABEL.place(x = 150, y = 375)

    WEIGHT_ENTRY = Entry(gui_window, bg = 'white', font = ('Bahnschrift'))
    WEIGHT_ENTRY.place(x = 375, y = 385)

    FIND_BMI = Button(gui_window, text = "Get BMI", font = ("Bahnschrift"), fg = 'white', bg = 'red', activebackground = 'blue', command = CALCULATE_BMI)
    FIND_BMI.place(x = 575, y = 370)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------

    def CALCULATE_MAIN():
        height_2 = float(HEIGHT_ENTRY_2.get())
        weight_2 = float(WEIGHT_ENTRY_2.get())
        gender = str(GENDER_ENTRY.get())
        age = float(AGE_ENTRY.get())
        activity_level = str(ACTIVITY_LEVEL_ENTRY.get())

        if gender.lower() == "male" or gender.lower() == 'm' and activity_level.lower() == "sedentary":
            bmr = (88.362 + (13.397 * weight_2) + (4.799 * height_2) - (5.677 * age))*1.2
            bmr = round(bmr, 2)
        elif gender.lower() == "male" or gender.lower() == 'm' and activity_level.lower() == "light":
            bmr = (88.362 + (13.397 * weight_2) + (4.799 * height_2) - (5.677 * age))*1.375
            bmr = round(bmr, 2)
        elif gender.lower() == "male" or gender.lower() == 'm' and activity_level.lower() == "moderate":
            bmr = (88.362 + (13.397 * weight_2) + (4.799 * height_2) - (5.677 * age))*1.55
            bmr = round(bmr, 2)
        elif gender.lower() == "male" or gender.lower() == 'm' and activity_level.lower() == "active":
            bmr = (88.362 + (13.397 * weight_2) + (4.799 * height_2) - (5.677 * age))*1.725
            bmr = round(bmr, 2)
        elif gender.lower() == "female" or gender.lower() == 'f' and activity_level.lower() == 'sedentary':
            bmr = (447.593 + (9.247 * weight_2) + (3.098 * height_2) - (4.330 * age))*1.2
            bmr = round(bmr, 2)
        elif gender.lower() == "female" or gender.lower() == 'f' and activity_level.lower() == 'light':
            bmr = (447.593 + (9.247 * weight_2) + (3.098 * height_2) - (4.330 * age))*1.375
            bmr = round(bmr, 2)
        elif gender.lower() == "female" or gender.lower() == 'f' and activity_level.lower() == 'moderate':
            bmr = (447.593 + (9.247 * weight_2) + (3.098 * height_2) - (4.330 * age))*1.55
            bmr = round(bmr, 2)
        elif gender.lower() == "female" or gender.lower() == 'f' and activity_level.lower() == 'active':
            bmr = (447.593 + (9.247 * weight_2) + (3.098 * height_2) - (4.330 * age))*1.725
            bmr = round(bmr, 2)

        PRINT_BMR = Label(gui_window, text = f"You need to consume {bmr} calories a day\nto maintain your current weight", font = ('Corbel 15'))
        PRINT_BMR.place(x = 900, y = 525)

    BMR_LABEL = Label(gui_window, text = "Maintenance Calorie Calculator - Calculate how may calories you need to maintain your current body weight", font = ("Centaur 17 underline"))
    BMR_LABEL.place(x = 100, y = 425)

    GENDER_LABEL = Label(gui_window, text = "1.Enter your gender (male/female) : ", font = ("Corbel 15"))
    GENDER_LABEL.place(x = 150, y = 475)

    GENDER_ENTRY = Entry(gui_window, bg = 'white', font = ('Bahnschrift'))
    GENDER_ENTRY.place(x = 500, y = 485)

    WEIGHT_LABEL_2 = Label(gui_window, text = "2.Enter your weight (in Kg) : ", font = ("Corbel 15"))
    WEIGHT_LABEL_2.place(x = 150, y = 500)

    WEIGHT_ENTRY_2 = Entry(gui_window, bg = 'white', font = ('Bahnschrift'))
    WEIGHT_ENTRY_2.place(x = 500, y = 510)

    HEIGHT_LABEL_2 = Label(gui_window, text = "3.Enter your Height (in cm) : ", font = ("Corbel 15"))
    HEIGHT_LABEL_2.place(x = 150, y = 525)

    HEIGHT_ENTRY_2 = Entry(gui_window, bg = 'white', font = ('Bahnschrift'))
    HEIGHT_ENTRY_2.place(x = 500, y = 535)

    AGE_LABEL = Label(gui_window, text = "4.Enter your Age (in years) : ", font = ("Corbel 15"))
    AGE_LABEL.place(x = 150, y = 550)

    AGE_ENTRY = Entry(gui_window, bg = 'white', font = ('Bahnschrift'))
    AGE_ENTRY.place(x = 500, y = 560)

    ACTIVITY_LEVEL_LABEL = Label(gui_window, text = "5.What is your activity level?:\n (Sedentary : Little or no exercise)\n(Light : 1-3 days a week) \n(Moderate : 3-5 days a week)\n(Active : 6-7 days a week)", font = ('Corbel 15'))
    ACTIVITY_LEVEL_LABEL.place(x = 120, y = 575)

    ACTIVITY_LEVEL_ENTRY = Entry(gui_window, bg = 'white', font = ('Bahnschrift'))
    ACTIVITY_LEVEL_ENTRY.place(x = 500, y = 585)

    FIND_BMR = Button(gui_window, text = "Get Maintenance Calorie", font = ("Bahnschrift"), fg = 'white', bg = 'red', activebackground = 'blue', command = CALCULATE_MAIN)
    FIND_BMR.place(x = 700, y = 525)

    gui_window.geometry("1600x900")
    gui_window.mainloop()

main()

if __name__ == '__main__':
    while True:
        notification.notify(
            title="**Please Drink Water Now!!",
            message="Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones.",
            app_icon = "D:\VS Code Files\Health Management\Icon.ico",
            timeout=10)
        time.sleep(60*60)