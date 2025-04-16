# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
 # Docs:
 # https://dateutil.readthedocs.io/en/stable/relativedelta.html
 # https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


data = datetime(2024,3,15, 15, 58, 15, 45)


print(data)



datas_str = '2024-06-28 07:45:40'
datas_str_fmt = '%Y-%m-%d %H:%M:%S'

data = datetime.strptime(datas_str, datas_str_fmt)
print(data)


data = datetime.now() 
print(data)


tims = datetime.now().timestamp() 
print(tims)
print(datetime.fromtimestamp(tims))
delta = timedelta(seconds= 5, days=2)
print(data)
print(data - delta)

## verificar a diferença entre duas datas virando m delta que vcoe pode aplicar em outra data
delta_relativo = relativedelta(data, (data-delta))
print(delta_relativo)

## formatar datas
fmt = '%d/%m/%Y'

data = datetime.strptime('2022-12-13 07:05:15', '%Y-%m-%d %H:%M:%S')
print(data)

print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%d'), data.day)
print(data.strftime('%m'), data.month)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)