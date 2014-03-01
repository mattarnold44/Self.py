#!/usr/bin/python

class Self (object):
    # consider existential concepts of the self. has this been done before?

    def __init__(self, was=None, am=None, want2be=None): # add parameters
        self.was = was
        self.am = am
        self.want2be = want2be  
        self.zen = Trait('no-mind')  # create private zen object
        self.Kierk = Trait('Soren Kierkegaard (Knight of Faith)') # create private Kierkegaard object
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
        print '\n\n\t you became S0ren Kierkegaard\n'
         
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
# other functions:

def printOptions():
    print '\nOPTIONS:'
    print '\t1. i am...'
    print '\t2. become [x]'
    print '\t[q] to quit'

def getInput(prompt):
    o = raw_input(prompt)
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
#             MAIN                                #
###################################################

if __name__ == "__main__":
    print '\nnew game\n\n'    
    quit = False
    while quit != True:
        beAnsw = getInput('do you want to be? [y/n/quit]\n')

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
                choice = getInput('choose\n')
        
                if choice == '1':
                    i.printMe()
                
                elif choice == '2': 
                    
                    while True:
                        want = getInput('what do you want to become?\n\t1. what i am\n\t2. something else...\n')
                        if want == '1':
                            if i.getHemi() == 'east':
                                i.goZen()
                            else:
                                i.goKierk()
                            break
                        elif want == '2':
                            want2be = getInput('choose anything\n')
                            print '\ninteresting choice'
                             
                            while True:
                                response = getInput('how bad do you want it?\n\t1. bad\n\t2. real bad\n\t3. i don\'t\n')
                                if response == '1' or response == '2':
                                    i.plantDesire(want2be)
                                    break
                                elif response == '3':
                                    i.actualize(want2be)
                                    break
                                else:
                                    print '\ninvalid choice\n'
                            break    
                        else:
                            print '\ninvalid choice\n'

                elif choice == 'q':
                    quit = True
                else:
                    print '\ninvalid choice'
        
        elif beAnsw == 'quit':
            quit = True 
