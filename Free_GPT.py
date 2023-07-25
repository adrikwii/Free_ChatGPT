import g4f
import colorama
import os
from sys import platform

isStart = True


def Chat_GPT(demande):
    response = g4f.ChatCompletion.create(model=g4f.Model.gpt_4,provider=g4f.Provider.DeepAi, messages=[{"role": "user", "content": demande}])
    print(colorama.Fore.GREEN + "Chat_GPT :")
    print(colorama.Fore.GREEN + response)

########################## MAIN ###########################

while isStart == True:
    correctResponse = False
    print(colorama.Fore.RED + 
"""#############################################
 ____  ____  ____  ____        ___  ____  ____ 
(  __)(  _ \(  __)(  __)      / __)(  _ \(_  _)
 ) _)  )   / ) _)  ) _)  ____( (_ \ ) __/  )(  
(__)  (__\_)(____)(____)(____)\___/(__)   (__) 

#################################################
Create By : adrikiwii""")
    print(colorama.Fore.CYAN +"You :")
    question = input()  
    Chat_GPT(question)
    while correctResponse == False:
        print(colorama.Fore.MAGENTA+"Continu ? Y/N")
        Continu = input()
        if Continu == "Y" or Continu == "y":
            if platform == "linux" or platform == "linux2" or platform == "darwin":
                os.system('clear')
                correctResponse = True
            elif platform == "win32":
                os.system('cls')
                correctResponse = True
        elif Continu == "N" or Continu == "n":
            isStart = False
            correctResponse = True




