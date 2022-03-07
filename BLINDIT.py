#!/usr/bin/env python
# coding: utf-8

# # BlindIT!
# BlindIT is a python code to automatically blind folder names.
# It changes folder names to numbers from 0 to n-1 where n is the number of folders in the directory of your choosing. The program saves a txt file (KEYS) containing the keys with the original names associated to the numbers to revert the names once you are done analyzing your data.

# In[42]:


#importing the appropriate modules
import os
import random
#change working directory
def blindIT():
    files = os.listdir(r"{}".format(user_cwd))
    print(f"The folder names in the current directory were:{files}\n")
    #create an unordered list of numbers corrisponding to the new identity
    keys=[x for x in range(len(files))]
    random.shuffle(keys)
    #print(keys)
    #changing folder name
    for old,new in zip(files,keys):
        os.rename(old,str(new))
    #creating and saving a text file containing the dictionary with keys associated with folder names
    dictionary = {}
    for i in range(len(files)):
        dictionary[keys[i]]=files[i]
    strdic=str(dictionary)
    print("and now they are: " + strdic)
    f=open("KEYS.txt","a+")
    f.write(strdic)
    f.close()  
    
#main loop
#please enter the directory you want to blind
try:
    user_cwd = input("Please insert directory you want to blind: (ex. C:\\test)\nor quit the program by typing quit \n")
    if user_cwd == "quit":
        print("Thank you for using blindIT!\n")
    else:    
        os.chdir(r"{}".format(user_cwd)) 
        active = True
        while active:
            user = input("WARNING: are you sure you want to blind the folders in that directory? (y/n) \nThe process is IRREVERSIBLE, make sure you have a copy if anything were to go wrong\n").lower()
            if user == "y":
                blindIT()
                active=False
                print("Your folders are blinded! \nThank you for using blindIT!\n")
            elif user == "n":
                active = False
                print("No folders were blinded. \nThank you for using blindIT!\n")
            else:
                print ("Enter either the y or n \n")
except FileNotFoundError:
    print("You did not insert a valid directory\nYou have to copy and paste the directory from the address bar! \n")


# In[ ]:




