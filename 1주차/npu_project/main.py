import json
import time

EPS = 1e-9 # 동점판단 기준 허용 오차범위

class Matrix:
    def __init__(self, n):
        self.n = n # 매트릭스 크기
        self.data = [[0,0] * n for _ in range(n)] # 매트릭스 초기화

    def set(self, r, c, v): #row colum value
        self.data[r][c] = v

    def get(self, r, c):
        return self.data[r][c]
 
def read_matrix(name, n=3): # 모드 1, n줄 입력 > matrix 만들어 반환
    print(f"{name} {n}줄 {n}개 입력, 공백구분")
    while True:
        rows = []
        for i in range(n):
            line = input().strip() # 공백으로 나눔
            if len(n) != n :
                print(f"")

def mac(pattern, filt): # 같은 자리 다 곱해서 더하기
    n = pattern.n # 매트릭스.n attr
    score = 0.0 # 합

    for r in range(n):
        for c in range(n):
            score += pattern.get(r, c) * filt.get(r, c)
    return score

def nomalize_label(raw): # 똑같은 의미로 정규화작업
    table = {'+':'Cross', 'x':'X', 'cross':'Cross'}
    key = str(raw).strip().lower()

    return table.get(key)



def list_to_matrix(arr): # json 리스트를 matrix로 변경
    n = len(arr) 
    m = Matrix(n)

    for r in range(n):
        for c in range(n):
            m.set(r, c, float(arr[r][c])) # 실제 환경에는 소수점 쓰니 flaot)
    return m



def run_mode_1(): # 사용자입력
    pass
def run_mode_2(): # json 입력
    pass
def main():
    print("--- mini npu simulator ---")
    print("\n -모드선택-")
    print("1. 사용자입력 (3x3)")
    print("2. data.json 분석")

    choice = input("선택 : ").strip()

    if choice == 1:
        run_mode_1()
    elif choice == 2:
        run_mode_2()
    else:
        print("1 또는 2를 입력하세요")

    if __name__ == '__main__':
        main()