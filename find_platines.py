import openpyxl,os

filepath_excel="C:\\Users\\dony.tawil\\Desktop\\projet platine dony\\DS\\LOT3\\02 - Calcul\\1-pre\\1-releves"
filepath_list_platine = "C:\\Users\\dony.tawil\\Desktop\\projet platine dony\\DS"

platines = openpyxl.load_workbook(filepath_list_platine + "\\" + "Platine a calculer.xlsx")


rand_excel = openpyxl.load_workbook(filepath_excel + "NOTE_LOT3_ANNEXE1_01_1ANCRAGE.xlsx")

