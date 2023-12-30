import tkinter as tk
from tkinter import ttk
import os

# 
system_state = False 
def update_timer():
    global remaining_seconds
    global system_state 
    if system_state == False:
        return
    if remaining_seconds > 0:
        remaining_seconds -= 1
        time_str = f"{remaining_seconds // 3600:02d}:{(remaining_seconds % 3600) // 60:02d}:{remaining_seconds % 60:02d}"
        timer_label.config(text=time_str)
        root.after(1000, update_timer)
    else:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def start_timer():
    global remaining_seconds
    global system_state 
    hours = int(hour_combo.get())
    minutes = int(minute_combo.get())
    remaining_seconds = hours * 3600 + minutes * 60
    system_state = True
    update_timer()

def reset_timer():
    global remaining_seconds
    global system_state
    system_state = False
    remaining_seconds = 0
    timer_label.config(text="00:00:00")




root = tk.Tk()
root.title("休眠計時器")
root.configure(bg='light blue')  # 設置背景顏色
# 初始化樣式
style = ttk.Style()
style.configure('TFrame', background='light blue')
style.configure('TButton', background='light blue')
style.configure('TLabel', background='light blue')
remaining_seconds = 0

ttk.Label(root, text="選擇時間後系統將進入休眠模式:", background='light blue').pack(pady=10)

# 時間選擇容器
time_frame = ttk.Frame(root, style='TFrame')
time_frame.pack(pady=5)

hour_lable = ttk.Label(time_frame, text="時:", style='TLabel')
hour_lable.pack(side=tk.LEFT, padx=5)

hour_combo = ttk.Combobox(time_frame, values=list(range(24)), width=5)
hour_combo.pack(side=tk.LEFT, padx=5)
hour_combo.set("0")

minute_label = ttk.Label(time_frame, text="分:", style='TLabel')
minute_label.pack(side=tk.LEFT, padx=5)

minute_combo = ttk.Combobox(time_frame, values=list(range(60)), width=5)
minute_combo.pack(side=tk.LEFT, padx=5)
minute_combo.set("10")

timer_label = ttk.Label(root, text="00:00:00", font=("Helvetica", 30), style='TLabel')
timer_label.pack(pady=20)

# 按鈕容器
button_frame = ttk.Frame(root, style='TFrame')
button_frame.pack(pady=10)

ttk.Button(button_frame, text="開始計時", command=start_timer, style='TButton').pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="重新開始", command=reset_timer, style='TButton').pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="取消", command=root.destroy, style='TButton').pack(side=tk.LEFT, padx=5)

root.mainloop()
