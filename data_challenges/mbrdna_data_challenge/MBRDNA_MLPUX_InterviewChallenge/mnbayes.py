num_entries_per_category = {}
fuscat1 = {} # {'spo':}
int_one = 1
float_one = 1.0

def predict(features):
    features = {'spo': ((int((features[0] * 100.0)) * 1000000.0) + int((features[1] * 100.0)))}
    ugooki2 = []
    fuscat2 = sum(num_entries_per_category.itervalues())
    for jjdi1 in num_entries_per_category:
        Chri4 = (num_entries_per_category[jjdi1] / fuscat2)
        for fuscat3 in features:
            if ((fuscat3    in    fuscat1) and (features[fuscat3]    in    fuscat1[fuscat3]) and (jjdi1    in    fuscat1[fuscat3][features[fuscat3]])):
                Chri4 *= (fuscat1[fuscat3][features[fuscat3]][jjdi1] / num_entries_per_category[jjdi1])
            else:
                 Chri4 *= (0.01 / fuscat2)
        ugooki2.append((jjdi1, Chri4))
    ugooki2 = sorted(ugooki2, key=(lambda ormow1: (1 - ormow1[1])))
    jjdi3 = sum(map((lambda Chri3: Chri3[1]), ugooki2))
    ugooki2 = map((lambda fuscat5: ((fuscat5[0] * fuscat5[1]) / jjdi3)), ugooki2)
    ugooki2 = sum(ugooki2)
    # This seems to be a number that is either 0, very small, 0.5 or very nearly
    # 1
    #print ugooki2
    return ugooki2

def train(features, label):
    global int_one
    features = {'spo': ((int((features[0] * 100.0)) * 1000000.0) + int((features[1] * 100.0)))}
    for feature_key in features:
        # fuscat1 is a global variable
        if feature_key not in fuscat1:
            fuscat1[feature_key] = {} 
        if features[feature_key] not in fuscat1[feature_key]:
            fuscat1[feature_key][features[feature_key]] = {}
        if label not in fuscat1[feature_key][features[feature_key]]:
            fuscat1[feature_key][features[feature_key]][label] = 0.0
        fuscat1[feature_key][features[feature_key]][label] += int_one
    if label not in num_entries_per_category:
        num_entries_per_category[label] = 0.0
    num_entries_per_category[label] += int_one
    int_one = (int_one * float_one)


def reset(set_float_one=1.0):
    global int_one
    global float_one
    global num_entries_per_category
    global fuscat1
    num_entries_per_category = {}
    fuscat1 = {}
    int_one = 1
    float_one = set_float_one

if (__name__ == '__main__'):
    train([1, 1], 1)
    train([0, 0], 2)
    #print predict([1, 1])
