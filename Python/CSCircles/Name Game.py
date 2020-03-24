# input (PEARL) = output: pearl, pearl, bo-bearl
#                         banana-fana fo-fearl
#                         fee-fi-mo-mearl
#                         pearl!
while True:

    inp = input("Name? ")

    name = inp                    # PEARL
    block = name[1:len(name)]     # EARL

    print(name + ", " + name + ", " + "bo-b" + block)
    print("banana-fana fo-f" + block)
    print("fee-fi-mo-m" + block)
    print(name + "!")
    print("–––––––––––––––––––")
