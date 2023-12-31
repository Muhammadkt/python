numbers=[1,2,3,4,5,6,7]
even=[i for i in numbers if i%2==0]
print(even)
sqr_numbers=[i*i for i in numbers]
print(sqr_numbers)
s=set([1,2,3,4,5,2,3])
print(s)
even={ i for i in numbers if i%2==0}
print(even)

cities=["mumbai","new york","paris"]
countries=["india","usa","france"]
z=zip(cities,countries)
print(z)
for a in z:
    print(a)

d={city:country for city,country in zip(cities,countries)}
print(d)