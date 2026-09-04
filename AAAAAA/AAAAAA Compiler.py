import os
import platform
COMPILED = ""
with open("code.AAAAAA", mode="r") as f:
    CODE = f.read().splitlines()
for i in range(len(CODE)):
    CODE[i] = CODE[i].split()
    for ii in range(len(CODE[i])):
        if CODE[i][ii] == "aAaaAa":
            COMPILED += 'print("'
        elif CODE[i][ii] == "aAAAAA":
            COMPILED += "a"
        elif CODE[i][ii] == "AaAAAA":
            COMPILED += "b"
        elif CODE[i][ii] == "AAaAAA":
            COMPILED += "c"
        elif CODE[i][ii] == "AAAaAA":
            COMPILED += "d"
        elif CODE[i][ii] == "AAAAaA":
            COMPILED += "e"
        elif CODE[i][ii] == "AAAAAa":
            COMPILED += "f"
        elif CODE[i][ii] == "aaAAAA":
            COMPILED += "g"
        elif CODE[i][ii] == "aAaAAA":
            COMPILED += "h"
        elif CODE[i][ii] == "aAAaAA":
            COMPILED += "i"
        elif CODE[i][ii] == "aAAAaA":
            COMPILED += "j"
        elif CODE[i][ii] == "aAAAAa":
            COMPILED += "k"
        elif CODE[i][ii] == "aaaAAA":
            COMPILED += "l"
        elif CODE[i][ii] == "aaAaAA":
            COMPILED += "m"
        elif CODE[i][ii] == "aaAAaA":
            COMPILED += "n"
        elif CODE[i][ii] == "aaAAAa":
            COMPILED += "o"
        elif CODE[i][ii] == "aaaaAA":
            COMPILED += "p"
        elif CODE[i][ii] == "aaaAaA":
            COMPILED += "q"
        elif CODE[i][ii] == "aaaAAa":
            COMPILED += "r"
        elif CODE[i][ii] == "AaAAaA":
            COMPILED += "s"
        elif CODE[i][ii] == "AAaAAa":
            COMPILED += "t"
        elif CODE[i][ii] == "AAAaAa":
            COMPILED += "u"
        elif CODE[i][ii] == "AAAaaA":
            COMPILED += "v"
        elif CODE[i][ii] == "AAAaaa":
            COMPILED += "w"
        elif CODE[i][ii] == "AaaAAA":
            COMPILED += "x"
        elif CODE[i][ii] == "AaAaAA":
            COMPILED += "y"
        elif CODE[i][ii] == "AAaAaA":
            COMPILED += "z"
        elif CODE[i][ii] == "aaaaaa":
            COMPILED += " "
        elif CODE[i][ii] == "AAAAAA":
            COMPILED += "input()\n"
        elif CODE[i][ii] == "aaAAaa":
            COMPILED += '")\n'
with open("Compiled-AAAAAA-TEMP.py", mode="w") as f:
    f.write("import os\n" + COMPILED + """\nos.remove("Compiled-AAAAAA-TEMP.py")""")
if platform.system() == "Windows":
    os.system("start Compiled-AAAAAA-TEMP.py")
else:
    os.system("python3 Compiled-AAAAAA-TEMP.py")

