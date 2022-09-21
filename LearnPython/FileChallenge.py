import os
from os import path


rootDirPath = path.split(os.path.abspath(__file__))[0]

newDirName: str = "result"
newDirPath = path.join(rootDirPath, newDirName)

os.mkdir(newDirPath)

file = open(rootDirPath + "\\result\\result.txt", "w+")
fl = os.listdir(rootDirPath)

global content
totalBytes = 0

for fn in fl:

    fp = rootDirPath + "\\" + fn
    print(fn)
    print(fp)

    if path.isfile(fp):

        totalBytes += path.getsize(fp)
        content = fn + "\n"

        file.write(content)

file.write("Total bytes: {tb}\n".format(tb = totalBytes))
file.seek(0,0)
print(file.read())

file.close()


