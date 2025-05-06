# ----------------------------------------------
# 데이터 읽어 오기
# 함수기능 :  데이터 읽어오기
# 리턴 함수 : 없음
# ----------------------------------------------

def print_info( df, dfname ):
    df.info()
    print(f"{dfname} head() ====== \n{df.head(2)}")
    print(f"{dfname} tail() ====== \n{df.tail(2)}")
    print(f"{dfname} shape() ====== \n{df.shape}")
    print(f"{dfname} descirb ====== \n{df.describe()}")

