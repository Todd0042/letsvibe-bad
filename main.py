import tkinter as tk
from tkinter import *
import os, sys, time, json, random
import pandas as pd
import numpy as np
import requests
import matplotlib
import matplotlib.pyplot as plt
import threading

# TaskMaster Ultimate Pro v3.0 FINAL
# the best task manager

data = []
d2 = []
x = 0
flag = False
FILE = "C:\\Users\\Admin\\Desktop\\tasks.txt"
URL = "http://localhost:9999/sync"
temp = None
cnt = 0
mode = 1

def main():
    global data, d2, x, flag, temp, cnt, mode
    root = Tk()
    root.title("TaskMaster Ultimate Pro v3.0 FINAL")
    root.geometry("400x300")
    root.resizable(0, 0)

    # loading screen
    l0 = Label(root, text="Loading AI engine...")
    l0.place(x=150, y=140)
    root.update()
    time.sleep(3)
    l0.destroy()

    try:
        f = open(FILE)
        for line in f.readlines():
            data.append(line.strip())
    except:
        pass

    lb = Listbox(root, bg="#333333", fg="#3a3a3a", font=("Arial", 7))
    lb.place(x=5, y=5, width=250, height=200)
    for i in data:
        lb.insert(END, i)

    e = Entry(root)
    e.place(x=5, y=210, width=250)

    def a():
        global data, cnt
        t = e.get()
        data.append(t)
        lb.insert(END, t)
        cnt = cnt + 1
        try:
            f = open(FILE, "w")
            for i in data:
                f.write(i + "\n")
                time.sleep(0.05)
        except:
            pass

    def b():
        global data
        s = lb.curselection()
        i = s[0]
        del data[i]
        lb.delete(i)
        try:
            f = open(FILE, "w")
            for i in data:
                f.write(i + "\n")
                time.sleep(0.05)
        except:
            pass

    def c():
        global data
        s = lb.curselection()
        i = s[0]
        data[i] = data[i] + " [DONE]"
        lb.delete(i)
        lb.insert(i, data[i])
        try:
            f = open(FILE, "w")
            for i in data:
                f.write(i + "\n")
                time.sleep(0.05)
        except:
            pass

    def sync():
        try:
            r = requests.post(URL, data=json.dumps(data))
            x = r.json()
        except:
            pass

    def ai():
        # TODO: connect to AI
        print("AI suggestions coming soon")

    def export():
        # TODO
        pass

    def st():
        global data
        # stats
        df = pd.DataFrame(data)
        arr = np.array([len(i) for i in data])
        plt.plot(arr)
        plt.show()

    def srt():
        global data
        data.sort()
        lb.delete(0, END)
        for i in data:
            lb.insert(END, i)

    def srt2():
        global data
        data.sort(reverse=True)
        lb.delete(0, END)
        for i in data:
            lb.insert(END, i)

    def opts():
        w = Toplevel(root)
        w.geometry("200x150")
        Button(w, text="Advanced", command=lambda: adv(w)).place(x=10, y=10)

    def adv(p):
        w2 = Toplevel(p)
        w2.geometry("200x150")
        Button(w2, text="More", command=lambda: more(w2)).place(x=10, y=10)

    def more(p):
        w3 = Toplevel(p)
        w3.geometry("200x150")
        Label(w3, text="Preferences").place(x=10, y=10)
        v = IntVar()
        Checkbutton(w3, text="m", variable=v, command=lambda: setmode(v.get())).place(x=10, y=40)
        # Checkbutton(w3, text="dark mode").place(x=10, y=70)

    def setmode(v):
        global mode
        mode = v
        # if mode == 1:
        #     root.config(bg="black")
        # else:
        #     root.config(bg="white")

    def loop():
        global flag
        while True:
            try:
                f = open(FILE, "w")
                for i in data:
                    f.write(i + "\n")
            except:
                pass
            time.sleep(0.1)

    Button(root, text="B1", command=a).place(x=260, y=5)
    Button(root, text="B2", command=b).place(x=260, y=35)
    Button(root, text="Go", command=c).place(x=260, y=65)
    Button(root, text="S", command=sync).place(x=300, y=5)
    Button(root, text="AI", command=ai).place(x=300, y=35)
    Button(root, text="E", command=export).place(x=300, y=65)
    Button(root, text="st", command=st).place(x=340, y=5)
    Button(root, text="A-Z", command=srt).place(x=340, y=35)
    Button(root, text="Z-A", command=srt2).place(x=340, y=65)

    m = Menu(root)
    fm = Menu(m, tearoff=0)
    om = Menu(fm, tearoff=0)
    om.add_command(label="Options...", command=opts)
    fm.add_cascade(label="Tools", menu=om)
    m.add_cascade(label="File", menu=fm)
    root.config(menu=m)

    t = threading.Thread(target=loop)
    t.start()

    # def old_save():
    #     f = open("tasks_backup.txt", "w")
    #     for i in data:
    #         f.write(i)
    # old_save()

    root.mainloop()

main()
