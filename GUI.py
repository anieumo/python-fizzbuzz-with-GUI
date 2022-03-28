

def onButtonClicked1():
    x = 0
    while x < 30:
        x += 1
        if x % 4 == 0 and x % 5 == 0:
            print ("fizzbuzz")
        elif x % 5 == 0:
            print ("buzz")
            continue
        elif x % 4 == 0:
            print ("fizz")
            continue
        else:
            print (x)

    fizzbuzz(name=name)
    
def onButtonClicked2():
     x = 0
     while x < 30:
         x += 1
         if x % 4 == 0 and x % 5 == 0:
             print x

def onButtonClicked3():
    x = 0
    while x < 30:
        x += 1
        if x % 4 == 0:
            print x
             
def onButtonClicked4():
    x = 0
    while x < 30:
        x += 1
        if x % 5 == 0:
            print x

def launchFizzbuzzUI():
   
    window = cmds.window(title="fizzbuzz")
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(label="all numbers", command="onButtonClicked1()")
    cmds.button(label="fizzbuzz", command="onButtonClicked2()")
    cmds.button(label="fizz", command="onButtonClicked3()")
    cmds.button(label="buzz", command="onButtonClicked4()")

  
    cmds.showWindow(window)


launchFizzbuzzUI()