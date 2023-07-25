from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_time):
    alarm_rang = False
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    ring_time = 60
    
    while not alarm_rang:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The current date is: " + date)
        print(now + "\n")

        if now == set_alarm_time or set_alarm_time < now:
            print("Time to Wake Up!")
            alarm_rang = True
            while ring_time > 0:
                winsound.PlaySound("alert.wav", winsound.SND_ASYNC)
                time.sleep(1)
                ring_time -= 1

def get_time():
    set_alarm_time = f"{hour.get()}:{min.get()}:00"
    alarm(set_alarm_time)  


clock = Tk()
clock.configure(bg='black')
clock.title("Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text= "Enter time in 24 hour format!",
                    fg="white", bg="black",
                    font="helvetica").place(x=60, y=120)

addTime = Label(clock, text="    H         M    ",
                font='helvetica', fg='yellow', bg='black').place(x=130)

setYourAlarm = Label(clock, text="Enter Time : ",
                    fg="yellow", bg='black',
                    relief="solid",
                    font=("helvetica",16,"bold"),).place(x=0, y=30)

# variables required to set the alarm(initialization)
hour = StringVar(clock)
min = StringVar(clock)

now = datetime.datetime.now().strftime("%H:%M:%S")
i = now.find(":")
hour.set(str(now[:i]))
min.set(str(now[i+1:i+3]))

hourTime = Entry(clock, textvariable=hour,
                 bg="#2E2E2E", fg='yellow',
                 width=5,
                 font=("helvetica",17,'bold'),
                 justify=CENTER).place(x=130, y=30)


minTime = Entry(clock, textvariable=min,
                bg="#2E2E2E", fg='yellow',
                width=5,
                font=('helvetica',17,'bold'),
                justify=CENTER).place(x=200, y=30)


# to get time input by user
submit = Button(clock, text="Set Alarm",
                fg="yellow", bg='black',
                width=10,
                command=get_time,
                relief=SUNKEN).place(x=150,y=70)


clock.mainloop()
