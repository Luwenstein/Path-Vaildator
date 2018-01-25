import _winreg, os, sys, logging
from _winreg import ConnectRegistry, OpenKey, CloseKey, CreateKey, QueryInfoKey, SetValueEx

logging.basicConfig(filename='Log.txt',level=logging.DEBUG)
curnt = (os.path.dirname(os.path.realpath(__file__)))+'\\'
logging.info(curnt)

installDir = ("C:\Program Files\Path_Validator\\")
Infile = ("Path_Validator-V1.0-Windows-x86.exe")

print curnt+Infile
print installDir+Infile

if not os.path.exists(installDir):
    os.makedirs(installDir)
    
try:
    os.rename(curnt+Infile, installDir+Infile)
except WindowsError as er:
    logging.exception("\n\n Something Has Gone Wrong!")
    exit()

 #Registry Setup, DONT TOUCH THESE

keyVal = r'Directory\Background\shell\Validate Paths\\command'

try:
    key = OpenKey(_winreg.HKEY_CLASSES_ROOT, keyVal, 0, _winreg.KEY_ALL_ACCESS)
except:
    key = CreateKey(_winreg.HKEY_CLASSES_ROOT, keyVal)

SetValueEx(key, "", 0, _winreg.REG_SZ, r"C:\Program Files\Path_Validator\Path_Validator-V1.0-Windows-x86.exe %V")

CloseKey(key)
exit()
