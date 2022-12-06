# 만 나이 계산기 2021-06-01 by 컴닥
from datetime import datetime

# birth = str(input('양력 생일(YYYY-MM-DD)을 입력하세요. '))
birth = '1992.04.13'.replace(".","-")


birth = datetime.strptime(birth, '%Y-%m-%d').date()
print(birth)
today = datetime.now().date()
year = today.year - birth.year
koreaage = year+1
if today.month < birth.month:
    year -= 1
elif today.month == birth.month and today.day < birth.day:
    year -= 1

print(f"{birth.strftime('%Y-%m-%d')}부터 {today.strftime('%Y-%m-%d')}까지")
print(f"한국나이는 {koreaage}살입니다.")
print(f'만나이는 {year}살입니다.')


#만나이 
#한국나이는 


birth = '2000-12-29'
today = '2022-12-08'

mYear, mMonth, mDay = birth.split("-")
nYear, nMonth, nDay = today.split("-")

mYear = int(mYear)
mMonth = int(mMonth)
mDay = int(mDay)
nYear = int(nYear)
nMonth = int(nMonth)
nDay = int(nDay)

year = nYear - mYear
koreaAge = year+1

if mMonth > nMonth :
    year -= 1

elif mMonth == nMonth and mDay > nDay :
    year -= 1

print(f"한국나이는 {koreaAge}살입니다.")
print(f"외국나이는 {year}살입니다.")
