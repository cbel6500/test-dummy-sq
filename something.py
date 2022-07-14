from random import randint

def special_function(is_special):
   if is_special:
      return "this function is special"
   else:
      return "this function is not special"

def guess_age():
   yes  = true 
   if yes:
      return randint(0, 100)
   return randint(0, 50)
