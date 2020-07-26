from tkinter import *
from tkinter.ttk import *

# def cli():
#     lbl.config(text=chk_state.get() )

window = Tk()
window.title('URL Shortner')
window.geometry('600x400')

# menu = Menu(window)
# new_item = Menu(menu, tearoff=0)
# new_item.add_command(label='configure')
# menu.add_cascade(label='File', menu=new_item)


targetURLlbl = Label(window, text='URL')
targetURLtxt = Entry(window, width=50)
targetURLbtn = Button(window, text='Short it!')
targetURLlbl.grid(column=0, row=0)
targetURLtxt.grid(column=1, row=0)
targetURLbtn.grid(column=2, row=0)





# lbl = Label(window, text= "bit.ly")
# lbl.grid(column=1,row=0)
#
# chk_state = BooleanVar()
# chk_state.set(True)
#
# chk = Checkbutton(window, text='Test Checkbutton', var=chk_state)
# chk.grid(column=0, row=0)

# txt = Entry(window,width=10)
# txt.grid(column=1,row=0)

# btn = Button(window, text="Click me", command=cli)
# btn.grid(column=2,row=0)




# window.config(menu=menu)
window.mainloop()