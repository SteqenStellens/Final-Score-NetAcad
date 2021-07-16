__author__ = 'Avinash'
ModifyBy = 'Steqen Stellens'

import tkinter as tk
from functools import partial
def call_result(label_result,sum1,sum2,prj,sba,final):
    SumTest1 = (sum1.get())
    SumTest2 = (sum2.get())
    Project = (prj.get())
    SBA = (sba.get())
    FinalTest = (final.get())
    result = float(((float(SumTest1)+ float(SumTest2))*0.6666666667)+((float(Project)+float(SBA))*0.15)+(float(FinalTest)*0.6))
    label_result.config(text="Final Score %f" % result)
    return

root = tk.Tk()
root.geometry('400x200+100+200')
root.title('Calculator Final Score')
number1 = tk.DoubleVar()
number2 = tk.DoubleVar()
number3 = tk.DoubleVar()
number4 = tk.DoubleVar()
number5 = tk.DoubleVar()
labelTitle = tk.Label(root, text="Enter Your Score :").grid(row=0, column=2)
labelNum1 = tk.Label (root, text="Summary Test Part 1 ").grid(row=1, column=0)
labelNum2 = tk.Label (root, text="Summary Test Part 2 ").grid(row=2, column=0)
labelNum3 = tk.Label (root, text="Project             ").grid(row=3, column=0)
labelNum4 = tk.Label (root, text="SBA                 ").grid(row=4, column=0)
labelNum5 = tk.Label (root, text="Final Test          ").grid(row=5, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=8, column=2)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=2)
entryNum4 = tk.Entry(root, textvariable=number4).grid(row=4, column=2)
entryNum5 = tk.Entry(root, textvariable=number5).grid(row=5, column=2)
call_result = partial(call_result, labelResult, number1, number2, number3, number4, number5)
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=7, column=0)
root.mainloop()
