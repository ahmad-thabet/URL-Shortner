import pyshorteners

def invalid():
   print ("INVALID CHOICE!")

def bitly():
    key = input("Enter API key .. ")
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener(api_key='YOUR_KEY')
    result = s.bitly.short(domain)
    print(result)


def tinyurl():
    s = pyshorteners.Shortener()
    site = input("Enter Site .. ")
    result = s.tinyurl.short(site)
    print(result)

def adfly():
    key = input("Enter API Key .. ")
    user_id = input("Enter User ID .. ")
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener(api_key=key, user_id=user_id,
                               , type='int')
    result = s.adfly.short(site)
    print(result)

def chilpit():
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener()
    result = s.chilpit.short(domain)
    print(result)

def clckru():
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener()
    result = s.clckru.short(domain)
    print(result)

def cuttly():
    key = input("Enter API Key .. ")
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener(api_key='YOUR_KEY')
    result = s.cuttly.short('http://www.google.com')
    print(result)



if __name__ == '__main__':
    menu = {"1":("adf.ly",adfly),
            "2":("Bit.ly",bitly),
            "3": ("Chilp.it",chilpit),
            "4": ("Clck.ru",clckru),
            "5": ("Cutt.ly",cuttly),
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
            "16": ("TinyURL.com",tinyurl),
            "17": ("Git.io"),
            "18": ("Tiny.cc"),
           }

    for key in sorted(menu.keys()):
         print(key+": " + menu[key][0])

    ans = input("Make A Choice.. ")
    menu.get(ans,[None,invalid])[1]()