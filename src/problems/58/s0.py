class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      splitted = s.split(" ")
      last_idx = len(splitted) - 1
      while len(splitted[last_idx]) == 0:
        last_idx -= 1
      return len(splitted[len(splitted) - 1])
    
def main():
  solution = Solution()
  
  print(solution.lengthOfLastWord("Hello World"))
  print(solution.lengthOfLastWord("   fly me   to   the moon  "))
  print(solution.lengthOfLastWord("luffy is still joyboy"))
  