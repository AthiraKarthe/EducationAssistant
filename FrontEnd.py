import tkinter as tk
tko = tk.Tk()
from  tkinter import filedialog
import tkinter.font as tkFont
import BackEnd_01

# Opening Page:
tko.name = 'Educational Assistant'

def CreateSummaryWindow():
    sum = tk.Toplevel(tko)
    sum.geometry('300x300')
    # Summary Page:


    label = tk.Label( sum, text='Path' ,font = tkFont.Font(family="Helvetica", size=10, weight=tkFont.BOLD,slant=tkFont.ITALIC))
    LinkField = tk.Entry(sum)
    label1 = tk.Label(sum,text='Percentage',font = tkFont.Font(family="Helvetica", size=10, weight=tkFont.BOLD,slant=tkFont.ITALIC))
    PercentageField = tk.Entry(sum)

    SubmitButton = tk.Button(sum, text = 'Summarize', width = 25, command = lambda:BackEnd_01.Summarize(LinkField.get(),int(PercentageField.get())), background = 'Moccasin',fg='Black',activeforeground='white',activebackground='black')
    label.place(x=50,y=50)
    LinkField.place(x=150,y=50)
    label1.place(x=50,y=100)
    PercentageField.place(x=150,y=100)
    SubmitButton.place(x=50,y=150)
    sum.mainloop()

def CreateQuestionWindow():
    que = tk.Toplevel(tko)
    passLabel = tk.Label(que,text='Passage:',font = tkFont.Font(family="Helvetica", size=10, weight=tkFont.BOLD,slant=tkFont.ITALIC))
    passageField = tk.Text(que,height = 20,width=30)
    queLabel = tk.Label(que,text='Query:',font = tkFont.Font(family="Helvetica", size=10, weight=tkFont.BOLD,slant=tkFont.ITALIC))
    queryField = tk.Text(que,height=3,width=30)
    answerButton = tk.Button(que,text= 'Answer!',background = 'Moccasin',fg='Black',activeforeground='white',activebackground='black')
    answerLabel = tk.Label(que,text='answer displays here')
    que.geometry('700x600')
    passLabel.place(x=100,y=80)
    passageField.place(x=100,y=100)
    queLabel.place(x=400,y=80)
    queryField.place(x=400,y=100)
    answerButton.place(x=400,y=400)
    answerLabel.place(x=400,y=200)


label3 = tk.Label(tko,text = 'What can I do for you?', font = tkFont.Font(family="Helvetica", size=10, weight=tkFont.BOLD,slant=tkFont.ITALIC))
tko.pack_propagate(0)
tko.geometry("400x300")
tko.resizable(0, 0)
button1 = tk.Button(tko, text = 'Summary Generation', command = CreateSummaryWindow, fg='Black',bg='Moccasin',activeforeground='white',activebackground='black')
button2 = tk.Button(tko, text = 'Question Answering', command = CreateQuestionWindow,fg='Black',bg='Moccasin',activeforeground='white',activebackground='black')
label3.place(x=125,y=100)
button1.place(x=50,y=150)
button2.place(x=200,y=150)
tko.mainloop()
