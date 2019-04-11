from tkinter import *
#import main
import database_1003 as f
import funs
import tkinter as tk
import PIL.Image
import PIL.ImageTk


class Application(tk.Tk):
                                        #*arguments, **keywordarguments(pass through dictionary)
    def __init__(self, *args, **kwargs): #the main functions that you want to run on start up
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self) #frame is like a window
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1) #weight determines who gets priority
        container.grid_columnconfigure(0, weight =1)

    
        self.frames = {}

        for F in (FirstPage, StartPage, PageOne, PageTwo, PageTwoA, PageTwoB, PageTwoC, PageTwoD,
                  PageThree, PageFour, PageFive, PageSix):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky = "nsew")

        self.show_frame(FirstPage)



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() #raise frame to the front


def qf(param):
    print(param)


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        image = PIL.Image.open("fflogo.png")
        image = image.resize((100,100), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 20)

        
        label = tk.Label(self, text="WELCOME TO FOOD FINDER!", bg = '#ffdb4d', fg = 'white',
                         font=('Arial', 15, 'bold' )) 
        label.pack(padx=10)

        label1 = tk.Label(self, text="")
        label1.pack()
        
        button = tk.Button(self, text= "Find food now!",
                            font=('Arial', 10, 'bold'), width = 20, height = 1, pady = 10, bg = 'white', fg = '#ffdb4d',
                            command = lambda: controller.show_frame(StartPage)) #goes to start page
        button.pack()
#===============================================================================================
class StartPage(tk.Frame):  

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        image = PIL.Image.open("fflogo.png")
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 10)
        
        label = tk.Label(self, text="WELCOME TO FOOD FINDER!", bg = '#ffdb4d', fg = 'white',
                         font=('Arial', 15, 'bold' ))
        label.pack(pady=10,padx=10)


        button1 = tk.Button(self, text= "1. Search for food you want to eat.",
                            width = 50, height = 1, pady = 10,
                            command = lambda: controller.show_frame(PageOne))
        button1.pack()
    #===============================================================================
        button2 = tk.Button(self, text= "2. Search food by stall name.",
                            width = 50, height = 1, pady = 10,
                            command = lambda: controller.show_frame(PageTwo))
        button2.pack()
    #===============================================================================
        button3 = tk.Button(self, text= "3. Search food by Cuisine.",
                            width = 50, height = 1, pady = 10,
                            command = lambda: controller.show_frame(PageThree))
        button3.pack()
    #================================================================================
        button4 = tk.Button(self, text= "4. Search food by Food Type.",
                            width = 50, height = 1, pady = 10,
                            command = lambda: controller.show_frame(PageFour))
        button4.pack()
    #================================================================================
        button5 = tk.Button(self, text= "5. Search for nearest canteen.",
                            width = 50, height = 1, pady = 10,
                            command = lambda: controller.show_frame(PageFive))
        button5.pack()
    #================================================================================
        button6 = tk.Button(self, text= "6. Search for canteen by price.",
                            width = 50, height = 1, pady = 10,
                            command = lambda: controller.show_frame(PageSix))
        button6.pack()
    #===============================================================================
        button7 = tk.Button(self, text= "View the entire Menu",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.showAll()))
        button7.pack()
    #===============================================================================
        label1 = tk.Label(self, text="")
        label1.pack()
    #===============================================================================
        button8 = tk.Button(self, text= "Quit",
                            width = 20, height = 1, font = ('Arial', 10, 'bold'), pady = 10, bg = 'white', fg = '#ffdb4d',
                            command = quit)
        button8.pack()





#======================================================================================================
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        image = PIL.Image.open("fflogo.png")
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 10)
        
        label = tk.Label(self, text="1. Search for the food you want to eat.",
                         font=('Arial', 10, 'bold' ))
        label.pack(pady=10,padx=10)
        

        self.search_food = Entry(self, width = 30)#entry box
        self.search_food.pack()
        #x = f.foodName(str(self.search_food.get()))

        label1 = tk.Label(self, text="")
        label1.pack()

        submit_button = tk.Button(self, text = "Submit",
                                  width = 20, height = 1, pady = 10,
                                  command = lambda: qf(f.foodName(str(self.search_food.get()))))
        submit_button.pack(side = tk.LEFT, padx = 50, pady = 0)                                   
        
        """self.text = Text(self, width =35, height =5, wrap = WORD) #message to be printed out
        self.text.pack()"""

  
        button1 = tk.Button(self, text= "Back to Home",
                                width = 20, height = 1, pady = 10, bg = '#ffdb4d', fg = 'white',
                                command = lambda: controller.show_frame(StartPage))
        button1.pack(side = tk.LEFT, padx = 50, pady = 0)



        
#======================================================================================================
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = PIL.Image.open("fflogo.png")
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 10)
        
        label = tk.Label(self, text="2. Search food by Stall Name.",
                         font=('Arial', 10, 'bold' )) #,font=LARGE_FONT
        label.pack(pady=10,padx=10)

        

        button1 = tk.Button(self, text = "Chicken Rice",
                            width = 50, height = 1,
                            command = lambda: qf(f.stallName("Chicken Rice")))
                            
                            
                                                
                            
        button1.pack()

        button2 = tk.Button(self, text = "Ayam Penyet",
                            width = 50, height = 1,
                            command = lambda: qf(f.stallName("Ayam Penyet")))
        button2.pack()

        button3 = tk.Button(self, text = "Mixed Veg Rice",
                            width = 50, height = 1,
                            command = lambda: qf(f.stallName("Mixed Veg Rice")))
        button3.pack()

        button4 = tk.Button(self, text = "Waffle",
                            width = 50, height = 1,
                            command = lambda: qf(f.stallName("Waffle 11")))
        button4.pack()

        button5 = tk.Button(self, text = "Golden Kitchen",
                            width = 50, height = 1,
                            command = lambda: qf(f.stallName("Golden Kitchen")))
        button5.pack()

        button6 = tk.Button(self, text = "Menya Takashi",
                            width = 50, height = 1,
                            command = lambda: qf(f.stallName("Menya Takashi")))
        button6.pack()

        button7 = tk.Button(self, text = "Ban Mian",
                            width = 50, height = 1,
                            command = lambda: qf(f.stallName("Ban Mian")))
        button7.pack()

        button8 = tk.Button(self, text = "Korean Stall",
                            width = 50, height = 1,
                            command = lambda: controller.show_frame(PageTwoA))
        button8.pack()

        button9 = tk.Button(self, text = "Mala Stall",
                            width = 50, height = 1,
                            command = lambda: controller.show_frame(PageTwoB))
        button9.pack()

        button10 = tk.Button(self, text = "Indian Stall",
                             width = 50, height = 1,
                            command = lambda: controller.show_frame(PageTwoC))
        button10.pack()

        button11 = tk.Button(self, text = "Japanese Stall",
                             width = 50, height = 1,
                            command = lambda: controller.show_frame(PageTwoD))
        button11.pack()

        button12 = tk.Button(self, text = "Ananda Kitchen",
                             width = 50, height = 1,
                            command = lambda: controller.show_frame(PageTwoD))
        button12.pack()

        button13 = tk.Button(self, text = "Pizza Hut",
                             width = 50, height = 1,
                            command = lambda: qf(f.stallName("Pizza Hut Express")))
        button13.pack()

        button14 = tk.Button(self, text = "Roasted Duck",
                             width = 50, height = 1,
                            command = lambda: qf(f.stallName("Cantonese Roasted Duck")))
        button14.pack()

        button15 = tk.Button(self, text = "Yong Tau Foo",
                             width = 50, height = 1,
                            command = lambda: qf(f.stallName("YTF")))
        button15.pack()

        label1 = tk.Label(self, text="")
        label1.pack()
                
        button0 = tk.Button(self, text= "Back to Home",
                            width = 20, height = 1, bg = '#ffdb4d', fg = 'white',
                            command = lambda: controller.show_frame(StartPage))
        button0.pack()

#======================================================================================================
class PageTwoA(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = PIL.Image.open("fflogo.png")
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 10)
        
        label = tk.Label(self, text="Korean Stall",
                         font=('Arial', 10, 'bold' )) #,font=LARGE_FONT
        label.pack(pady=10,padx=10)

       

        button2 = tk.Button(self, text = "Korean Cuisine",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Korean Cuisine")))
        button2.pack()                                   
        
        button3 = tk.Button(self, text = "Korean Canteen 9",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Korean 9")))
        button3.pack()

        button4 = tk.Button(self, text = "Korean Canteen 13",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Korean 13")))
        button4.pack()


        button5 = tk.Button(self, text = "Korean Tamarind",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Korean Tamarind")))
        button5.pack()

        button0 = tk.Button(self, text= "Other food stalls",
                            width = 50, height = 1, pady = 10,
                            command = lambda: controller.show_frame(PageTwo))
        button0.pack()

        label1 = tk.Label(self, text="")
        label1.pack()

        button1 = tk.Button(self, text= "Back to Home Page",
                            width = 20, height = 1, pady = 10, bg = '#ffdb4d', fg = 'white',
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

#======================================================================================================
class PageTwoB(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = PIL.Image.open("fflogo.png")
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 10)
        
        label = tk.Label(self, text="Mala Stall",
                         font=('Arial', 10, 'bold' )) #,font=LARGE_FONT
        label.pack(pady=10,padx=10)

       

        button2 = tk.Button(self, text = "Mala Canteen 1",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Mala Can1")))
        button2.pack()                                   
        
        button3 = tk.Button(self, text = "Mala Canteen 9",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Mala Can9")))
        button3.pack()

        button4 = tk.Button(self, text = "Mala NorthHill",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Mala NorthHill")))
        button4.pack()

        button5 = tk.Button(self, text = "Mala Pioneer",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Mala Pion")))
        button5.pack()

        button0 = tk.Button(self, text= "Other food stalls",
                            width = 50, height = 1, pady = 10,
                            command = lambda: controller.show_frame(PageTwo))
        button0.pack()

        label1 = tk.Label(self, text="")
        label1.pack()

        button1 = tk.Button(self, text= "Back to Home Page",
                            width = 20, height = 1, pady = 10, bg = '#ffdb4d', fg = 'white',
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

#======================================================================================================
class PageTwoC(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = PIL.Image.open("fflogo.png")
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 10)
        
        label = tk.Label(self, text="Indian Stall",
                         font=('Arial', 10, 'bold' )) #,font=LARGE_FONT
        label.pack(pady=10,padx=10)

       

        button2 = tk.Button(self, text = "Indian Cuisine",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Indian Cuisine")))
        button2.pack()                                   
        
        button3 = tk.Button(self, text = "Indian Canteen 16",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Indian 16")))
        button3.pack()

        button4 = tk.Button(self, text = "Indian Canteen 23",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Indian 23")))
        button4.pack()

        button0 = tk.Button(self, text= "Other food stalls",
                            width = 50, height = 1, pady = 10,
                            command = lambda: controller.show_frame(PageTwo))
        button0.pack()

        label1 = tk.Label(self, text="")
        label1.pack()

        button1 = tk.Button(self, text= "Back to Home Page",
                            width = 20, height = 1, pady = 10, bg = '#ffdb4d', fg = 'white',
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

#======================================================================================================
class PageTwoD(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = PIL.Image.open("fflogo.png")
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 10)
        
        label = tk.Label(self, text="Japanese Stall",
                         font=('Arial', 10, 'bold' )) #,font=LARGE_FONT
        label.pack(pady=10,padx=10)

       

        button2 = tk.Button(self, text = "Japanese Canteen 9",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Japanese Can9")))
        button2.pack()                                   
        
        button3 = tk.Button(self, text = "Japanese Canteen 11",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.stallName("Japanese Can11")))
        button3.pack()

        button4 = tk.Button(self, text = "Japanese Canteen 16",
                            width = 50, height = 1,pady = 10,
                            command = lambda: qf(f.stallName("Japanese Can16")))
        button4.pack()

        button5 = tk.Button(self, text = "Japanese South Spine",
                            width = 50, height = 1,pady = 10,
                            command = lambda: qf(f.stallName("Japanese SS")))
        button5.pack()


        button0 = tk.Button(self, text= "Other food stalls",
                            width = 50, height = 1, pady = 10,
                            command = lambda: controller.show_frame(PageTwo))
        button0.pack()

        label1 = tk.Label(self, text="")
        label1.pack()

        button1 = tk.Button(self, text= "Back to Home Page",
                            width = 20, height = 1, pady = 10, bg = '#ffdb4d', fg = 'white',
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

#===========================================================================================

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = PIL.Image.open("fflogo.png")
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 10)
        
        label = tk.Label(self, text="3. Search by Cuisine",
                         font=('Arial', 10, 'bold' )) #,font=LARGE_FONT
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text = "Chinese",
                            width = 50, height = 1, pady = 5,
                            command = lambda: qf(funs.sort_by_rank("Chinese")))
        button1.pack()

        button2 = tk.Button(self, text = "Indian",
                            width = 50, height = 1, pady = 5,
                            command = lambda: qf(funs.sort_by_rank("Indian")))
        button2.pack()

        button3 = tk.Button(self, text = "Indonesian",
                            width = 50, height = 1, pady = 5,
                            command = lambda: qf(funs.sort_by_rank("Indonesian")))
        button3.pack()

        button4 = tk.Button(self, text = "Italian",
                            width = 50, height = 1, pady = 5,
                            command = lambda: qf(funs.sort_by_rank("Italian")))
        button4.pack()

        button5 = tk.Button(self, text = "Japanese",
                            width = 50, height = 1, pady = 5,
                            command = lambda: qf(funs.sort_by_rank("Japanese")))
        button5.pack()

        button6 = tk.Button(self, text = "Korean",
                            width = 50, height = 1, pady = 5,
                            command = lambda: qf(funs.sort_by_rank("Korean")))
        button6.pack()

        label1 = tk.Label(self, text="")
        label1.pack()

        
        button0 = tk.Button(self, text= "Back to Home",
                            width = 20, height = 1, pady = 5, bg = '#ffdb4d', fg = 'white',
                            command = lambda: controller.show_frame(StartPage))
        button0.pack()

#===========================================================================================

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = PIL.Image.open("fflogo.png")
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 10)
        
        label = tk.Label(self, text="4. Food Type",
                         font=('Arial', 10, 'bold' )) #,font=LARGE_FONT
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text = "Non Vegetarian",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.foodType("Non-Vegetarian")))
        button1.pack()

        button2 = tk.Button(self, text = "Halal",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.foodType("Halal")))
        button2.pack()

        button3 = tk.Button(self, text = "Vegetarian",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(f.foodType("Vegetarian")))
        button3.pack()

        label1 = tk.Label(self, text="")
        label1.pack()

        
        button0 = tk.Button(self, text= "Back to Home",
                            width = 20, height = 1, pady = 10, bg = '#ffdb4d', fg = 'white',
                            command = lambda: controller.show_frame(StartPage))
        button0.pack()

#===========================================================================================

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = PIL.Image.open("fflogo.png")
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 10)
        
        label = tk.Label(self, text="5. Search for nearest canteen",
                         font=('Arial', 10, 'bold' )) #,font=LARGE_FONT
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text = "Select your current location",
                            width = 50, height = 1, pady = 10,
                            command = lambda: qf(funs.nearest_canteen_cumulative()))
                                                                                    #function that gives distance etc just from mouseclick.
        button1.pack()

        label1 = tk.Label(self, text="")
        label1.pack()
        
        button0 = tk.Button(self, text= "Back to Home",
                            width = 20, height = 1, pady = 10, bg = '#ffdb4d', fg = 'white',
                            command = lambda: controller.show_frame(StartPage))
        button0.pack()

#======================================================================================================
class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image = PIL.Image.open("fflogo.png")
        image = image.resize((50,50), PIL.Image.ANTIALIAS)
        photo = PIL.ImageTk.PhotoImage(image)
        panel = Label(self, image = photo)
        panel.image = photo
        panel.pack(pady = 10)
        
        label = tk.Label(self, text="6. Type in your budget.",
                         width = 50, height = 1,font=('Arial', 10, 'bold' )) 
        label.pack(pady=10,padx=10)

        self.budget = Entry(self)#entry box
        self.budget.pack()

        label1 = tk.Label(self, text="")
        label1.pack()
        
        submit_button = tk.Button(self, text = "Submit",
                                  width = 20, height = 1, pady = 10,
                                  command = lambda: qf(f.priceSort(float(self.budget.get()))))
        submit_button.pack(side = tk.LEFT, padx = 50, pady = 0)                                 
        
        
        
        label1 = tk.Label(self, text="")
        label1.pack()


        button1 = tk.Button(self, text= "Back to Home",
                            width = 20, height = 1, pady = 10, bg = '#ffdb4d', fg = 'white',
                            command = lambda: controller.show_frame(StartPage))
        button1.pack(side = tk.LEFT, padx = 50, pady = 0)


app = Application()
app.geometry("500x550")
app.mainloop()
