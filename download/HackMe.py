# By wanets: https://i.ibb.co/5YkGHx7/image.png
#██╗░░██╗░█████╗░░█████╗░██╗░░██╗  ███╗░░░███╗███████╗██╗
#██║░░██║██╔══██╗██╔══██╗██║░██╔╝  ████╗░████║██╔════╝╚═╝
#███████║███████║██║░░╚═╝█████═╝░  ██╔████╔██║█████╗░░░░░
#██╔══██║██╔══██║██║░░██╗██╔═██╗░  ██║╚██╔╝██║██╔══╝░░░░░
#██║░░██║██║░░██║╚█████╔╝██║░╚██╗  ██║░╚═╝░██║███████╗██╗
#╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚══════╝╚═╝
# HackMe is made for fun. Don't use it for real hacking




#Cͨoͦdͩeͤ:
# The hack is simple: Edit, Delete and Create...and Read
def readmode(fil):
    f = open(fil, "r")
    print("The file content now is:",f.read())
def editmode(fil):
    f = open(fil, "w")
    text = input("Change file content to:")
    f.write(text)
    f.close()
def makemode(fil):
    f = open(fil, "x")
def delmode(fil):
    os.remove(fil)
# My idea is to make a working console:
def console():
    console = str(input("[E]dit file, [Del]ete file, [C]reate a file or [R]ead file...More commands COMING SOON"))
    fil = str((input("Type the file name(like 'ReadMe.txt')")))
    if console == "E":
        editmode(fil)
    elif console == "Del":
        delmode(fil)
    elif console == "C":
        makemode(fil)
    elif console == "R":
        readmode(fil)
    else:
        print("No console command provided. Please rerun")
console()


