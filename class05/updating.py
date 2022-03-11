# with open("newfile.txt","r+", encoding="utf-8") as file:
#     file.seek(23)
#     file.write("\nEmine Kartal")

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())

# ***** Sayfa sonunda güncelleme *****

# with open("newfile.txt","a", encoding="utf-8") as file:
#     file.write("\nGünaydın Kartal")

# ***** Sayfa başında güncelleme *****

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Metin Kartal\n" + content
#     file.seek(0)
#     file.write(content)



# ***** Sayfa ortasında güncelleme *****

with open("newfile.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(6, "Merve Kartal\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())
