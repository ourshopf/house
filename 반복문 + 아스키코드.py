while True:
    num = str(input("문자를 입력해주세요 >"))
    num1 = int(input("정수를 입력해주세요 >"))
    num = ord(num)
    for count in range(num1+1):
        if count == 26:
            count = 0
    print(chr(count + num))
