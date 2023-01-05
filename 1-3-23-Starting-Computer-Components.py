print("""Starting Computer Components




- MENU -


`````````


Please choose one of the options below, and press enter.


1) IPO


2) Power Supply


3) Motherboard


4) Central Processing Unit (CPU)


5) Random-Access Memory (RAM)


6) Hard Disk Drive / Solid State Drive


7) Heatsink


8) Computer Fan


9) Thermal Paste


10) Computer Case


11) Video Card


12) I/O Shield


""")







answer = "empty"







while (answer == "empty"):


 userchoice = input()


 answer = "chosen"






 if(userchoice == "1"):


   print("IPO is a basic acronym representing the basics of an information system. It stands for Input, Process, Output. It is an abstract way to describe the structure of a system. The entity receives some input, processes it, and produces some output. This model can represent a total system - like a phone - or a single aspect of the system like a button on an app. A practical aspect of this model is that if you standardise the inputs and outputs, then how exactly the data is processed is unimportant.")


 elif(userchoice == "2"):


   print("True to its name, the power supply powers all other components of the machine. It usually plugs into the motherboard to power the other parts. The power supply connects to either an internal battery (on a laptop) or a plug for an outlet (on a desktop).")


 elif(userchoice == "3"):


   print("The motherboard is an important computer component because it's what everything else connects to! The motherboard is a decently sized circuit board that lets other components communicate. A motherboard has ports that face outside a PC's case, so you can charge your computer, plug in a monitor, or connect a mouse.")


 elif(userchoice == "4"):


   print("A CPU, sometimes referred to as a computer's brain, is the workhorse of the machine. It performs the calculations needed by a system, and can vary in speed. The work that a CPU does generates heat, which is why your computer has a fan inside. A more powerful CPU is necessary for intense computer work like editing high-definition video or programming complex software.")


 elif(userchoice == "5"):


   print("RAM is temporary memory. Whenever you open up a Microsoft Word window, your computer places it in RAM, and when you close the window, that RAM is freed. Since RAM is volatile, its contents are lost if the machine loses power. This is why you lose a Word document when the power goes out if you didn't save it.")


 elif(userchoice == "6"):


   print("Since RAM is temporary, your computer needs a place to store data permanently. That's where the hard drive comes in. The traditional hard drive consists of several spinning platters with an arm that physically writes data to the disk. However, these drives are slow and are starting to be replaced by the faster solid-state drives.")


 elif(userchoice == "7"):


   print("A passive heat exchanger that transfers the heat generated by an electronic or a mechanical device to a fluid medium, often air or a liquid coolant, where it is dissipated away from the device, thereby allowing regulation of the device's temperature.")


 elif(userchoice == "8"):


   print("A computer fan is any fan inside, or attached to, a computer case used for active cooling. Fans are used to draw cooler air into the case from the outside, expel warm air from inside and move air across a heat sink to cool a particular component.")


 elif(userchoice == "9"):


   print("Thermal paste (aka thermal compound, thermal interface material (TIM), and other names) is a thermally conductive (but usually electricaly insulating) chemical compound, which is commonly used as an interface between heat sinks and heat sources such as high-power semiconductor devices. The main role of thermal paste is to eliminate air gaps or spaces (which act as thermal insulation) from the interface area in order to maximize heat transfer and dissipation. Thermal paste is an example of a thermal interface material. As opposed to thermal adhesive, thermal paste does not add mechanical strength to the bond between heat source and heat sink. It has to be coupled with a mechanical fixation mechanism such as screws to hold the heat sink in place and to apply pressure, spreading and thinning the thermal paste.")


 elif(userchoice == "10"):


   print("A computer case, aka computer chassis, tower, system unit, or cabinet, is the enclosure that contains most of the components of a personal computer (usually excluding the display, keyboard, and mouse). It both provides structure for the components, as well as provides some level of physical protection.")


 elif(userchoice == "11"):


   print("A video card is a dedicated unit for handling the output of images to a display. Video cards have their own dedicated RAM for performing these functions. A high-end video card is required to process extremely intense visual functions, such as computer drafting by engineers. Like many components, many types of video cards are available with varying power and prices.")


 elif(userchoice == "12"):


   print("Aka RFI/EMI cover plate, keeps electro-magnetic radiation inside of the case. Aids in keeping dust out of the case, aids in controlling air flow.")


 else:


   print("That's not one of the options, silly!")


   answer = "empty"
