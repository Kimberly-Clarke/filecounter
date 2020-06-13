#Just a simple program to check the number of specific extension files in a dir.
import os
import time
while True:
   count = 0
   print(">>> File counter..")
   print(">>> Press anything else to exit.")
   enter_file = input(">>>Enter the extension of file you want to search(with .): ")
   if enter_file.startswith('.'):
      for (dirs, dirname, files) in os.walk('.'):
         for filename in files:
            if filename.endswith(enter_file):
               count = count + 1
      p = ("Found {} files with extension {}".format(count,enter_file))
      print(p,"\n\n")
      continue
   elif enter_file == "q" or enter_file == "Q":
      print("exiting.",end="")
      time.sleep(1)
      print(".")
      break
   else:
      print("Invalid choice!\n")
      continue
