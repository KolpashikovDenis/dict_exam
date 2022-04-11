def avg(l):
    return round(sum(l)/len(l), 1)

ids = ['1111:271', '1111:190', '1231:106', '1211:104', '1111:201', '1231:120', '1001:205', '1001:223', '1001:127', '1001:236', \
      '1111:229', '1231:286', '1231:195', '1001:279', '1001:124', '1111:292', '1505:219', '1231:259', '1231:253', '1001:220', '1001:202',\
      '1231:103', '1211:249', '1212:275']
count = [111, 3, 13, 111, 9, 5, 17, 10, 13, 3, 16, 4, 16, 11, 18, 12, 14, 4, 3, 2, 14, 14, 10, 10]

items_count = {k:v for k, v in zip(ids, count)}

categories = set([x.split(':')[0] for x in items_count.keys()])


tmp = {}
c = 0
for cat in categories:
    for key in items_count.keys():
        if cat in key:
            if cat in tmp.keys():
                tmp[cat].append(items_count[key])
                c += 1
            else:
                c = 0
                tmp[cat] = [items_count[key]]
print({k:avg(tmp[key]) for k in tmp.keys()})
print(tmp)