# SearchAstroFields
Перед началом запуска программы, следует кастомизировать четыре строки.
1) Для первой переменной "m" зададим путь к файлу с координатами объектов, координаты должны быть в градусах.
2) Второй переменной "field" мы присваиваем размеры поля (в градусах) используемого телескопа.
3) В переменной "cols" указываем номера столбцов с координатами из исходной таблицы. Отсчёт столбцов правильно начинать с нуля.
4) В последней строке в функции "np.savetxt" указываем название и формат итогового файла.
Если у используемого телескопа присутствует сильное виньетирование, то рекомендуется сократить размеры поля до области с приемлемым виньетированием. Это можно реализовать в переменной "field".
Выполнив вышеперечисленные процедуры, запускаем расчёты как обычный Python код.
