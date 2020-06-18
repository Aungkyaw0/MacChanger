import subprocess
import re
class Mac_Changer:
    def __init__(self):
        self.mac_add = ""
    
    def get_mac(self,iface):
        out = subprocess.run(["ifconfig",iface] , shell=False , capture_output=True)
        
        cmd_output = out.stdout.decode("utf-8")
        

        patter = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'

        regex = re.compile(patter)

        ans = regex.search(cmd_output)

        currt_mac = ans.group().split(" ")[1]
        
        self.mac_add = currt_mac

        return currt_mac
    
    def change_mac(self,iface,new):
        print("[+] Current MAC Address is :: ",self.get_mac(iface))
        outt = subprocess.run(["ifconfig",iface,"down"],shell=False , capture_output=True)
        outt.stdout.decode("utf-8")
        
        
        outt0 = subprocess.run(["ifconfig",iface,"hw","ether",new],shell=False , capture_output=True)
        outt0.stdout.decode("utf-8")
        

        outt1 = subprocess.run(["ifconfig",iface,"up"],shell=False , capture_output=True)
        outt1.stdout.decode("utf-8")
        
        print("[+] Updating Mac Address is :: ",self.get_mac(iface))
        return self.get_mac(iface)



