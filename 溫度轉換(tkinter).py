# -*- coding: utf-8 -*-
import tkinter as tk

window = tk.Tk()
window.title('溫度轉換計算')
window.geometry('300x400')

def temperature():
    tempC=eval(tempc_entry.get())
    tempF=tempC*(9/5)+32
    result = ("華氏溫度是:%.1f"%(tempF))
    result_label.configure(text=result)
    
    
def reset():
    tempc_entry.delete(0,tk.END)
    result_label.configure(text="")
    
    
#攝氏溫度標籤與輸入   
tempc_label = tk.Label(window, text='攝氏溫度:', font='_ 30')
tempc_label.pack()

tempc_entry = tk.Entry(window, font='_ 30')
tempc_entry.pack()

# 顯示計算結果的label
result_label = tk.Label(window, font='_ 20')
result_label.pack()

#計算按鈕
calculate_btn = tk.Button(window, text='轉換', command=temperature, font=("Arial",20))
calculate_btn.pack()

#清除按鈕
reset_btn = tk.Button(window, text="重設", font=("Arial", 20),  command=reset)
reset_btn.pack() 


window.mainloop()