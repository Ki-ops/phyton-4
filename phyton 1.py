from tkinter import*
root=Tk()

root.title("fibonacci")
root.geometry("400x400")
label=Label(root,text="fibonacci series")
label.place(relx=0.5,rely=0.2,anchor=CENTER)

def fibo():
    num=10
    first=0
    second=1
    sum=0
    counter=1
    while counter<=num:
        label["text"]+=str(sum)+" "
        counter=counter+1
        first=second
        second=sum
        sum=first+second 
        
btn=Button(root,text="fibonacci series",command=fibo)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)


root.mainloop()
