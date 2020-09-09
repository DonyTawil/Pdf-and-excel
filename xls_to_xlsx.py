import win32com.client as win32
fname = r"C:\Users\dony.tawil\Desktop\perso\WPy64-3770\notebooks\synthese images contraintes 2.xls"
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(fname)

wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
wb.Close()                               #FileFormat = 56 is for .xls extension
excel.Application.Quit()