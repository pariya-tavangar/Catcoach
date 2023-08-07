# Useroption = int(input('Enter your choice: '))
        
# #Check what choice was entered and act accordingly
# if Useroption == 1:
#     AsciiArts.cat1()
# elif Useroption == 2:
#     option2()
# elif Useroption == 3:
#     option3()
# elif Useroption == 4:
#     print('Thanks message before exiting')
#     exit()
# else:
#     print('Invalid option. Please enter a number between 1 and 4.')


        #   ________________________________________________
        #  |____________________TODO LIST___________________|           
                                                 
        #     1-  {}   []   ~   Deadline: {}   
        #     2- ...   []          
        #     3- ...   []          
        #     4- ...   []            
        #     5- ...   []           
        #     6- ...   []                 
        #     8- ...   []                   
        #     9- ...   []                   
        #     10- ...  []                  
        #  ________________________________________

        #              ____ Page1 ____


# print("""\
#          _________________________________________
#         |________________TODO LIST_______________|           
#         |                                        |
#         |     1- ...   []   ~       ####         |
#         |     2- ...   []   ~       ####         |
#         |     3- ...   []   ~       ####         |
#         |     4- ...   []   ~       ####         |
#         |     5- ...   []   ~       ####         |
#         |     6- ...   []   ~       ####         |
#         |     7- ...   []   ~       ####         |
#         |     8- ...   []   ~       ####         |
#         |     9- ...   []   ~       ####         |
#         |    10- ...   []   ~       ####         |
#         |________________________________________|
                        
#                     ____ Page1 ____       

#            """)

#-------- Variables ----------
# taskName2, taskName3, taskName4, taskName5, taskName6, taskName7, taskname8, taskname9, taskname10 = ""
# taskTime2, taskTime3, taskTime4, taskTime5, taskTime6, taskTime7, taskTime8, taskTime9, taskTime10 = ""

# def Adding():
#     taskName = ( input ("Enter your task name?"))
#     taskTime = ( input ("Enter your deadline ?"))
# def Adding2():
#     taskName2 = ( input ("Enter your task name?"))
#     taskTime2 = ( input ("Enter your deadline ?"))  

# Task_Table= """\
#     ________________________________________________
#    |____________________TODO LIST___________________|           
#         1-  {}   []   ~   Deadline: {}
#         2-  {}   []   ~   Deadline: {}                                                                                                         
#     _________________________________________________

#                     ____ Page1 ____       

#     """.format(taskName2,taskTime2)

# print(Task_Table)

# adding_input = input(("You want to add more tasks? (y/n)"))

# if (adding_input=="y"):
#     Adding2()
# elif (adding_input=="n"):
#     print("menu")
# else:
#     "Unknown text !"


    
 
# task = (input("Give me a number ?"))
# string_in_string=""" bla bla bla {} bla bla """.format(task)
# print(string_in_string)
# page =1
# tasknum =0
# print("Number of tasks: {}".format(tasknum))
# print("Number of pages: {}".format(page))
# task = str(input('Write a task to be added in the list : \n'))
# time = str(input('Write your deadline :\n'))
# checked = bool(input('Is it checked? y/n : '))

# if checked=="y" :
#     checkIcon= "[x]"
# else:
#     checkedIcon="[ ]"    

# print("*___ Task 1 ___*")
# print("The deadline : {}".format(time))
# print("The Checked : {}".format(checkedIcon))

# def Adding4():
#     taskName4 = ( input ("Enter your task name?"))
#     taskTime4 = ( input ("Enter your deadline ?"))
#     Task_Table= """\
#           ________________________________________________
#          |____________________TODO LIST___________________|           
                                                 
#             4-  {}   []   ~   Deadline: {}                    
#          _________________________________________________

#                      ____ Page1 ____       

#             """.format(taskName4,taskTime4)
# def Adding5():
#     taskName5 = ( input ("Enter your task name?"))
#     taskTime5 = ( input ("Enter your deadline ?"))
# def Adding6():
#     taskName6 = ( input ("Enter your task name?"))
#     taskTime6 = ( input ("Enter your deadline ?"))
# def Adding7():
#     taskName7 = ( input ("Enter your task name?"))
#     taskTime7 = ( input ("Enter your deadline ?"))
# def Adding8():
#     taskName8 = ( input ("Enter your task name?"))
#     taskTime8 = ( input ("Enter your deadline ?"))
# def Adding9():
#     taskName9 = ( input ("Enter your task name?"))
#     taskTime9 = ( input ("Enter your deadline ?"))
# def Adding10():

# keyboard.add_hotkey("alt+d", lambda: print("CTRL+ALT+D Pressed!"))
# keyboard.on_release("ctrl+d" , lambda:print("wow"))






#-------------------------  Keyboard ------------------------------
# from pynput import keyboard

# def on_activate():
#     print('Global hotkey activated!')

# def for_canonical(f):
#     return lambda k: f(l.canonical(k))

# hotkey = keyboard.HotKey(
#     keyboard.HotKey.parse('<ctrl>+<alt>+h'),
#     on_activate)
# with keyboard.Listener(
#         on_press=for_canonical(hotkey.press),
#         on_release=for_canonical(hotkey.release)) as l:
#     l.join()
#--------------------------  Keyboard ----------------------------