import os
import datetime

result = dir(os)
result = os.name

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

# klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/yeniklasör")

# listeleme
# result = os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


# etkin dizin öğrenme
# result = os.getcwd()


# result = os.stat("zaman.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

# os.system("notepad.exe")

# path

result = os.path.abspath("isletimSistemi.py")
result = os.path.dirname("C:/Users/Admin/VSCode/Python/isletimSistemi.py")
result = os.path.dirname(os.path.abspath("isletimSistemi.py"))
result = os.path.exists("C:/Users/Admin/VSCode/Python/isletimSistemi1.py")
result = os.path.exists("C:/Users/Admin/VSCode/Python")
result = os.path.isdir("C:/Users/Admin/VSCode/Python")
result = os.path.isfile("C:/Users/Admin/VSCode/Python/isletimSistemi.py")

print(result)
