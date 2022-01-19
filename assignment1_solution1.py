# -*- coding: utf-8 -*-
"""
Write a Python function that will work on three strings. The function will return to the user a concatenation of 
the string values in reverse order. The function is to be called from the main program.
In the main program, prompt the user for the three strings and pass these values to the function.

"""

def concatenation_func(str1, str2, str3):
  main_str = str3+str2+str1
  return main_str

def main():
  str1 = input("Please enter string 1: ")
  str2 = input("Please enter string 2: ")
  str3 = input("Please enter string 3: ")
  main_str = concatenation_func(str1, str2, str3)
  print("Output: ", main_str)
  
if __name__ == "__main__":
  main()