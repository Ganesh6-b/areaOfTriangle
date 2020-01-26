a,b,c = map(int,input("Enter you Three sides:").split())

s = float((a+b+c)/2)

area = (s * (s-a) * (s-b) * (s-c))**0.5
print("Area of Triangle is :", area)
