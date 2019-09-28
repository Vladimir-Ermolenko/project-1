#Gives a list of data based on the users date of birth
import math
byr = int(input("Введите год Вашего рождения:"))
age = int(2019-byr)

#The users age in diff. values
mhs = int(age*12)
ds = int(age*365)
hs = int(ds*24)
ms = int(hs*60)
ss = int(ms*60)

#Appr. volume of air  the user has inhaled
vd = int(4665600) #л в год
vf = int(vd*age)
nf = float(vf*0.78)
of = float(vf*0.2)
arf = float(vf*0.01)
orf = float(vf*0.01)
print(" За свою жизнь", "Вы вдохнули", vf, "литров воздуха.",
      '\n', "Из этого:",
      '\n', nf, "азота"
      '\n', of, "кислорода"
      '\n', arf, "аргона"
      '\n', orf, "прочего", '\n')

#Appr. number of turnovers  the Earth has done
ti = age
ts = ds
print(" За вашу жизнь", "Земля сделала:",
      '\n', ti, "об. вокруг своей оси"
      '\n', ts, "об. вокруг Солнца", '\n')

#Appr. number of people born and died during users lifetime
nb = float(146.5*age)
nd = float(57.9*age)
print(" За вашу жизнь:",
      '\n', "родилось", nb, "мил. человек",
      '\n', "умерло", nd, "мил. человек")