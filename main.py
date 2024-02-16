# try: #Задание 1
#     print("1.Понедельник\n2.Вторник\n3.Среда\n4.Четверг\n5.Пятница\n6.Суббота\n7.Воскресенье")
#     day=int(input("Выберите день:"))
#     match day:
#      case 1:
#         print("Понедельник")
#      case 2:
#         print("Вторник")
#      case 3:
#         print("Среда")
#      case 4:
#         print("Четверг")
#      case 5:
#         print("Пятница")
#      case 6:
#         print("Суббота")
#      case 7:
#         print("Воскресенье")
#      case _:
#          print("Ведите день от 1 до 7")
#
#
# except IndexError as error:
#     print(f"Ошибка цифр: {error}")

# try: # Задание 2
#     num1=int(input("Ведите число: "))
#     num2=int(input("Ведите число:"))
#     if num1==num2:
#         print("Числа равные ")
#     else:
#         if num1>num2:
#             print("Первое Число больше",num1 ,num2)
#         else:
#             print("Второе число больше",num2,num1)
# except ValueError as error:
#     print("Ведите коректное число")


try: #Задание 3
    num1=int(input("Ведите число:"))
    num2=int(input("Ведите число:"))
    user_select=int(input("Выберите действие"))
    match user_select:
        case 1:
            result=num1+num2
            print("Додавання",result)
        case 2:
            result=num1-num2
            print("Виднимання",result)
        case 3:
            result=num1*num2
            print("Множення",result)
        case 4:
            result=num1/num2
            print("Деление",result)

except ZeroDivisionError as error:
    print(f"ZeroDivisionError occurred: {error}")
except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("End of calculation")








