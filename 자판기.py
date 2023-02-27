food = ['1.콜라','2.사이다','3.사과주스','4.식혜']
foodname = ['콜라','사이다','사과주스','식혜']
price = [1500,1500,1200,1100]
money = 5000
er = "내용없음"

while True:
    print("=----자판기입니다----=")
    print()
    print(food)
    print(price)
    print("현재 소유하신 돈 >", money)
    print("내용:", er)
    print()
    print("=------------------=")
    sel = int(input(">"))
    if sel > 4:
        er = "올바르지 않은 번호"
    elif sel <= 0:
        er = "올바르지 않은 번호"
    else:
        print("선택하신 상품 >", foodname[sel-1])
        if money < price[sel-1]:
            er = "돈이 부족합니다 다음에 이용해주세요"
        else:
            money = money - price[-1]
            er = foodname[sel-1] + "를 구매해주셔서 감사합니다"
