print("""4th INDUSTRIAL REVOLUTION

The 4th Industrial Revolution is 


- MENU -
````````
Please choose one of the options below, and press enter.

1) Question & Answer 1
2) Question & Answer 2
3) Question & Answer 3
""")

answer = "empty"

while (answer == "empty"):
  userchoice = input()
  answer = "chosen"

  if(userchoice == "1"):
    print("""I’m required to be here, other than that, I am here to learn the skills required to exist in a reasonably decent life and succeed.

To learn / teach the public specific skills that require specific thought patterns that the government finds befitting of an American citizen (aka beneficial to capitalist society).

I guess, I am getting the knowledge I expected to get even if at times it is less than fulfilling and I wish I never signed up for it in the first place.""")
  elif(userchoice == "2"):
    print("""The technological advancement could make education more advanced or at least run at a faster, more efficient pace; that being said, most modern technology is more focussed on increasing the general quality of life and filling in or assisting with specialty jobs that require extensive training and precision. Education does not seem to be the priority but with further development that could very well change.""")
  elif(userchoice == "3"):
    print("""Love is a strong word and I’m not particularly committed to something entirely yet but there are things that I strongly like such as computer science, art, and writing.
Yes, I have been given many opportunities to develop my skills in each of these areas all of which were relatively enjoyable and effective.
A combination of the two, if it wasn’t at school it may have been school that made me aware of the opportunity or granted me the opportunity, even then, there have been plenty of experiences to further develop the skills related to my passion unrelated to school entirely.
Most likely, I think past that stage in life priorities change and in a weird way you have more time, even if there are plenty of responsibilities to fill that time. It is a more free stage of life to work on your passions after your dedication to schooling and/or training for a stable career.

I do think our school system is flawed but I personally have no solutions to offer, it could be complacency but I choose to believe I just don’t care enough to create the change myself. I’m graduating soon enough and don’t particularly care much about education so should it change? Yes. Will I change it or assist in any way? Probably not.""")
  else:
    print("INVALID INPUT, please try again")
    answer = "empty"
