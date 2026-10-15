#profile generator
#taking input from user about their name,age,height(in mtr)
name = input("Enter your name: ")
age = int(input("Enter your current age: "))
height = float(input("Enter your current height(in mtr): "))
is_study = bool(input("Are you studying: "))

print(name,"of age",age,"is standing over",height,"is currently studying:",is_study)
print("data type of name,age,height,is_study is",type(name),type(age),type(height),type(is_study),"respectively")