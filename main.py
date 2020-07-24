import pyshorteners

def invalid():
   print ("INVALID CHOICE!")

def Adfly():
    key = input("Enter API Key .. ")
    user_id = input("Enter User ID .. ")
    domain = input("Enter Domain")
    s = pyshorteners.Shortener(api_key=key, user_id=user_id,
                               domain=domain, type='int')
if __name__ == '__main__':

    menu = {"1":("adf.ly"),
            "2":("Bit.ly"),
            "3": ("Chilp.it"),
            "4": ("Clck.ru"),
            "5": ("Cutt.ly"),
            "6": ("Da.gd"),
            "7": ("Git.io"),
            "8": ("Is.gd"),
            "9": ("NullPointer"),
            "10": ("Os.db"),
            "11": ("Ow.ly"),
            "12": ("Po.st"),
            "13": ("Qps.ru"),
            "14": ("Short.cm"),
            "15": ("Tiny.cc"),
            "16": ("TinyURL.com"),
            "17": ("Git.io"),
            "18": ("Tiny.cc"),
           }
    for key in sorted(menu.keys()):
         print(key+": " + menu[key])

    ans = input("Make A Choice.. ")
    menu.get(ans,[None,invalid])[1]()