from mac import Mac_Changer

if __name__ == "__main__":
    mc =Mac_Changer()
    curr = mc.get_mac("eth0")
    New = input("Enter New Mac Address :: ")
    change = mc.change_mac("eth0",New)
    