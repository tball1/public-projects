knowngrabbers = [
    "lovebird.guru",
    "trulove.guru",
    "dateing.club",
    "otherhalf.life",
    "shrekis.life",
    "datasig.io",
    "datauth.io",
    "headshot.monster",
    "gaming-at-my.best",
    "progaming.monster",
    "yourmy.monster",
    "screenshare.host",
    "imageshare.best",
    "screenshot.best",
    "gamingfun.me",
    "catsnthing.com",
    "mypic.icu",
    "catsnthings.com",
    "curiouscat.club",
    "joinmy.site",
    "fortnitechat.site",
    "fortnight.space",
    "freegiftcards.co",
    "stopify.co",
    "grabify.link",
    "iplogger.org",
    "2no.co",
    "iplogger.ru",
    "iplogger.com"
    "iplogger.info"
    "ipgrabber.ru",
    "ipgraber.ru",
    "iplis.ru",
    "02ip.ru",
    "ezstat.ru"




] #Add more if you like but theese are all the ones I know of

site = input("site:")
logger = False
for grabber in knowngrabbers:
    if site.find(grabber) != -1:
        print("IP LOGGER")
        logger = True
        break
if not logger:
    print("This link seems safe")

