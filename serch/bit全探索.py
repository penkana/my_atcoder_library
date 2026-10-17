def bit_serch(N):
    for i in range(2 ** N):
        for j in range(N):  # このループが一番のポイント
            if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                pass  # フラグが立っていたら処理する

# N <= 20 で使える