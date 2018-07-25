import shutil, os
from Tkinter import Tk
from tkFileDialog import askdirectory

#This utility parses the approved JPG folder and copies the respective
#RAW into the designated folder

#Useful when sorting large numbers of JPGs then copying the RAWs to later polish

filenames = []
suffix = '.RAF'

Tk().withdraw()
#Filepath of the JPG folder (TITLE SRC)
filePathJPG = askdirectory(title='Select the JPG folder')
#Filepath of the RAW folder (IMG SRC)
filePathRaw = askdirectory(title='Select the source folder with the RAWs')
#Filepath of the RAW folder (IMD DEST)
filePathRawDEST = askdirectory(title='Select the RAWs destination folder')

for file in os.listdir(filePathJPG):
    if file.endswith(".JPG"):
        filenames.append(os.path.splitext(file)[0])

frozenSet = os.listdir(filePathRaw)
for name in filenames:
    nameSuffix = name + suffix

    if nameSuffix in frozenSet:
        targetSet = os.listdir(filePathRawDEST)

        if nameSuffix not in targetSet:
            shutil.copy2(os.path.join(filePathRaw,nameSuffix),filePathRawDEST)
