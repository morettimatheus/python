class CashRegister :
    #init is our mandatory constructor. We are setting itemCount and totalPrice to 0
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0

   #we are defining a method for adding itens (and changing the total)
   def addItem(self, price) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price

   #just returns us the total price
   def getTotal(self) :
      return self._totalPrice

   #returns us the count of itens
   def getCount(self) :
      return self._itemCount

   #clears our variables
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0

   def getPounds(self):
       return int(self._totalPrice)

   def giveChange(self, payment):
       if payment >= self._totalPrice:
           return payment - self._totalPrice
       else:
           return 0
