import time
n=int(input('Введите время.\nУточнение.Вы вводите время в секундах'))
time_format = time.strftime("%H:%M:%S", time.gmtime(n))
print("Время в предпочтительном формате. :-",time_format)


time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")
