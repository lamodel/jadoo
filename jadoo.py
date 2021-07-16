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


#creating title:
lblTitle = Label(root, text="JADOO",font=50)
lblTitle.place(x=150,y=100)
#end title

#creating input:
userInpt = Entry(root, bd=5,width=30)
userInpt.place(x=86,y=130)

#creating button:
clickBtn = Button(root, text="SEARCH",padx=20,pady=5,command=search)
clickBtn.place(x=130,y=180)

root.mainloop()
