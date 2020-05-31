import os


# employees = []
# db_path = "YoklamaKayitlari"
# if os.path.isdir(db_path):
#     for r, d, f in os.walk(db_path):  # r=root, d=directories, f = files
#         for file in f:
#             if '.xlsx' in file:
#                 exact_path = r + "/" + file
#                 employees.append(exact_path)
#
#
# print(employees)
#
# for i in employees:
#     os.remove(i)
#     print(i)

if os.path.exists("DBCreate.pyx"):
    print("True")
else:
    print("False")

veri = "Arzunaz GÜL"

print("arzunaz gül"[::-1])