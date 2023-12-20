from tkinter import *


window_background_color = "#078282"
entry_background_color = "#339E66"
label_foreground_color = "#4409A4"


window =Tk()
window.config(bg=window_background_color)
window.title("BMI Calculator")
window.config(padx=20,pady=20)

def calculate():
    try:
        weight = float(my_entry.get())
        height = float(my_entry_2.get()) / 100

        if weight > 0 and height > 0:
            bmi = weight / height ** 2
            if bmi < 18.5:
                my_label_3.config(text=f"Your BMI is {bmi:.2f}. You are Underweight")
            elif 18.5 <= bmi < 25:
                my_label_3.config(text=f"Your BMI is {bmi:.2f}. You are Normal")
            elif 25 <= bmi < 30:
                my_label_3.config(text=f"Your BMI is {bmi:.2f}. You are Overweight")
            elif 30 <= bmi < 35:
                my_label_3.config(text=f"Your BMI is {bmi:.2f}. You are Obese")
            elif 35 <= bmi < 40:
                my_label_3.config(text=f"Your BMI is {bmi:.2f}. You are Severely Obese")
            elif bmi >= 40:
                my_label_3.config(text=f"Your BMI is {bmi:.2f}. You are Morbidly Obese")
        else:
            my_label_3.config(text="Please Enter a Valid Number")
    except ValueError:
        my_label_3.config(text="Please Enter a Valid Number")

#Label
my_label = Label(text="Enter Your Weight (kg)",)
my_label.config(bg=window_background_color, fg=label_foreground_color)
my_label.config(pady=5,padx=5)
my_label.grid(row=0,column=0)

my_label_2 = Label(text="Enter Your Heigth (cm)")
my_label_2.config(bg=window_background_color, fg=label_foreground_color)
my_label_2.config(padx=5,pady=5)
my_label_2.grid(row=1,column=0)

my_label_3 = Label(text="")
my_label_3.config(
    bg=window_background_color,
    fg=label_foreground_color
)
my_label_3.grid(row=3, column=0, columnspan=2)


#Entry
my_entry = Entry(width=15)
my_entry.config(bg=entry_background_color)
my_entry.grid(row=0,column=1)

my_entry_2 = Entry(width=15)
my_entry_2.config(bg=entry_background_color)
my_entry_2.grid(row=1,column=1)

#button
my_button = Button(text="Calculate",command=calculate)
my_button.grid(row=2, column=0, columnspan=2)
my_button.config(
    bg=entry_background_color,
    fg=label_foreground_color
)



window.mainloop()