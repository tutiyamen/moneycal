# 給料計算してくれる
def money(start, end):
    # 基本時給を登録
    money_per_hour = float(1000)

    # 働いた時間を計算
    work_hour = end - start
    print("労働時間は",work_hour,"時間")


    #残業深夜手当なし
    if work_hour <= 9:
        total_money = money_per_hour * work_hour

    #残業手当あり
    elif work_hour > 9:
        nomal_money = money_per_hour * work_hour
        overtime_money = money_per_hour * 0.25 * (work_hour - 9)
        total_money = nomal_money + overtime_money

    #深夜手当あり
    elif end >= 22 and work_hour <= 9:
        nomal_money = money_per_hour * work_hour
        midnight_money = money_per_hour * 0.25 * (end -22)
        total_money = nomal_money + midnight_money


    #深夜手当あり+残業手当あり
    elif end >= 22 and work_hour >= 9 :
        nomal_money = money_per_hour * work_hour
        overtime_money = money_per_hour * 0.25 * (work_hour - 9)
        midnight_money = money_per_hour * 0.25 * (end -22)
        total_money = nomal_money + overtime_money + midnight_money

    else:
        print("eorr")

    return total_money



total = money(float(input("開始時間を記入")),float(input("終了時間を記入")))

print("給料は",total,"円")
