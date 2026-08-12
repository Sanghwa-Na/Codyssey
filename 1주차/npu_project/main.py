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
            tokens = line.split()
            if len(tokens) != n :
                print(f"{n}개의 숫자를 공백으로 구분해 입력하세요")
                break
            try:
                rows.append([float(c) for c in tokens])
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
            m.set(r, c, float(arr[r][c])) # 실제 환경에는 소수점 쓰니 float)
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
    if abs(score_cross - score_x) < EPS: # 차이가 너무 작으f면 판정불가
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
    print("-"*20)
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
        with open("data.json", "r") as f: # json 열기
            data = json.load(f)
    except FileNotFoundError:
        print("data.json 파일이 없습니다")
        return

    print("-"*20)
    print("1. 필터 로드") # 필터 로드
    print("-"*20)
    filters = {} #{사이즈 : {'필터 이름': 매트릭스}}

    for size_key, label_dict in data['filters'].items(): # 사이즈별 필터
        size = int(size_key.split('_')[1]) # size_3 > 3
        filters[size] = {} # {3 : {'Cross': 매트릭스, 'X': 매트릭스}}
        for label, arr in label_dict.items(): # 라벨별 필터
            std = nomalize_label(label) # 라벨 정규화
            filters[size][std] = list_to_matrix(arr)
        print(f"{size}x{size} 필터 로드 완료 (cross, x )")
        
    print("-"*20)
    print("2. 패턴 분석 (라벨 정규화 적용)") # 패턴 분석
    print("-"*20)
    total = passed = failed = 0
    failed_list = []

    for key, item in data['patterns'].items(): # 패턴별 분석
        total += 1
        size = int(key.split('_')[1]) # size_5_ > 5
        pattern = list_to_matrix(item['input']) # 패턴 매트릭스
        expected = nomalize_label(item['expected']) # 라벨 정규화

        if size not in filters: # 필터가 없는 경우 / 크기 불일치
            failed += 1
            failed_list.append((f"{key} : 크기 불일치, 필터 없음"))
            print(f"{size}x{size} 필터 없음, 분석 불가")
            continue

        # MAC 수행
        score_cross = mac(pattern, filters[size]['Cross'])
        score_x = mac(pattern, filters[size]['X'])
        result = decide_label(score_cross, score_x)
        is_pass = (result == expected)

        print("-"*20) # 출력
        print(f"{key} 분석 결과")
        print(f"Cross score : {score_cross:.2f}, X score : {score_x:.2f}")
        status = "PASS" if is_pass else "FAIL"
        print(f"판정 : {result}, 예상 : {expected}, 결과 : {status}")

        if result == expected: # 집계
            passed += 1
        else:
            failed += 1
            reason = "Undecided" if result == "UNDECIDED" else "판정 불일치"
            failed_list.append((f"{key} : {reason}"))

    # 성능 분석
    print("-"*20)
    print("-"*20)
    print("3. 분석 결과 요약 (평균/10회)")
    print("-"*20)
    print(f"{'크기':<8}{'평균 시간(ms)':<16}{'연산 횟수'}")
    print("-"*20)

    for size in [3, 5, 13, 25]:
        if size in filters:
            mat = filters[size]['Cross']    # 실제 필터로 측정
        else:
            mat = Matrix(3)              # 3×3은 JSON에 없으니 더미
        t = measure(mat, mat)
        size_label = f"{size}×{size}"
        print(f"{size_label:<8}{t:<16.3f}{size*size}")

    # 결과 요약
    print("-"*20)
    print("# 4. 결과 요약")
    print("-"*20)
    print(f"총 테스트: {total}개")
    print(f"통과: {passed}개")
    print(f"실패: {failed}개")
    if failed_list:
        print("\n실패 케이스:")
        for item in failed_list:
            print(f"- {item}")

def main():
    print("--- mini npu simulator ---")
    print("\n -모드선택-")
    print("1. 사용자입력 (3x3)")
    print("2. data.json 분석")

    choice = int(input("선택 : ").strip())

    if choice == 1:
        run_mode_1()
    elif choice == 2:
        run_mode_2()
    else:
        print("1 또는 2를 입력하세요")

if __name__ == '__main__':
    main()