#���� ������ ������ �м�(��ü�� ���� �м� �߰�)
import csv

f = open('���������������ǥ�ص�����.csv')
place = input('� ���� ��ġ�� �������� ��Ȳ�� ���� �;��?(��ü, ����ü�, ���κ���, ������, ����, ������ȭ, ���ǽü�, ��Ÿ�� �ϳ�)')
data = csv.reader(f)
next(data)

tele = {}
for row in data :
    if place == '��ü' :
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


#���� ��Ż纰 ������ �м�(��ҹ��� ���� ����, ��ü �м� ����)
import csv

f = open('���������������ǥ�ص�����.csv')
place = input('� ���� ��ġ�� �������� ��Ȳ�� ���� �;��?(����ü�, ���κ���, ������, ����, ������ȭ, ���ǽü�, ��Ÿ�� �ϳ�)')
data = csv.reader(f)
next(data)

tele = {}
for row in data :
    if place == '��ü' :
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
