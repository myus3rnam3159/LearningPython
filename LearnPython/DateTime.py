import calendar
from datetime import datetime, timedelta

now = datetime.now()

#Time delta - tạo khoảng cách thời gian
#Lấy ngày này + 1 năm 5 h 1 phút sau đó

print("Ngày đó là". str(now + timedelta(days=365, hours=5, minutes=1)))

#Calendar
#Chọn tuần bắt đầu từ chủ nhật
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2022, 1, 0, 0)
print(str)

#Lặp qua các ngày của tháng 8
for i in c.itermonthdays(2022, 8):
    print(i)

#Lặp qua các tên tháng
for name in calendar.month_name:
    print(name)

#Lặp qua các ngày trong tuần
for day in calendar.day_name:
    print(day)

#Một nhóm sẽ vào thứ 6 đầu tiên mỗi tháng
#Tìm ra những ngày đó là ngày náo

#Lặp qua các thàng từ 1 đến 12
for m in range(1, 13):
    #Lấy lịch mỗi tháng
    cal = calendar.monthcalendar(2022, m)
    #Thứ 6 đầu tiên chỉ có thẻ trong 2 tuần đầu
    weekone = cal[0]
    weektwo = cal[1]

    #Nếu nó nằm trong tuần đầu
    if weekone[calendar.FRIDAY] != 0:
        meetday = weektwo[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    
    print(calendar.month_name[m], meetday)

