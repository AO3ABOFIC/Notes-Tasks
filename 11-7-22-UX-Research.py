print("""Todays date is 11/7/2022, and these are notes on Prototypes and UX Research
Prototypes are used for a variety of reasons.
Here are the most common ways they are used across the industry.
-- MENU --
''''''''''
Please choose on of the options below, and press enter.
1) Wireframe
2) Mockup
3) Prototype
""")

answer = "empty"

while (answer == "empty"):
 userchoice = input()
 if(userchoice == "1"):
 print(""" Wireframes are a planning diagram to communicate the overall layout.
""")

 elif(userchoice == "2"):
  print(""" Mockups are a planning illustration to communicate the final appearance. """)
 print("")
 print(""" """)

 elif(userchoice == "3"):
  print(""" Prototypes are:
  1. a planning tool to communicate the functionality
  2. finished version used for quality assurance before mass-production. 
""")


 else: 
  print("INVALID INPUT, please try again")
  answer = "empty"
  userchoice = input()
