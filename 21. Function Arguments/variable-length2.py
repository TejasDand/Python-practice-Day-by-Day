#Two stars (**) means dict

def name(**name):
    print("Hello,",name["fname"],name["mname"],name["lname"])

name(fname = "Tejas", lname = "Dand", mname = "Girish")