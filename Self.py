#!/usr/bin/python2 

class Self (object):
    # consider existential concepts of the self. has this been done before?

    def __init__(self, was=None, am=None, want2be=None): # add parameters
        self.was = was
        self.am = am
        self.want2be = want2be  
        self.zen = Trait('no-mind')  # create private zen object
        self.Kierk = Trait('Soren Kierkegaard (Knight of Faith)') # create private Kierkegaard object
        self.hemi = None
        self.despair = False
        self.immortal = False
        self.tab = 0
    
    def incTab(self):
        self.tab += 1
    
    def decTab(self):
        self.tab -= 1

    def getTab(self):
        return int(str(self.tab))

    def checkImmortality(self):
        if self.immortal == True:
            return True
        else:
            return False
    
    def startDespairing(self):
        self.despair = True

    def getDespair(self):
        if self.despair == True:
            return True
        else:
            return False

    def isEast(self):
        self.hemi = 'east'

    def isWest(self):
        self.hemi = 'west'

    def getHemi(self):
        if self.hemi == 'east':
            return 'east'
        else:
            return 'west'
    
    def actualize(self, want2be):
        # equivalent to setAm
        if self.was is None:
            self.was = []
        self.was.append(str(self.am))
        self.am = want2be
        self.want2be = None
        print 
        print "\t"*self.tab + "*****************"
        print "\t"*self.tab + "   ~actualized~  "
        print "\t"*self.tab + "*****************"
 
    def plantDesire(self, want2be):
        self.want2be = want2be
        if self.am == self.zen:
            # this if/else is currently unnecessary because goZen() sets self.was to None
            if self.was is None:
                self.was = []
                self.was.append(str(self.am))
                self.am = Trait('no longer zen')
            else:
                temp = self.am
                self.am = self.was.pop()
                self.was.append(temp)            
    
    def goZen(self):
        self.was = None
        self.am = self.zen
        self.want2be = None    
        print '\n\n' + '\t'*self.tab + '                           zen\n'
    
    def goKierk(self):
        if self.was is None:
            self.was = []
        self.was.append(self.am)
        self.am = self.Kierk
        self.want2be = None
        # implies immortality
        self.immortal = True
        # implies despair
        self.despair = True
        print '\n\n\t' + '\t'*self.tab + ' you became S0ren Kierkegaard\n'
         
    def getWas(self):
        return str(self.was)

    def getAm(self):
        return str(self.am)

    def getWant2Be(self):
        return str(self.want2be)

    def printMe(self):
        ret = '\n\t' + '\t'*self.tab + '%-9s%s' % ('was: ', self.getWas())
        ret += '\n\t' + '\t'*self.tab + '%-9s%s' % ('am: ', self.getAm())
        ret += '\n\t' +  '\t'*self.tab + '%-9s%s' % ('want2be: ', self.getWant2Be())
        print ret


class Trait (object):

    def __init__(self, adj):
        self.adj = adj

    def __str__(self):
        return str(self.adj)

    def setAdj(self, newAdj):
        self.adj = newAdj

# ===========================================================
# other functions:

def printTabbedOptions(tabs, optionsList):
    for option in optionsList:
        print '\t' + tabs + option

def getInput(tab1, prompt, tab2):  
    # must give 3 parameters
    fullPrompt = tab1 + prompt + tab2
    o = raw_input(fullPrompt)
    return o

def setEastWest():
    EastWest = False
    while EastWest == False:
        EastWest = getInput('','\n\t...of the [east], or of the [west]?\n\t','').lower()
        if EastWest == 'east':
            i.isEast() 
        elif EastWest == 'west':
            i.isWest()
        else:                
            print '\n\tinvalid choice'
            EastWest = False

def updateTab(t):
    t = '\t'*i.getTab()
    return t

###################################################
#             MAIN                                #
###################################################

if __name__ == "__main__":
    print '\nnew game\n\n'    
    quit = False
    while quit != True:
        beAnsw = getInput('','do you want to be? [y/n/quit]\n','')

        if beAnsw == "n":
            # never existed
            print '\nunborn\n'

        elif beAnsw == "y":
            # choosing to exist
            i = Self()
            tabs = '\t'*i.getTab()
            print '\nyou exist, as an object'
            
            setEastWest()

            quit = False
            while quit != True:
                # the print options loop
                print '\n' + tabs+ 'OPTIONS:'
                printTabbedOptions(tabs, ['1. i am...', '2. become [x]', '3. check despair status', '4. shift right', '5. shift left', '[q] to quit'])
                choice = getInput(tabs,'choose\n', tabs)
        
                if choice == '1':
                    # i am...
                    i.printMe()
                
                elif choice == '2': 
                    # become [x]
                    while True:
                        print '\n' + tabs + 'what do you want to become'
                        printTabbedOptions(tabs, ['1. what i am', '2. something else...'])
                        want = getInput(tabs,'choose\n', tabs)
                        if want == '1':
                            if i.getHemi() == 'east':
                                i.goZen()
                            else:
                                i.goKierk()
                            break
                        elif want == '2':
                            want2be = getInput(tabs,'choose anything\n',tabs)
                            print '\n' + tabs + 'interesting choice\n'
                             
                            while True:
                                print  tabs + 'how bad do you want it?\n\t' + tabs + '1. bad\n\t' + tabs + '2. real bad\n\t' + tabs + '3. i don\'t'
                                response = getInput(tabs,'choose\n', tabs)
                                if response == '1' or response == '2':
                                    i.plantDesire(want2be)
                                    break
                                elif response == '3':
                                    i.actualize(want2be)
                                    break
                                else:
                                    print '\n',tabs,'invalid choice\n'
                            break    
                        else:
                            print '\n',tabs,'invalid choice\n'
                
                elif choice == '3':
                    # check despair status
                    if i.getDespair() == True:
                        print '\n',tabs,'you are in despair'
                    else:
                        print '\n',tabs,'you are not in despair'
                
                elif choice == '4':
                    # shift right
                    i.incTab()
                    tabs = updateTab(tabs)

                elif choice == '5':
                    # shift left
                    i.decTab()
                    tabs = updateTab(tabs)

                elif choice == 'q':
                    if i.checkImmortality() == True:
                        print '\n',tabs,'the self is eternal; you can\'t quit now'
                    else:
                        quit = True
                else:
                    print '\n',tabs,'invalid choice'
        
        elif beAnsw == 'quit':
            quit = True 

#TODO : synopsis, suicide, (tabbing)
