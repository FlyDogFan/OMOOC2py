# _*_ coding:utf-8 _*_

import sys
from Tkinter import *
from time import gmtime, strftime

reload(sys)# 这是什么意思?
sys.setdefaultencoding('utf-8')

class Mydaily(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.entrything = Entry(master)
        self.entrything.pack(ipadx=200, side=TOP)
        self.contents = StringVar()
        self.entrything["textvariable"] = self.contents
                
        #self.existcontents = StringVar()
        self.showcontents = Text(height=20, width = 500)        
        self.showcontents.pack()
        
        self.entrything.bind('<Key-Return>',self.read_and_save)

        self.quit = Button(master, text="quit", command=self.cancel)
        self.quit.pack(pady=5, side=BOTTOM)
        
    def  read_and_save(self, event):
         self.read_contents(event)
         self.save_and_print_contents(event)
          

    def save_and_print_contents(self, event):
        with open('diary.md','a') as self.f:
            now = strftime("%Y年%m月%d日 %H:%M:%S", gmtime())
            self.f.write("%s\n\n %s\n\n" %(now, self.contents.get()))
            self.f.close()
        print "This is your input --->", self.contents.get()
        self.entrything.delete(0,END)          #回车后,输入框清零.
        #self.entrything.focus_set()             #什么用啊?

    def read_contents(self, event):
        lines = self.contents.get()
        self.showcontents.insert(END, lines+'\n')
        self.f.close()

    def cancel(self):
        self.master.destroy()
    

def main():
    root = Tk()
    mydaily = Mydaily(master=root)
    mydaily.master.title('Mydaily')
    mydaily.master.geometry('640x480')# size copy from @picklecai
    mydaily.mainloop()

if __name__=="__main__":
    main()
