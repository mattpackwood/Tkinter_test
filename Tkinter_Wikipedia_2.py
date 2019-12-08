#!/usr/bin/env python3
 2 import tkinter as tk
 3 
 4 class Application(tk.Frame):
 5 
 6     def __init__(self, master=None):
 7         super(Application, self).__init__(master)
 8         self.grid()  
 9         self.createWidgets()
10 
11     def createWidgets(self):
12         self.mondialLabel = tk.Label(self, text='Hello World')
13         self.mondialLabel.config(bg="#00ffff")
14         self.mondialLabel.grid()
15         self.quitButton = tk.Button(self, text='Quit', command=self.quit)
16         self.quitButton.grid()
17 
18 app = Application()
19 app.master.title('Sample application')
20 app.mainloop()
