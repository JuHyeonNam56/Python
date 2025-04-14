it = 4
at = 10
bt = 10
while it > 1:
    print(it)
    it = it - 1

print('while loop execution is done')
print("************************************************")
while at > 1:
    if at == 3:
        break
    print(at)
    at = at - 1
print("************************************************")

while bt > 1:
       if bt == 9:
           bt = bt - 1
           continue
       if bt == 3:
           break
       print(bt)

       bt = bt - 1

print('while 문안에 if 문을 넣어 일정 값을 제외 시키는 방법')