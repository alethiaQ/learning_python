# functions are defined by 'def' keyword, they are indent based so all code inside the function has to be indented, otherwise it is considered outside 

def firstfunction():
    print("Since this print statement is indented properly, it is apart of the firstfunction function")
    print("So is this!")
print("I am not apart of the function, sad!")
print("These print statements will be printed first, becaused we have yet to call our fn")

firstfunction()

def prints_name(name):
    print("How's it " + name)

prints_name("BOBBBBY")
