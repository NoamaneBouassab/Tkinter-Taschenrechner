import tkinter as tk
import webbrowser


class Rechner : 
    def __init__(self):
    
        self.Root = tk.Tk()
        self.Root.title("Rechner")
        self.Root.geometry("340x350")
        self.Root.resizable(width=False, height=False)
        self.Root.config(bg="#A9A9A9")

        BtnFont = "Arial 20 bold"



    



        self.MyEntry = tk.Entry(self.Root,bd=10, width=20, font="Arial 22",bg="white")
        self.MyEntry.grid(row=0,column=0,columnspan=4)
        
        self.Number7 = tk.Button(self.Root,text="7",font= BtnFont,bd=10,height=1,width=3,command=lambda: self.Click(7))
        self.Number7.grid(row=1,column=0)

        self.Number8 = tk.Button(self.Root,text="8",font= BtnFont,bd=10,height=1,width=3,command=lambda: self.Click(8))
        self.Number8.grid(row=1,column=1)

        self.Number9 = tk.Button(self.Root,text="9",font= BtnFont,bd=10,height=1,width=3,command=lambda: self.Click(9))
        self.Number9.grid(row=1,column=2)
        
        self.Number4 = tk.Button(self.Root,text="4",font= BtnFont,bd=10,height=1,width=3,command=lambda: self.Click(4))
        self.Number4.grid(row=2,column=0)

        self.Number5 = tk.Button(self.Root,text="5",font= BtnFont,bd=10,height=1,width=3,command=lambda: self.Click(5))
        self.Number5.grid(row=2,column=1)

        self.Number6 = tk.Button(self.Root,text="6",font= BtnFont,bd=10,height=1,width=3,command=lambda: self.Click(6))
        self.Number6.grid(row=2,column=2)

        self.Number1 = tk.Button(self.Root,text="1",font= BtnFont,bd=10,height=1,width=3,command=lambda: self.Click(1))
        self.Number1.grid(row=3,column=0)

        self.Number2 = tk.Button(self.Root,text="2",font= BtnFont,bd=10,height=1,width=3,command=lambda: self.Click(2))
        self.Number2.grid(row=3,column=1)

        self.Number3 = tk.Button(self.Root,text="3",font= BtnFont,bd=10,height=1,width=3,command=lambda: self.Click(3))
        self.Number3.grid(row=3,column=2)

        self.Number0 = tk.Button(self.Root,text="0",font= BtnFont,bd=10,height=1,width=3,command=lambda: self.Click(0))
        self.Number0.grid(row=4,column=0)


        self.Addition = tk.Button(self.Root,text="+",font= BtnFont,bd=10,height=1,width=3,bg="SeaGreen",command=lambda: self.Click("+"))
        self.Addition.grid(row=1,column=3)

        self.Subtraction = tk.Button(self.Root,text="-",font= BtnFont,bd=10,height=1,width=3,bg="SeaGreen",command=lambda: self.Click("-"))
        self.Subtraction.grid(row=2,column=3)

        self.Multiplication = tk.Button(self.Root,text="x",font= BtnFont,bd=10,height=1,width=3,bg="SeaGreen",command=lambda: self.Click("*"))
        self.Multiplication.grid(row=3,column=3)

        self.Division = tk.Button(self.Root,text="÷",font= BtnFont,bd=10,height=1,width=3,bg="SeaGreen",command=lambda: self.Click("/"))
        self.Division.grid(row=4,column=3)

        self.Delete = tk.Button(self.Root,text="C",font= BtnFont,bd=10,height=1,width=3,bg="Crimson")
        self.Delete.grid(row=4,column=1)

        self.Equal = tk.Button(self.Root,text="=",font= BtnFont,bd=10,height=1,width=3,bg="yellow")
        self.Equal.grid(row=4,column=2)

        self.Root.mainloop()


    def Click(self,number) : 
        self.MyEntry.insert(tk.END,number)


Mein_Rechner = Rechner()
    

