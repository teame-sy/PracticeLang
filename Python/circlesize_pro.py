r = input("구의 반지름을 입력해주세요: ")
while r<0:
  r = input("구의 반지름을 입력해주세요: ")


# 부피는 s 겉넓이는 z
pi = 3.141592
s = r ** 3 * pi / 4 * 3
z = pi * r ** 2 * 4

print(" 구의 겉넓이는 {} 입니다. " .format(z))
print(" 구의 부피는 {} 입니다. ".format(s))

except Exception as exception:
  print("오류가 발생했습니다. ")
