from tkinter import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



class StopWords:
    def __init__(self,root):
        self.root=root
        self.root.title("StopWords Removal")
        self.root.geometry("650x600")
        self.root.iconbitmap("logo404.ico")
        self.root.resizable(0,0)



        def on_enter1(e):
            but_generate['background']="black"
            but_generate['foreground']="cyan"
  
        def on_leave1(e):
            but_generate['background']="SystemButtonFace"
            but_generate['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"




#============================function==========================#
        
        def clear():
            text1.delete('1.0',"end")
            text2.delete('1.0',"end")

        def getdata():
            stop_words=set(stopwords.words('english'))
            x=text1.get('1.0',"end")
            words=x.split()
            for r in words:
               if not r in stop_words:
                   x=str(r.replace(",", " "))
                   text2.insert("end",x+" ")





# mainframe======================================================


        mainframe=Frame(self.root,width=650,height=600,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=644,heigh=265,relief="ridge",bd=3)
        firstframe.place(x=0,y=0)

        buttonframe=Frame(mainframe,width=644,heigh=65,relief="ridge",bd=3,bg="gray55")
        buttonframe.place(x=0,y=265)

        secondframe=Frame(mainframe,width=644,heigh=265,relief="ridge",bd=3)
        secondframe.place(x=0,y=330)





#button===============================================================
        
        but_generate=Button(buttonframe,width=15,text="Generate",font=('times new roman',14),cursor="hand2",command=getdata)
        but_generate.place(x=100,y=10)
        but_generate.bind("<Enter>",on_enter1)
        but_generate.bind("<Leave>",on_leave1)

        but_clear=Button(buttonframe,width=15,text="Clear",font=('times new roman',14),cursor="hand2",command=clear)
        but_clear.place(x=380,y=10)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


#firstframe ===========================================================

        scol=Scrollbar(firstframe ,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text1=Text(firstframe ,height=13,width=76,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black",bg="gray76",wrap="word")      
        text1.place(x=3,y=1)
        scol.config(command=text1.yview)


#secondframe ===========================================================

        scrol2=Scrollbar(secondframe ,orient="vertical")
        scrol2.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text2=Text(secondframe ,height=13,width=76,font=('times new roman',12),yscrollcommand=scrol2.set,relief="sunken",bd=3,fg="black",bg="gray76",wrap="word")      
        text2.place(x=3,y=1)
        scrol2.config(command=text2.yview)
    



if __name__=="__main__":
    root=Tk()
    StopWords(root)
    root.mainloop()