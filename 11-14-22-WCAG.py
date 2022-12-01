print("""WCAG
- MENU -
`````````
Please choose one of the options below, and press enter.
1) What is WCAG?
2) When was WCAG released?
3) Who works on WCAG?
4) What is WCAG 2.1 in comparison to WCAG 2.0?
5) Two guidelines or focuses related to WCAG 2 or 3
6) SaaS accessibility preference
""")

answer = "empty"

while (answer == "empty"):
  userchoice = input()
  answer = "chosen"
  
  if(userchoice == "1"):
    print("""WCAG stands for Web Content Accessibility Guidelines. WCAG is a collection of guidelines for the best possible user accessibility online. It defines how to make web content more accessible to people with disabilities and aging people with changing abilities.""")
  elif(userchoice == "2"):
    print("""WCAG 1 was released May 5th, in 1999.""")
  elif(userchoice == "3"):
    print("""WCAG is developed by the World Wide Web Consortium (W3C).""")
  elif(userchoice == "4"):
    print("""WCAG 2.1 is an extension of WCAG 2.0, not a replacement. WCAG 2.1 added 17 more success criteria to WCAG 2.0, most of which were included to cover significant changes in regards to websites and content producers.""")
  elif(userchoice == "5"):
    print("""I think that WCAG 3's accessibility guidelines of Guidance for more disability groups & Starts from user needs of disability groups instead of technical solutions are not worthy. These accessibility guidelines are extremely important as they move the focus towards making technology even more available for disabled people and accommodating for their needs rather than a technological focus that will persist naturally regardless of focus.""")
  elif(userchoice == "6"):
    print("""My favorite accessibility menu on the different SaaS services is the second one, 'accessiBe.com'. The website has the most options to tailor the website to the user's needs and provides different colors for certain features, which sets it apart from the first one. While the third option also offers different colors, the colors are very bright, which can be distracting or impede a user's ability to navigate the site.""")
  else:
    print("That's not one of the options, silly!")
    answer = "empty"
