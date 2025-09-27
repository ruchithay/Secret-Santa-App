from random import *
from tkinter import *
from tkinter import messagebox
from csv import *
with open('santadata.csv','w',newline='') as claus:
        csvwrite=writer(claus)
        csvwrite.writerow(['Santas','Receivers'])
        peop=[]
        print("Enter names of the participants one by one. Enter done after completion.")
        while True:
            user_inpt = input()
            if user_inpt == 'done':
                break
            peop.append(user_inpt)
        print("Processing...")
        santas=set();lucky=set()
        magic=Tk()
        magic.title('Secret Santa')
        magic.geometry('750x500')
        magic.config(bg='pink')
        c=0
        def find():
            global c
            ranper=choice(peop)
            if name.get().title() in santas:
                '''lab=Label(magic,text='Your turn is over!',font=('Calisto MT',15,'bold'),bg='pink')
                lab.place(x=325,y=375)'''
                messagebox.showwarning('Oops!','Your turn is over!')
            elif name.get().lower() not in peop:
                '''lab=Label(magic,text='Please enter a valid name!',font=('Calisto MT',15,'bold'),bg='pink')
                lab.place(x=325,y=375)'''
                messagebox.showerror('Try again','Please enter a valid name!')
            else:
                while ranper in lucky or ranper==name.get().lower():
                    ranper=choice(peop)
                c+=1
                lucky.add(ranper)
                santas.add(name.get().lower())
                csvwrite.writerow([name.get(),ranper])
                lab = Label(magic, text=ranper, font=('Calisto MT', 15, 'bold'), fg='green',bg='pink')
                lab.place(x=325, y=400)
        def generic_func(func_lst):
            def calling_func(*args,**kwargs):
                for f in func_lst:
                    f(*args,**kwargs)
            return calling_func
        filename=PhotoImage(file='gift.png')
        def vanish():
            if c>=len(peop):
                magic.destroy()
        img=Button(magic,image=filename,pady=20,command=find)
        name = Entry(magic, width=20, bg='green', fg='white', font=('Century', 15, 'italic'), justify=CENTER)
        nlabe=Label(magic,text='Enter your name',fg='red',bg='pink',font=('Calisto MT',15,'bold'),pady=10)
        click=Label(text='Click to find out to whom you are the secret santa!',fg='red',font=('Century',15,'bold'),pady=10,bg='pink')
        clr=Button(magic,text='CLEAR',bg='green',fg='white',font=('Century',10,'bold'),activebackground='red',activeforeground='white',command=generic_func([lambda:name.delete(0, END),lambda:Label(magic,width=500,bg='pink').place(x=300,y=400),vanish]))
        nlabe.pack()
        name.pack()
        click.pack()
        img.pack()
        Label(magic,bg='pink').pack()
        clr.pack(side=BOTTOM)
        magic.mainloop()