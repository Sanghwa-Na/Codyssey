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

''' ----------------------------'''

# 보너스 문제 1차원 배열 최적화
def flatten(matrix_2d):
    # 2D 리스트 > 1D 리스트로 펼치기
    flat = []
    for row in matrix_2d:
        for val in row:
            flat.append(float(val))
    return flat

def mac_1d(flat_a, flat_b): # 패턴, 필터
    # 1차원 배열로 MAC 계산 (최적화 버전)
    total = 0.0
    for i in range(len(flat_a)):        # 인덱스 하나로 순회
        total += flat_a[i] * flat_b[i]
    return total

def compare_performance(matrix_2d, filter_2d, repeat=10000):
    # 최적화 전/후 비교

    print("성능 비교, 10000회 반복 측정")
    flat_m = flatten(matrix_2d)
    flat_f = flatten(filter_2d)

    # 2D 버전 측정
    start = time.perf_counter() # 시작 - 반복문 - 종료 시간
    for _ in range(repeat):
        mac(list_to_matrix(matrix_2d), list_to_matrix(filter_2d))
    time_2d = (time.perf_counter() - start) * 1000

    # 1D 버전 측정
    start = time.perf_counter() # 시작 - 반복문 - 종료 시간
    for _ in range(repeat):
        mac_1d(flat_m, flat_f)
    time_1d = (time.perf_counter() - start) * 1000

    # 결과 출력
    print(f"2D 방식: {time_2d:.3f} ms")
    print(f"1D 방식: {time_1d:.3f} ms")
    if time_1d > 0: # 제로 디비전 방지
        print(f"속도 향상: {time_2d / time_1d:.2f}배")
    return time_2d, time_1d


# 보너스 문제 패턴 생성기

def make_cross(n):
    # N×N 십자가 패턴 생성
    center = n // 2                    # 가운데 인덱스
    pattern = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == center or j == center:  # 중앙 행 or 중앙 열
                row.append(1)
            else:
                row.append(0)
        pattern.append(row)
    return pattern

def make_x(n):
    # N×N X 패턴 생성
    pattern = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j or i + j == n - 1:   # 두 대각선
                row.append(1)
            else:
                row.append(0)
        pattern.append(row)
    return pattern

def print_pattern(pattern):
    for row in pattern:
        print(' '.join('@' if v == 1 else '·' for v in row))

def run_bonus():
    print("\n" + "="*44)
    print(" 보너스 과제 실행")
    print("="*44)

    # 크기 입력 (안전하게)
    try:
        n = int(input("패턴 크기 N을 입력하세요 (예: 5): "))
        if n < 1:
            print("오류: N은 1 이상이어야 합니다.")
            return
    except ValueError:
        print("오류: 숫자를 입력하세요.")
        return

    print("\n#" + "-"*40)
    print(f"# {n}×{n} 패턴 생성") # 패턴 생성
    print("#" + "-"*40)

    cross = make_cross(n)
    x = make_x(n)

    print(f"\n=== {n}×{n} Cross ===")
    print_pattern(cross)
    print(f"\n=== {n}×{n} X ===")
    print_pattern(x)

    print("\n#" + "-"*40)
    print("# 2 생성 패턴으로 판정 테스트")
    print("#" + "-"*40)

    # Cross 패턴을 Cross/X 필터로 각각 채점, 생성된 패턴 제대로 작동되나 확인
    cross_m = list_to_matrix(cross)
    x_m = list_to_matrix(x)

    sc = mac(cross_m, cross_m)   # Cross vs Cross → 최고점
    sx = mac(cross_m, x_m)       # Cross vs X
    print(f"[Cross 입력] Cross 점수: {sc} | X 점수: {sx}")
    print(f"판정 결과: {decide_label(sc, sx)}")

    sc2 = mac(x_m, cross_m)
    sx2 = mac(x_m, x_m)          # X vs X → 최고점
    print(f"[X 입력]     Cross 점수: {sc2} | X 점수: {sx2}")
    print(f"판정 결과: {decide_label(sc2, sx2)}")

    # 1D 최적화 성능 비교 
    compare_performance(cross, cross, repeat=10000)

def main():
    print("--- mini npu simulator ---")
    print("\n -모드선택-")
    print("1. 사용자입력 (3x3)")
    print("2. data.json 분석")
    print("3. 보너스 문제: 패턴 생성기")

    choice = int(input("선택 : ").strip())

    if choice == 1:
        run_mode_1()
    elif choice == 2:
        run_mode_2()
    elif choice == 3:
        run_bonus()
    else:
        print("1 또는 2, 3을 입력하세요")

if __name__ == '__main__':
    main()