import os

curdir = r"C:\Users\dony.tawil\Desktop\perso\WPy64-3770\notebooks\Resultats"

alldirs = os.listdir(curdir)


for file in alldirs:
    text = file.split('_')
	
    for char in text:
        try:
            char = int(char) + 1000
            char = str(char)
            print(char)
        except ValueError:
            pass
	
    new_name = '_'.join(text)
    os.rename(curdir + "\\" +  file, curdir + "\\" + new_name)

	