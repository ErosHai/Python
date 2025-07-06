user_weight = float(input('Your Weight is(kg): '))
user_height = float(input('Your Height is(m): '))

user_BMI = user_weight / user_height ** 2

result = round(user_BMI,1)

if user_BMI >= 28:
    print('肥胖',result)
elif 24 <= user_BMI < 28:
    print('超重',result)
elif 18.5 <= user_BMI <=24:
    print('正常',result)
else:
    print('偏瘦',result)