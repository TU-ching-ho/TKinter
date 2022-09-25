import tkinter as tk
import math
window = tk.Tk()
window.title('BMI App')
window.geometry('600x400')
window.configure(background='white')
def calculate_bmi_number():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    print(height, weight, math.pow(height, 2))
    bmi_value = round(weight / math.pow(height/100, 2), 2)
    print(bmi_value)

    result = '你的 BMI 指數為：{} {}'.format(bmi_value, get_bmi_status_description(bmi_value))
    result_label.configure(text=result)
    
# 顯示評語
def get_bmi_status_description(bmi_value):
    if bmi_value < 18.5:
        return '體重過輕囉，多吃點！'
    elif bmi_value >= 18.5 and bmi_value < 24:
        return '體重剛剛好，繼續保持！'
    elif bmi_value >= 24 :
        return '體重有點過重囉，少吃多運動！'

# 清除
def reset():
    height_entry.delete(0,tk.END)
    weight_entry.delete(0,tk.END) 
    result_label.configure(text="")
# 大標題
header_label = tk.Label(window, text='BMI計算機', font='_ 30')
header_label.pack()

# 身高輸入區域
height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP, pady=10)

# 身高文字標籤
height_label = tk.Label(height_frame, text='身高(m)', font='_ 30')
height_label.pack(side=tk.LEFT)

# 身高輸入框
height_entry = tk.Entry(height_frame, font='_ 30')
#height_entry.insert(0, '0')
height_entry.pack(side=tk.LEFT)

# 體重輸入區域
weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP,pady=10)

# 體重文字標籤
weight_label = tk.Label(weight_frame, text='體重(kg)', font='_ 30')
weight_label.pack(side=tk.LEFT)

# 體重輸入框
weight_entry = tk.Entry(weight_frame, font='_ 30')
#weight_entry.insert(0, '0')
weight_entry.pack(side=tk.LEFT)

# 顯示計算結果的label
result_label = tk.Label(window, font='_ 20')
result_label.pack()

# 計算按鈕
calculate_btn = tk.Button(window, text='計算', command=calculate_bmi_number, font=("Arial", 20), background='blue')
calculate_btn.pack()

# 清除按鈕
reset_btn = tk.Button(window, text="重設", font=("Arial", 20), command=reset)
reset_btn.pack() 

window.mainloop()