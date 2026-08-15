name = input("enter your name ")
age = int(input("enter your age "))
print("Hello", name, ", you are", age, "years old")

length = float(input("enter the length of rectangle "))
width = float(input("enter the width of rectangle "))
print("The area = ", length * width)

names = ["Haneen","Ahmed","Shahd","Ali","Omar","Fatma","Jana"]
names.append("Merna")
print(names)
names.pop(2)
print(names)
names.sort()
print(names)

count = 0
for name in names:
    if name.startswith("A"):
        count += 1
print("The number of names that start with A is:", count)

nums = ('1', '20', '55', '16','3')
print(max(nums))
print(min(nums))
print(sum(int(num) for num in nums))
list = list(nums)
list.append('70')
list.append('14')
print(list)
tuple = tuple(list)
print(tuple)

products = {
    "pizza": 10,
    "shawerma": 5,
    "burger": 7,
    "cola": 8}
print(products)
price = 0

while True:
    pdt = input("enter the product name ")
    if pdt == "exit":
        break
    if pdt in products:
        print("the price of", pdt, "is", products[pdt])
        price += products[pdt]
    else :
        print("Product not found")
print("Total price:", price)