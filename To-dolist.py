# Store Values in Shelf
# Open Values when App Starts
import tkinter as tk
from tkinter import messagebox
import shelve

window = tk.Tk()
window.title("To-do List")

# frame structure
frame00 = tk.Frame(window)
frame01 = tk.Frame(window)
frame10 = tk.Frame(window)
frame11 = tk.Frame(window)

frame00.grid(row=0, column=0)
frame01.grid(row=0, column=1)
frame10.grid(row=1, column=0)
frame11.grid(row=1, column=1)

tasks = {}
tasklist = shelve.open("tasklist")

newTaskLabel = tk.Label(text="Enter New Task:", master=frame01)
newTaskLabel.pack(side=tk.LEFT)
currentTasksLabel = tk.Label(text="Current Tasks", master=frame11)
currentTasksLabel.pack(side=tk.TOP)


def loadOnOpen():
    tasklist = shelve.open("tasklist")
    for task in tasklist.keys():
        var = tk.IntVar()
        # need to read shelf and recreate checkbox widgets for program
        newTaskBox = tk.Checkbutton(master=frame11, text=task, variable=var, command=checkoffs)
        newTaskBox.pack(side=tk.TOP)
        tasks[newTaskBox] = var
    tasklist.close()


def newTaskFunction(event):
    newTaskName = newTaskEntry.get()
    var = tk.IntVar()
    newTaskBox = tk.Checkbutton(
        master=frame11, text=newTaskName, variable=var, command=checkoffs
    )
    newTaskBox.pack(side=tk.TOP)
    tasks[newTaskBox] = var
    newTaskEntry.delete(0, tk.END)
    newTaskEntry.bind("<Return>", printTask)


def checkoffs():
    # Could this be simplified since only one box will ever
    # be checked at a time?
    destroyList = []
    for i, v in tasks.items():
        if v.get() == 1:
            destroyList.append(i)

    for item in destroyList:
        item.destroy()


def finalSave():
    tasklist = shelve.open("tasklist")
    for key, value in tasks.items():
        taskName = key.cget('text')
        tasklist[taskName] = var.get()

    tasklist.close()

def printTask(event):
    print(len(tasks))


newTaskEntry = tk.Entry(frame01)
newTaskEntry.pack()
newTaskEntry.bind("<Return>", newTaskFunction)

window.protocol("WM_DELETE_WINDOW", finalSave)


loadOnOpen()

tk.mainloop()
