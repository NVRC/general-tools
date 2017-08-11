import shutil, os

#This utility parses the approved JPG folder and copies the respective
#RAW into the designated folder

#Useful when sorting large numbers of JPGs then copying the RAWs to later polish

#Filepath of the JPG folder (TITLE SRC)
filePathJPG = '/Users/Slate/Documents/Photos/Fuji/Vineyard/JPG'
#Filepath of the RAW folder (IMG SRC)
filePathRaw = '/Volumes/Untitled/DCIM/108_FUJI'
#Filepath of the RAW folder (IMD DEST)
filePathRawDEST = '/Users/Slate/Documents/Photos/Fuji/Vineyard/RAW'

filenames = []
suffix = '.RAF'

for file in os.listdir(filePathJPG):
    if file.endswith(".JPG"):
        filenames.append(os.path.splitext(file)[0])

for name in filenames:
    shutil.copy2(os.path.join(filePathRaw,name+suffix),filePathRawDEST)
    print(os.path.join(filePathRawDEST,name + suffix))
