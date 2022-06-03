class Cat:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
cat=Cat()
cat.name="0"
cat.drink()
cat.eat()
print(cat)
print("%d"%id(cat))
print("%x"%id(cat))
cat1=Cat()
cat1.drink()
cat1.eat()
print(cat1)
print("%d"%id(cat1))
print("%x"%id(cat1))
cat2=cat1
print("%d"%id(cat2))
print("%x"%id(cat2))
