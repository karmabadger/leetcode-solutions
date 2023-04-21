

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      carry = 1
      for i,e in reversed(list(enumerate(digits))):
        tmp = e + carry
        if tmp < 10:
          digits[i] = tmp
          return digits
        else:
          digits[i] = tmp % 10
          carry = tmp // 10
      
      digits.insert(0, carry)
      return digits
    
    