str1= "программировать"
str2="учеба"
str3="Я люблю программировать"
str4="ЪЪЪ"
#конкатенации срок
print(str1+str2)
#повторение строк
print(str4*3)
#обращения по индексу
print(str1[3])
#извлечения среза
print(str1[1:8:3])
#определение длины строки
print(len(str3))
#подсчёт количества вхождений подстроки л в строку str3
print(str3.count('ю', 1, 8), )
#поиск подстроки в строке
print(str2.find('а',1,5))
#разбиение строки по разделителю
print(str2.split('е'))
#преобразование строки к верхнему или нижнему регистру
print(str2.upper())
print(str2.lower())