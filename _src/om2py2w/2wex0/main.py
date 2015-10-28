# _*_ coding:utf-8 _*_
from Tkinter import *
from time import gmtime, strftime

class App(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack(padx=10, ipadx=300, pady=10)
        self.contents = StringVar()
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>',
                              self.save_and_print_contents)
        
        self.showcontents = Label(textvariable=self.contents)
        self.showcontents.pack()

        self.quit = Button(master, text="quit", command=self.cancel)
        self.quit.bind()
        self.quit.pack(pady=5)
    
    def save_and_print_contents(self, event):
        with open('diary.md','a') as f:
            now = strftime("%Y年%m月%d日 %H:%M:%S", gmtime())
            f.write("%s\n\n %s\n\n" %(now, self.contents.get()))
            f.close()
        print "This is your input --->", self.contents.get()

    def cancel(self):
        self.master.destroy()


root = Tk()
app = App(master=root)
app.mainloop()
root.destroy()
