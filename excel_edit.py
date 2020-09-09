Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import openpxl
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import openpxl
ModuleNotFoundError: No module named 'openpxl'
>>> import openpyxl
>>> import os
>>> os.getcwd()
'C:\\Users\\dony.tawil\\Desktop\\perso\\WPy64-3770\\notebooks'
>>> os.chdir(r'C:\Users\dony.tawil\Desktop\projet platine dony\DE\Entrainement\DS_entrainement\LOT1\02 - Calcul\1-pre\1-releves')
>>> os.listdir
<built-in function listdir>
>>> os.listdir()
['FICHIER ROBOT', 'NOTE_LOT1_ANNEXE1_01_1ANCRAGE.xls', 'NOTE_LOT1_ANNEXE1_02_1ANCRAGE.xls', 'NOTE_LOT1_ANNEXE1_03_1ANCRAGE.xls', 'NOTE_LOT1_ANNEXE1_04_1ANCRAGE.xls', 'NOTE_LOT1_ANNEXE1_05_1ANCRAGE.xls', 'NOTE_LOT1_ANNEXE1_06_1ANCRAGE.xls', 'NOTE_LOT1_ANNEXE1_07_1ANCRAGE.xls', 'NOTE_LOT1_ANNEXE1_08_1ANCRAGE.xls', 'NOTE_LOT1_ANNEXE1_09_1ANCRAGE.xls', 'NOTE_LOT1_ANNEXE1_10_1ANCRAGE.xls', 'NOTE_LOT1_ANNEXE1_20_2ANCRAGES.xls', 'NOTE_LOT1_ANNEXE1_21_2ANCRAGES.xls', 'NOTE_LOT1_ANNEXE1_22_2ANCRAGES.xls', 'NOTE_LOT1_ANNEXE1_23_2ANCRAGES.xls', 'NOTE_LOT1_ANNEXE1_24_2ANCRAGES.xls', 'NOTE_LOT1_ANNEXE1_25_2ANCRAGES.xls', 'NOTE_LOT1_ANNEXE1_26_2ANCRAGES.xls', 'NOTE_LOT1_ANNEXE1_27_2ANCRAGES.xls', 'NOTE_LOT1_ANNEXE1_28_2ANCRAGES.xls', 'NOTE_LOT1_ANNEXE1_29_1ANCRAGES.xls', 'Renum_Pages.xls']
>>> alldir = os.listdir()
>>> my_platines = ['HRA11SE4095', 'HRA15SE5470', 'HRB02SE9009_sup']
>>> for dir in alldir:
	if '.xls' in dir:
		print(dir)

		
NOTE_LOT1_ANNEXE1_01_1ANCRAGE.xls
NOTE_LOT1_ANNEXE1_02_1ANCRAGE.xls
NOTE_LOT1_ANNEXE1_03_1ANCRAGE.xls
NOTE_LOT1_ANNEXE1_04_1ANCRAGE.xls
NOTE_LOT1_ANNEXE1_05_1ANCRAGE.xls
NOTE_LOT1_ANNEXE1_06_1ANCRAGE.xls
NOTE_LOT1_ANNEXE1_07_1ANCRAGE.xls
NOTE_LOT1_ANNEXE1_08_1ANCRAGE.xls
NOTE_LOT1_ANNEXE1_09_1ANCRAGE.xls
NOTE_LOT1_ANNEXE1_10_1ANCRAGE.xls
NOTE_LOT1_ANNEXE1_20_2ANCRAGES.xls
NOTE_LOT1_ANNEXE1_21_2ANCRAGES.xls
NOTE_LOT1_ANNEXE1_22_2ANCRAGES.xls
NOTE_LOT1_ANNEXE1_23_2ANCRAGES.xls
NOTE_LOT1_ANNEXE1_24_2ANCRAGES.xls
NOTE_LOT1_ANNEXE1_25_2ANCRAGES.xls
NOTE_LOT1_ANNEXE1_26_2ANCRAGES.xls
NOTE_LOT1_ANNEXE1_27_2ANCRAGES.xls
NOTE_LOT1_ANNEXE1_28_2ANCRAGES.xls
NOTE_LOT1_ANNEXE1_29_1ANCRAGES.xls
Renum_Pages.xls
>>> for dir in alldir:
	if '.xls' in dir:
		wb=openpyxl.load_workbook(dir)
		cur_platine = my_platines.pop(0
KeyboardInterrupt
>>> while len(my_platines) > 0:
	cur_platine = my_platines.pop(0)
	for dadir in alldir:
		if '.xls' in dadir:
			wb = openpyxl.load_workbook(dadir)
			if cur_platine in wb.sheetnames:
				print(cur_platine + " :" + dadir)

				
Traceback (most recent call last):
  File "<pyshell#22>", line 5, in <module>
    wb = openpyxl.load_workbook(dadir)
  File "C:\Users\dony.tawil\AppData\Roaming\Python\Python37\site-packages\openpyxl\reader\excel.py", line 311, in load_workbook
    data_only, keep_links)
  File "C:\Users\dony.tawil\AppData\Roaming\Python\Python37\site-packages\openpyxl\reader\excel.py", line 126, in __init__
    self.archive = _validate_archive(fn)
  File "C:\Users\dony.tawil\AppData\Roaming\Python\Python37\site-packages\openpyxl\reader\excel.py", line 96, in _validate_archive
    raise InvalidFileException(msg)
openpyxl.utils.exceptions.InvalidFileException: openpyxl does not support the old .xls file format, please use xlrd to read this file, or convert it to the more recent .xlsx file format.
>>> while len(my_platines) > 0:
	cur_platine = my_platines.pop(0)
	for dadir in alldir:
		if '.xls' in dadir:
			wb = openpyxl.load_workbook(dadir + "x")
			if cur_platine in wb.sheetnames:
				print(cur_platine + " :" + dadir)

				
Traceback (most recent call last):
  File "<pyshell#30>", line 5, in <module>
    wb = openpyxl.load_workbook(dadir + "x")
  File "C:\Users\dony.tawil\AppData\Roaming\Python\Python37\site-packages\openpyxl\reader\excel.py", line 311, in load_workbook
    data_only, keep_links)
  File "C:\Users\dony.tawil\AppData\Roaming\Python\Python37\site-packages\openpyxl\reader\excel.py", line 126, in __init__
    self.archive = _validate_archive(fn)
  File "C:\Users\dony.tawil\AppData\Roaming\Python\Python37\site-packages\openpyxl\reader\excel.py", line 98, in _validate_archive
    archive = ZipFile(filename, 'r')
  File "C:\Users\dony.tawil\Desktop\perso\WPy64-3770\python-3.7.7.amd64\lib\zipfile.py", line 1240, in __init__
    self.fp = io.open(file, filemode)
FileNotFoundError: [Errno 2] No such file or directory: 'NOTE_LOT1_ANNEXE1_01_1ANCRAGE.xlsx'
>>> 
