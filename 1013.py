a, b, c = map(int, input().split())

maiorAB = (a + b + abs(a - b))/ 2
maiorAC = (a + c + abs(a - c)) / 2

if maiorAB > maiorAC:
    print("%d eh o maior" %maiorAB)
else:
    print("%d eh o maior" %maiorAC)
