# Name: Muniba Maududi
# Date: 1/30/25
# Student ID: 101000747
#Type of document: Python Program
# Description: ICE2: Temperature Sensor Program Testing
from tkinter import *
from tkinter.tix import *
import sys

def validate_temp(value):
    try:
        temp= float(value)
        if -50 <= temp <= 150:
            return temp
        else:
            result.configure(text= "Error: Out-of-bound value detected.")
            return None
    except ValueError:
        result.configure(text= "Error: Invalid input detected.")
        return None

def temp_process():
    temp_list= []

    temp_value= [temp_1_entry.get(), temp_2_entry.get(), temp_3_entry.get(), temp_4_entry.get()]

    if all(value.strip() == "" for value in temp_value):
        result.configure(text= "Error: No input provided.")
        return None

    for value in temp_value:
        if value.strip() == "":
            continue  # Skip empty inputs

        temp = validate_temp(value)
        if isinstance(temp, str):  # Error message returned from validate_temp
            result.configure(text=temp)
            return  # Stop processing on first error

        temp_list.append(temp)

    if len(temp_list)==0:
        result.configure(text= "Warning! No valid temperature provided.")
        return

    min_temp= min(temp_list)
    max_temp= max(temp_list)
    avg_temp= round(sum(temp_list) / len(temp_list), 2)

    result.configure(text= f'Min:{min_temp} °C\nMax:{max_temp}°C\nAvg:{avg_temp}°C')

def temp_clear():
    temp_1_entry.delete(0,END)
    temp_2_entry.delete(0,END)
    temp_3_entry.delete(0,END)
    temp_4_entry.delete(0,END)
    result.configure(text= "")


def temp_exit():
    sys.exit()

window = Tk()
window.geometry("100x100")
window.title("Temperature Sensor Processor")
window.minsize(width= 700, height= 250)

temp_1= Label(window, text= "Temperature 1: ")
temp_1.grid(row= 0, column= 0, padx= 10, pady= 10)
temp_1_entry= Entry()
temp_1_entry.grid(row= 0, column= 1, padx= 10, pady= 10)

temp_2= Label(window, text= "Temperature 2: ")
temp_2.grid(row= 1, column= 0, padx= 10, pady=10)
temp_2_entry= Entry()
temp_2_entry.grid(row= 1, column= 1, padx= 10, pady= 10)

temp_3= Label(window, text= "Temperature 3: ")
temp_3.grid(row= 0, column= 2, padx= 10, pady=10)
temp_3_entry= Entry()
temp_3_entry.grid(row= 0, column= 3, padx= 10, pady= 10)

temp_4= Label(window, text= "Temperature 4: ")
temp_4.grid(row= 1, column= 2, padx= 10, pady=10)
temp_4_entry= Entry()
temp_4_entry.grid(row= 1, column= 3, padx= 10, pady= 10)

result= Label(window, font= ("Times New Roman", 15, "bold"), text= "RESULT: ")
result.grid(row= 2, column= 1, padx= 10, pady= 10, columnspan= 2)

btn_process= Button(window, text="Process", width= 15, command= temp_process)
btn_process.grid(row= 3, column= 1, padx= 10, pady= 10)

btn_clear= Button(window, text="Clear", width= 15, command= temp_clear)
btn_clear.grid(row= 3, column= 2, padx= 10, pady= 10)

btn_exit= Button(window, text="Exit", width= 15, command= temp_exit)
btn_exit.grid(row= 3, column= 3, padx= 10, pady= 10)

window.mainloop()
