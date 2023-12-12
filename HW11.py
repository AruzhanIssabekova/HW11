import datetime

# d=input()
# f=datetime.datetime.strptime(d, '%Y,%m,%d')
# h=f.isocalendar()
# print(h[1])

# d=list(map(int,input().split(',')))
# k=datetime.date(d[0],1,1)
# s=k.weekday()
# a=k.isocalendar()
# if a[1]==d[1]:
#     print('пн 1 январь 00:00:00', d[0])
# else:
#     m = d[1] * 7 - s
#     l = k + datetime.timedelta(days=m)
#     match l.month:
#         case 1:
#             h = 'январь'
#         case 2:
#             h = 'февраль'
#         case 3:
#             h = 'март'
#         case 4:
#             h = 'апрель'
#         case 5:
#             h = 'май'
#         case 6:
#             h = 'июнь'
#         case 7:
#             h = 'июль'
#         case 8:
#             h = 'август'
#         case 9:
#             h = 'сентябрь'
#         case 10:
#             h = 'октябрь'
#         case 11:
#             h = 'ноябрь'
#         case 12:
#             h = 'декабрь'
#     print('пн', l.day, h, '00:00:00', d[0])


# f=int(input())
# g=datetime.datetime(f,1,1)
# h=g.weekday()
# a=[]
# if h==6:
#     while True:
#         k=datetime.timedelta(days=7)
#         l=g+k
#         w=l.isocalendar()
#         q=l.date()
#         if w[0]!=f:
#             break
#         else:
#             a.append(q)
#         print(g.date())
#         g=l
#     for i in a:
#         print(i)
# else:
#     while True:
#         m=datetime.timedelta(days=1)
#         z=g+m
#         d=z.isocalendar()
#         if d[2]==7:
#             break
#         g=z
#     while True:
#         k=datetime.timedelta(days=7)
#         l=z+k
#         w=l.isocalendar()
#         q=l.date()
#         if w[0]!=f:
#             break
#         else:
#             a.append(q)
#         print(z.date())
#         z=l
#     for i in a:
#         print(i)

# def addYears(date,sh):
#     d1=date.year
#     d2=date.month
#     d3=date.day
#     result=datetime.date(d1+sh,d2,d3)
#     return result
# print(addYears(datetime.date(2015,1,1),-2))


# m=datetime.datetime.now()
# g=datetime.datetime.utcnow()
# print(m.time(),g.time(), sep='\n')

# d1=input()
# f1=datetime.datetime.strptime(d1, '%Y,%m,%d')
# d2=input()
# f2=datetime.datetime.strptime(d2, '%Y,%m,%d')
# delta=abs(f2-f1)
# print(delta.days)

# d1=input()
# f1=datetime.datetime.strptime(d1, '%Y,%m,%d,%H,%M,%S')
# d2=input()
# f2=datetime.datetime.strptime(d2, '%Y,%m,%d,%H,%M,%S')
# delta=abs(f2-f1)
# h=delta.seconds//3600
# m=(delta.seconds-h*3600)//60
# s=delta.seconds-h*3600-m*60
# print(delta.days, h, 'hours', m, 'minutes', s, 'seconds')