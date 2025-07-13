import os
import shutil


thisDir = os.getcwd()
print(thisDir)

filesInDir = os.listdir()
print(filesInDir)

copyFile = shutil.copy('hw1.py', 'copyhw1.py')

severalFolders = os.makedirs('C:/Users/Ім'я_користувача/Desktop/pythonproj/')