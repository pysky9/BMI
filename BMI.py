high = eval(input("Please fill in your height(cm): ")) / 100
weight = eval(input("Please fill in your weight(kg): "))
BMI = weight / high**2
print("你的BMI為 {} ".format(BMI))
if BMI < 18.5 :
	print("你的體重過輕")
elif BMI < 24 :
	print("你的BMI標準")
elif BMI < 27 :
	print("你的體重過重")
elif BMI < 30 :
	print("你輕度肥胖")
elif BMI < 35 :
	print("你中度肥胖")
else :
	print("你重度肥胖")