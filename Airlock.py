class Airlock:
    def __init__(self,code,sealed=False):
        self.code=code
        self.__sealed= sealed
    def is_sealed(self):
        return self.__sealed
    def __lock_bolts(self):
        print("Bolts locked.")
    def __unlock_bolts(self):
        print("Bolts unlocked.")
    def seal(self):
        if self.__sealed == True:
            print("Already Sealed.")
        else:
            self.__lock_bolts()
            self.__sealed=True
            print("Airlock sealed.")
    def unseal(self):
        if self.__sealed == False:
            print("Already open.")
        else:
            self.__lock_bolts()
            self.__sealed=False
            print("Airlock open.")
    def status(self):
        if self.__sealed == True:
            return "sealed"
        else:
            return "open"
    def __str__(self):
        return "Airlock "+ self.code + ":  "+self.status()
    
a = Airlock ("H1")
print(a)
a.seal()
print(a.is_sealed())
a . seal ()
a . unseal ()
print (a)
a . unseal ()
        
            