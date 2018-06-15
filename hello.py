#최종 지역별 데이터 분석(전체에 대한 분석 추가)
import csv

f = open('전국무료와이파이표준데이터.csv')
place = input('어떤 곳에 배치한 와이파이 현황을 보고 싶어요?(전체, 교통시설, 서민복지, 관공서, 관광, 지역문화, 편의시설, 기타중 하나)')
data = csv.reader(f)
next(data)

tele = {}
for row in data :
    if place == '전체' :
        if row[2] not in tele :
            tele[row[2]] = 1
        else :
            tele[row[2]] += 1
    elif place in row[4] :
        if row[2] not in tele :
            tele[row[2]] = 1
        else :
            tele[row[2]] += 1
print(tele)
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
plt.bar(range(len(tele.keys())),tele.values())
plt.xticks(range(len(tele.keys())),tele.keys(), rotation = 90)
plt.show()


#최종 통신사별 데이터 분석(대소문자 무시 실패, 전체 분석 실패)
import csv

f = open('전국무료와이파이표준데이터.csv')
place = input('어떤 곳에 배치한 와이파이 현황을 보고 싶어요?(교통시설, 서민복지, 관공서, 관광, 지역문화, 편의시설, 기타중 하나)')
data = csv.reader(f)
next(data)

tele = {}
for row in data :
    if place == '전체' :
        if row[4] not in tele :
            tele[row[5][0:2]] = 1
        else :
            tele[row[5][0:2]] += 1
    elif place in row[4] :
        if row[5][:2] not in tele :
            tele[row[5][0:2]] = 1
        else :
            tele[row[5][0:2]] += 1
print(tele)
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
plt.bar(range(len(tele.keys())),tele.values())
plt.xticks(range(len(tele.keys())),tele.keys(), rotation = 90)
plt.show()
