import tkinter as tk

#use a boolean variable to know if the time is running ot not
running = False

#time variables set to 0
hours, minutes, seconds = 0, 0, 0

#global used to modify variables outside funcs
#we can also use class and subclass frame

#FUNCTIONS
#start func
def start():
    global running
    if not running:
        update()
        running = True

#pause func
def pause():
    global running
    if running:
        #cancel updating time by using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

#reset func
def reset():
    global running
    if running:
        #cancel updating time by using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False
    #set variables back to zero
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    #output format for setting back to zero
    stopwatch_label.config(text='00:00:00')

#update func
def update():
    #update secs to mins and smly mins to hrs
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    #formatting time
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    #update by 1000ms = 1s
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)

    #after 1000ms update func is executed
    #update_time var to cancel or pause time using after_cancel
    global update_time
    update_time = stopwatch_label.after(1000, update)

#main window format
root = tk.Tk()
root.geometry('485x220')
root.title('Stopwatch')

#display time format
stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 80))
stopwatch_label.pack()

#buttons for start, pause, reset, quit buttons
start_button = tk.Button(text='Start', height=5, width=7, font=('Arial', 20), command=start)
start_button.pack(side=tk.LEFT)

pause_button = tk.Button(text='Pause', height=5, width=7, font=('Arial', 20), command=pause)
pause_button.pack(side=tk.LEFT)

reset_button = tk.Button(text='Reset', height=5, width=7, font=('Arial', 20), command=reset)
reset_button.pack(side=tk.LEFT)

quit_button = tk.Button(text='Quit', height=5, width=7, font=('Arial', 20), command=root.quit)
quit_button.pack(side=tk.LEFT)

#mainloop
root.mainloop()
