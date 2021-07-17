from tkinter import *
import webbrowser

root = Tk()
root.title("JADOO")
root.wm_iconbitmap("images/jadoo.ico")
root.geometry("350x400")
root.minsize(350,400)
root.resizable(0,0)

#func:
def search():
    ggl = 'google'  
    srch = ("https://www.google.com/search?q="+f"{userInpt.get()}")
    print("Searching...")
    
    if srch == ggl:
        webbrowser.open_new(f'{ggl}')
    else:
        webbrowser.open_new(f'{srch}')

def clear():
    userInpt.delete(0,END)    

#creating title:
lblTitle = Label(root, text="JADOO",font=('Arial bold',20))
lblTitle.place(x=130,y=80)
#end title

#creating input:
userInpt = Entry(root, bd=5,width=30)
userInpt.insert(0,'search...')
userInpt.place(x=86,y=130)

#creating button:
clickBtn = Button(root, text="SEARCH",padx=20,pady=5,command=search)
clickBtn.place(x=80,y=180)


#clear button:
clsBtn = Button(root,text="CLEAR",padx=20,pady=5,command=clear)
clsBtn.place(x=190,y=180)

root.mainloop()
