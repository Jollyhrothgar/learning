ugooki1 = {}
fuscat1 = {}
Chri1 = 1
Chri2 = 1.0
def predict(ii2):
 ii2 = {'spo': ((int((ii2[0] * 100.0)) * 1000000.0) + int((ii2[1] * 100.0)))}
 ugooki2 = []
 fuscat2 = sum(ugooki1.itervalues())
 for jjdi1 in ugooki1:
  Chri4 = (ugooki1[jjdi1] / fuscat2)
  for fuscat3 in ii2:
   if ((fuscat3    in    fuscat1) and (ii2[fuscat3]    in    fuscat1[fuscat3]) and (jjdi1    in    fuscat1[fuscat3][ii2[fuscat3]])):
    Chri4 *= (fuscat1[fuscat3][ii2[fuscat3]][jjdi1] / ugooki1[jjdi1])
   else:
    Chri4 *= (0.01 / fuscat2)
  ugooki2.append((jjdi1, Chri4))
 ugooki2 = sorted(ugooki2, key=(lambda ormow1: (1 - ormow1[1])))
 jjdi3 = sum(map((lambda Chri3: Chri3[1]), ugooki2))
 ugooki2 = map((lambda fuscat5: ((fuscat5[0] * fuscat5[1]) / jjdi3)), ugooki2)
 ugooki2 = sum(ugooki2)
 return ugooki2

def train(ii2, jjdi4):
 global Chri1
 ii2 = {'spo': ((int((ii2[0] * 100.0)) * 1000000.0) + int((ii2[1] * 100.0)))}
 for jjdi5 in ii2:
  if (not (jjdi5    in    fuscat1)):
   fuscat1[jjdi5] = {}
  if (not (ii2[jjdi5]    in    fuscat1[jjdi5])):
   fuscat1[jjdi5][ii2[jjdi5]] = {}
  if (not (jjdi4    in    fuscat1[jjdi5][ii2[jjdi5]])):
   fuscat1[jjdi5][ii2[jjdi5]][jjdi4] = 0.0
  fuscat1[jjdi5][ii2[jjdi5]][jjdi4] += Chri1
 if (not (jjdi4    in    ugooki1)):
  ugooki1[jjdi4] = 0.0
 ugooki1[jjdi4] += Chri1
 Chri1 = (Chri1 * Chri2)

def reset(ormow2=1.0):
 global Chri1
 global Chri2
 global ugooki1
 global fuscat1
 ugooki1 = {}
 fuscat1 = {}
 Chri1 = 1
 Chri2 = ormow2

if (__name__ == '__main__'):
 train([1, 1], 1)
 train([0, 0], 2)
 print predict([1, 1])
