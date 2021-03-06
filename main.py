#1.	Напишите функцию, принимающую предложение с числами,
#представляющими расположение слова, встроенного в каждое слово,
#и верните отсортированное предложение.

import re
a=input("Enter text: ")

b = a.split()#используем split() для разделения слов в тексте
q=""
for i in sorted(b,key=lambda a: sorted(a)):#теперь сортируем слова (используем анонимную функцию)
    q = q + " " + i
    q = re.sub(r"\d+", "", q, flags=re.UNICODE)#удаляем все цифры из строки
print(q)



#2.	Напишите функцию, которая принимает три измерения кирпича:
#высоту(a), ширину(b) и глубину(c) и возвращает true,
#если этот кирпич может поместиться в отверстие с шириной(w) и высотой(h).


a=int(input('введите высоту:'))
b=int(input('введите ширину:'))
c=int(input('введите глубину:'))
w=int(input('введите ширину отверстия:'))
h=int(input('введите высоту отверстия:'))
if b<=w and a<=h:
    print('true')
elif b<=h and a<=w:#похож на 1 вариант, но разворачиваем на 90 градусов
    print('true')
elif c<=w and a<=h:#до этого вдоль, сейчас поперёк
    print('true')
elif c<=h and a<=w:#снова разварачиваем предыдущий вариант на 90 градусов
    print('true')
else:
    print('кирпич не поместился')


#3.	Паутина определяется кольцами, пронумерованными от 0 до 4 от центра, и радиалами,
# помеченными по часовой стрелке сверху как A-H.
#Создайте функцию, которая принимает координаты паука и мухи и возвращает кратчайший
# путь для паука, чтобы добраться до мухи.