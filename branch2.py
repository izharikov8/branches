salary = int(input("Введите заработную плату в месяц: "))
mortage = int(input("Введите, какой (%) уходит на ипотеку: "))
expenses = int(input("Введите, какой (%) уходит на жизнь: "))
print()
print("Вывод:")
print()
print("На ипотеку было потрачено: ", (salary // 100) * mortage * 12, "рублей")
print("Было накоплено: ", (salary - (salary // 100) * (expenses + mortage)) * 12, "рублей")
print("Pay button")
<<<<<<< HEAD
print("Script metrika")
=======
print("Google analytics")
>>>>>>> feature/analytics
