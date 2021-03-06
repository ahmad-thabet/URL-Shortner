import pyshorteners

def invalid():
   print ("INVALID CHOICE!")

def bitly():
    key = input("Enter API key .. ")
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener(api_key='YOUR_KEY')
    result = s.bitly.short(domain)
    print(result)


def adfly():
    key = input("Enter API Key .. ")
    user_id = input("Enter User ID .. ")
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener(api_key=key, user_id=user_id, type='int')
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

def dagd():
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener()
    result = s.dagd.short(domain)
    print(result)

def gitio():
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener()
    result = s.gitio.short(domain)
    print(result)

def isgd():
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener()
    result = s.isgd.short(domain)
    print(result)

def nullpointer():
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener(domain='https://0x0.st')
    result = s.nullpointer.short(domain)
    print(result)

def osdb():
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener()
    result = s.osdb.short(domain)
    print(result)

def owly():
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener()
    result = s.owly.short(domain)
    print(result)

def post():
    key = input("Enter API Key .. ")
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener(api_key=key)
    result = s.post.short(domain)
    print(result)


def qpsru():
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener()
    result = s.qpsru.short(domain)
    print(result)

def shortcm():
    key = input("Enter API Key .. ")
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener(api_key=key)
    result = s.shortcm.short(domain)
    print(result)

def tinycc():
    key = input("Enter API Key .. ")
    user = input("Enter username .. ")
    domain = input("Enter Site .. ")
    s = pyshorteners.Shortener(api_key=key, login=user)
    result = s.tinycc.short(domain)
    print(result)

def tinyurl():
    site = input("Enter Site .. ")
    s = pyshorteners.Shortener()
    result = s.tinyurl.short(site)
    print(result)



if __name__ == '__main__':
    menu = {"1":("adf.ly",adfly),
            "2":("Bit.ly",bitly),
            "3": ("Chilp.it",chilpit),
            "4": ("Clck.ru",clckru),
            "5": ("Cutt.ly",cuttly),
            "6": ("Da.gd",dagd),
            "7": ("Git.io", gitio),
            "8": ("Is.gd", isgd),
            "9": ("NullPointer", nullpointer),
            "10": ("Os.db", osdb),
            "11": ("Ow.ly", owly),
            "12": ("Po.st",post),
            "13": ("Qps.ru",qpsru),
            "14": ("Short.cm", shortcm),
            "15": ("Tiny.cc", tinycc),
            "16": ("TinyURL.com",tinyurl)
            }

    for key in sorted(menu.keys()):
         print(key+": " + menu[key][0])

    ans = input("Make A Choice.. ")
    menu.get(ans,[None,invalid])[1]()