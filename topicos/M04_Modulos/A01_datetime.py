from datetime import datetime


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

