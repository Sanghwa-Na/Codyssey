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
    print(f"{name} {n}줄 {n}개 입력, 공백으로 구분")
    while True:
        rows = [] # 입력 받는 행
        for i in range(n):
            line = input().strip() # 공백으로 나눔
            if len(line) != n :
                print(f"{n}개의 숫자를 공백으로 구분해 입력하세요")
                break
            try:
                rows.append([float(c) for c in line])
            except ValueError:
                print(f"숫자만 입력해 주세요")
                break
        if len(rows) == n:
            return list_to_matrix(rows)
        
        print(f"다시 입력해 주세요")

def list_to_matrix(arr): # json 리스트를 matrix로 변경
    n = len(arr) 
    m = Matrix(n)

    for r in range(n):
        for c in range(n):
            m.set(r, c, float(arr[r][c])) # 실제 환경에는 소수점 쓰니 flaot)
    return m

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

def decide_label(score_cross, score_x): # cross, x 점수 비교
    if abs(score_cross - score_x) < EPS: # 차이가 너무 작으면 판정불가
        return "UNDECIDED"
    elif score_cross > score_x:
        return "Cross"
    else:
        return "X"

def decide_ab(score_a, score_b): # a, b 점수 비교
    if abs(score_a - score_b) < EPS: # 차이가 너무 작으면 판정불가
        return "UNDECIDED"
    elif score_a > score_b:
        return "A"
    else:
        return "B"

def measure(pattern, filter, repeat = 10): # 성능 측정, mac 반복 수행 후 평균값 반환
    start = time.time()
    for i in range(repeat):
        mac(pattern, filter)
    end = time.time()

    return (end - start) / repeat

def run_mode_1(): # 사용자입력
    print("-"*20)
    print("1. 필터 입력")
    flit_a = read_matrix("필터A")
    flit_b = read_matrix("필터B")

    print("-"*20)
    print("2. 패턴 입력")
    print*("-"*20)
    pattern = read_matrix("패턴")

    print("-"*20)
    print("3. MAC 수행 결과")
    print("-"*20)
    score_a = mac(pattern, flit_a)
    score_b = mac(pattern, flit_b)
    time = measure(pattern, flit_a)

    print(f"A score : {score_a:.2f}")
    print("-"*20)
    print(f"B score : {score_b:.2f}")
    print("-"*20)
    print(f"Time : {time:.6f}") # 연산 시간(평균/10회)
    print("-"*20)

    result = decide_ab(score_a, score_b)
    if result == "UNDECIDED":
        print("판정불가")
    else:
        print(f"판정 : {result}")   

def run_mode_2(): # json 입력
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("data.json 파일이 없습니다")
        return

    print("-"*20)
    print("1. 필터 로드")
    print("-"*20)
    flit = {} #{필터 이름: 필터 매트릭스}
    for size_key, label_dict in data.items():
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