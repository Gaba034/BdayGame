from datetime import date

class OWUpdate():
  m = "y/dbzymzsizy/d~tz,st/rgn~c"
  glo = "enojytrihtjotjorezjsijegnarjrebmunjeht"
  m2 = ""
  k = ""
  def __init__(self,k):
    self.k = k
  
  def dica(self):
   OW = str(date.today())
   b = OW.split("-")[2]
   if b == self.k:
     return "Day = "+self.k
   else:
    self.glo = self.glo[::-1].replace('j',' ')
    a = input("Quer uma dica? Respostas = S e N :  ")
    if a == "S":
      return('\n'+self.glo)
    else:
      return "Good Luck"
   
  def banga_jhagna(self):
    OW = str(date.today())
    b = OW.split("-")[2]
    self.m2 = self.m.replace('z',' ').replace('~','o').replace('/','a')
    z = len(self.m) - 2
    x = self.m2[25].upper()
    if b == self.k:
      return(x+self.m2[z::-1])
    else:
      return("Nope")


    
you = OWUpdate(input("2 dígitos ex: 00 ; 54 ; 67 ; =  "))
print(you.banga_jhagna())
print(you.dica())

# Yes, the code was made to look messy and crapy