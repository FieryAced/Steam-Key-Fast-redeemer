import re
import sys
import webbrowser

urlRoot = "https://store.steampowered.com/account/registerkey?key="

fileName = sys.argv[1]
file = open(fileName,"r")
file = file.read()
out = open("RedeemedKeys.txt","a")
search = re.findall("\w{5}-\w{5}-\w{5}",file)
for key in search:
    print(key) ## Debug
    out.write(key+"\n")
    webbrowser.open_new_tab(urlRoot+key)
out.close()
