from tkinter import *
from tkinter.ttk import *
import pyshorteners

def adfly(url):
    adfly_txt.delete(0,END)
    key = input("Enter API Key .. ")
    user_id = input("Enter User ID .. ")
    s = pyshorteners.Shortener(api_key=key, user_id=user_id, type='int')
    result = s.adfly.short(url)
    adfly_txt.insert(0,result)



def clicked():
    url = targetURLtxt.get()
    if adfly_chk_state.get():
        adfly(url)


window = Tk()
window.title('URL Shortner')
window.geometry('600x500')

txt_width = 50
default_checkbox = False

targetURLlbl = Label(window, text='URL')
targetURLtxt = Entry(window, width=50)
targetURLbtn = Button(window, text='Short it!', command=clicked)
targetURLlbl.grid(column=0, row=0)
targetURLtxt.grid(column=1, row=0)
targetURLbtn.grid(column=2, row=0)

adfly_chk_state = BooleanVar()
adfly_chk_state.set(default_checkbox)
adfly_chk = Checkbutton(window,text='Adf.ly', var=adfly_chk_state)
adfly_txt = Entry(window, width=txt_width)
adfly_chk.grid(column=0,row=1)
adfly_txt.grid(column=1, row=1)

bitly_chk_state = BooleanVar()
bitly_chk_state.set(default_checkbox)
bitly_chk = Checkbutton(window,text='Bit.ly', var=bitly_chk_state)
bitly_txt = Entry(window, width=txt_width)
bitly_chk.grid(column=0,row=2)
bitly_txt.grid(column=1, row=2)

chilpit_chk_state = BooleanVar()
chilpit_chk_state.set(default_checkbox)
chilpit_chk = Checkbutton(window,text='Chilp.it', var=chilpit_chk_state)
chilpit_txt = Entry(window, width=txt_width)
chilpit_chk.grid(column=0,row=3)
chilpit_txt.grid(column=1, row=3)

clckru_chk_state = BooleanVar()
clckru_chk_state.set(default_checkbox)
clckru_chk = Checkbutton(window,text='Clck.ru', var=clckru_chk_state)
clckru_txt = Entry(window, width=txt_width)
clckru_chk.grid(column=0,row=4)
clckru_txt.grid(column=1, row=4)

cuttly_chk_state = BooleanVar()
cuttly_chk_state.set(default_checkbox)
cuttly_chk = Checkbutton(window,text='Cutt.ly', var=cuttly_chk_state)
cuttly_txt = Entry(window, width=txt_width)
cuttly_chk.grid(column=0,row=5)
cuttly_txt.grid(column=1, row=5)

dagd_chk_state = BooleanVar()
dagd_chk_state.set(default_checkbox)
dagd_chk = Checkbutton(window,text='Da.gd', var=dagd_chk_state)
dagd_txt = Entry(window, width=txt_width)
dagd_chk.grid(column=0,row=6)
dagd_txt.grid(column=1, row=6)

gitio_chk_state = BooleanVar()
gitio_chk_state.set(default_checkbox)
gitio_chk = Checkbutton(window,text='Git.io', var=gitio_chk_state)
gitio_txt = Entry(window, width=txt_width)
gitio_chk.grid(column=0,row=7)
gitio_txt.grid(column=1, row=7)

isgd_chk_state = BooleanVar()
isgd_chk_state.set(default_checkbox)
isgd_chk = Checkbutton(window,text='is.gd', var=isgd_chk_state)
isgd_txt = Entry(window, width=txt_width)
isgd_chk.grid(column=0,row=8)
isgd_txt.grid(column=1, row=8)

nullpointer_chk_state = BooleanVar()
nullpointer_chk_state.set(default_checkbox)
nullpointer_chk = Checkbutton(window,text='NullPointer', var=nullpointer_chk_state)
nullpointer_txt = Entry(window, width=txt_width)
nullpointer_chk.grid(column=0,row=8)
nullpointer_txt.grid(column=1, row=8)

osdb_chk_state = BooleanVar()
osdb_chk_state.set(default_checkbox)
osdb_chk = Checkbutton(window,text='Os.db', var=osdb_chk_state)
osdb_txt = Entry(window, width=txt_width)
osdb_chk.grid(column=0,row=9)
osdb_txt.grid(column=1, row=9)

owly_chk_state = BooleanVar()
owly_chk_state.set(default_checkbox)
owly_chk = Checkbutton(window,text='Ow.ly', var=owly_chk_state)
owly_txt = Entry(window, width=txt_width)
owly_chk.grid(column=0,row=10)
owly_txt.grid(column=1, row=10)

post_chk_state = BooleanVar()
post_chk_state.set(default_checkbox)
post_chk = Checkbutton(window,text='Po.st', var=post_chk_state)
post_txt = Entry(window, width=txt_width)
post_chk.grid(column=0,row=11)
post_txt.grid(column=1, row=11)

qpsru_chk_state = BooleanVar()
qpsru_chk_state.set(default_checkbox)
qpsru_chk = Checkbutton(window,text='Qps.ru', var=qpsru_chk_state)
qpsru_txt = Entry(window, width=txt_width)
qpsru_chk.grid(column=0,row=12)
qpsru_txt.grid(column=1, row=12)

shortcm_chk_state = BooleanVar()
shortcm_chk_state.set(default_checkbox)
shortcm_chk = Checkbutton(window,text='Short.cm', var=shortcm_chk_state)
shortcm_txt = Entry(window, width=txt_width)
shortcm_chk.grid(column=0,row=13)
shortcm_txt.grid(column=1, row=13)

tinycc_chk_state = BooleanVar()
tinycc_chk_state.set(default_checkbox)
tinycc_chk = Checkbutton(window,text='Tiny.cc', var=tinycc_chk_state)
tinycc_txt = Entry(window, width=txt_width)
tinycc_chk.grid(column=0,row=14)
tinycc_txt.grid(column=1, row=14)

tinyurlcom_chk_state = BooleanVar()
tinyurlcom_chk_state.set(default_checkbox)
tinyurlcom_chk = Checkbutton(window,text='TinyURL.com', var=tinyurlcom_chk_state)
tinyurlcom_txt = Entry(window, width=txt_width)
tinyurlcom_chk.grid(column=0,row=15)
tinyurlcom_txt.grid(column=1, row=15)




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
window.configure(bg='#ECECEC')
window.mainloop()