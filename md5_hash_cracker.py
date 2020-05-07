# md5 hash cracker
import hashlib
from colorama import Fore, Style
try:
    print(Fore.GREEN + """         
             __  __           __       ______                __            
            / / / /___ ______/ /_     / ____/________ ______/ /_____  _____
           / /_/ / __ `/ ___/ __ \   / /   / ___/ __ `/ ___/ //_/ _ \/ ___/
          / __  / /_/ (__  ) / / /  / /___/ /  / /_/ / /__/ ,< /  __/ /    
         /_/ /_/\__,_/____/_/ /_/   \____/_/   \__,_/\___/_/|_|\___/_/     
                                                                           
             MD5 Hash Cracker 			[Author : HackersBrain]""" + Style.RESET_ALL)

except Exception as err:
    pass
print()
try:
    hash = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter the Hash : " + Fore.GREEN)
    w_list = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Input Full Path of Wordlist : " + Fore.GREEN)
    print(Style.RESET_ALL)
    pass_file = open(w_list, "r")

    for i in pass_file:
        file_enc = i.encode('utf-8')
        md_hash = hashlib.md5(file_enc.strip()).hexdigest()

        if md_hash == hash:
            print(Fore.GREEN + " Password Found :", i + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + " Password Not Found !!!" + Style.RESET_ALL)
except Exception as error:
    print(Style.RESET_ALL)
    print(error, "\n\t File not Found ...\t Exiting Program...\n")
