#ДЗ 6.2. Конвертер із числа в дату
#8639999 -> 99 днів, 23:59:59
var=8639999
print(var," => ", end="")
h1=3600
d1=86400
lst1=[1]
lst2=[2, 3, 4]
lst3=[5, 6, 7, 8, 9, 0]
lst4=[11,12,13,14]
#дні
var_day=var//d1
day_word=str(var_day)
d=int(day_word[-1])
dd=int(day_word)
#день-дні-днів
if dd in lst4:
   print(var_day, "днів, ", end="")
elif d in lst1:
   print(var_day, "день, ", end="")
elif d in lst2:
   print(var_day, "дні, ", end="")
elif d in lst3:
   print(var_day, "днів, ", end="")
#години
var_day_end=var%d1
var_hour=var_day_end//h1
var_hour=str(var_hour)
var_hour=var_hour.zfill(2)
print(var_hour,":", end="")
#хвилини
var_hour_end=var_day_end%h1
var_minute=var_hour_end//60
var_minute=str(var_minute)
var_minute=var_minute.zfill(2)
print(var_minute, ":", end="")
#секунди
var_minute_end=var_hour_end%60
var_minute_end=str(var_minute_end)
var_minute_end=var_minute_end.zfill(2)
print(var_minute_end, end="")
