#!/usr/bin/python

class Self (object):
    # consider existential concepts of the self. has this been done before?

    def __init__(self, was=None, am=None, want2be=None): # add parameters
        self.was = was
        self.am = am
        self.want2be = want2be  # should it be 'other' or 'want2be'?
        self.zen = Trait('no-mind')  # create private zen object
        self.Kierk = Trait('Soren Kierkegaard (Knight of Faith)')
        self.hemi = None

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
        print "\n*****************"
        print "    ~actualized~   "
        print "*****************"

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
        print '\n\n                           zen\n'
    
    def goKierk(self):
        if self.was is None:
            self.was = []
        self.was.append(self.am)
        self.am = self.Kierk
        self.want2be = None
        print '\n\n\t you became Soren Kierkegaard\n'
         
    def getWas(self):
        return str(self.was)

    def getAm(self):
        return str(self.am)

    def getWant2Be(self):
        return str(self.want2be)

    def printMe(self):
        ret = "\n\t%-9s%s" % ("was: ", self.getWas())
        ret += "\n\t%-9s%s" % ("am: ", self.getAm())
        ret += "\n\t%-9s%s" % ("want2be: ", self.getWant2Be())
        print ret
    
    # TODO synopsis()
    # try/except ValueError

class Trait (object):

    def __init__(self, adj):
        self.adj = adj

    def __str__(self):
        return str(self.adj)

    def setAdj(self, newAdj):
        self.adj = newAdj

# ===========================================================

def askBe():
    a = raw_input('do you want to be? [y/n/quit]\n')
    print a
    return a

def printOptions():
    print '\nOPTIONS:'
    print '\t1. i am...'
    print '\t2. become [x]'

def getInput(prompt):
    o = raw_input(prompt)
    print o
    return o

def setEastWest():
    EastWest = False
    while EastWest == False:
        EastWest = getInput('\n\t...of the [east], or of the [west]?\n\t').lower()
        if EastWest == 'east':
            i.isEast() 
        elif EastWest == 'west':
            i.isWest()
        else:                
            print 'invalid choice'
            EastWest = False

###################################################
print '\nnew game\n\n'    
quit = False
while quit != True:
    beAnsw = askBe()

    if beAnsw == "n":
        # never existed
        print '\nunborn\n'

    elif beAnsw == "y":
        # choosing to exist
        i = Self()
        print '\nyou exist, as an object'
        
        setEastWest()

        quit = False
        while quit != True:
            # the print options loop
            printOptions()
            choice = int(getInput('choose\n'))
    
            if choice == 1:
                i.printMe()
            elif choice == 2:
                want = int(getInput('what do you want to become?\n\t1. what i am\n\t2. something else...\n'))
        
                if want == 1:
                    if i.getHemi() == 'east':
                        i.goZen()
                    else:
                        i.goKierk()
                elif want == 2:
                    want2be = getInput('choose anything\n')
                    print '\ninteresting choice'
                    response = int(getInput('how bad do you want it?\n\t1. bad\n\t2. real bad\n\t3. i don\'t\n'))
                    if response == 1 or response == 2:
                        i.plantDesire(want2be)
                    elif response == 3:
                        i.actualize(want2be)
    
    elif beAnsw == 'quit':
        quit = True

    
