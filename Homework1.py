FIO = ["станевич", "михаил", "андреевич"]
name = FIO[1]
lastname = FIO[0]
middlename = FIO[2]


"""вывод переменной с заглавной буквы"""
phrase = f"Мой друг {name.title()}"
print(phrase)


"""удаление методом remove"""
FIO.remove("андреевич")
print(FIO)