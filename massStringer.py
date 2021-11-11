import os
import subprocess
import re
path = str(input("Enter directory path: "))
for file in os.listdir(path):
        print(file, ":")
        filepath = path + str(file)
        bashcmd = ["strings", filepath]
        process = subprocess.Popen(bashcmd, stdout=subprocess.PIPE)
        output, error = process.communicate()
        flag = re.search("ABCTF{(.*)}",output.decode())

        print(flag)
