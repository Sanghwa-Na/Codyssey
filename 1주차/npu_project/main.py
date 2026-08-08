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

def run_mode_1():
    pass
def run_mode_2():
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