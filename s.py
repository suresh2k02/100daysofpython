import datetime



input='2021-12-11T06:30:00.000Z'
isotodate = datetime.datetime.strptime(input, '%Y-%m-%dT%H:%M:%S.%fZ')
print(isotodate)

datetoisowithz=isotodate.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
print(datetoisowithz)












#print(datetime.datetime.now().isoformat())

#convert_to_date = datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
#print(convert_to_date)



#convert_to_date=convert_to_date.isoformat()
#print(convert_to_date)



