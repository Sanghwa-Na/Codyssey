class QuizGame:
    def __init__(self):
        self.quizzes = [] # 퀴즈 목록
        self.score = 0 # 점수
        self.load_quizzes() # 퀴즈 불러오기 quizzes.json
        self.load_score() # 점수 불러오기 state.json
    
    def get_default_quizzes(self): # 기본 퀴즈 목록
        return [
            {
                "question": "영화 '기생충'의 감독은?",
                "choices": ["박찬욱", "봉준호", "김기덕", "이창동"],
                "answer": 2
            },
            {
                "question": "마블에서 타노스가 모은 인피니티 스톤 개수는?",
                "choices": ["4개", "5개", "6개", "7개"],
                "answer": 3
            },
            {
                "question": "영화 '인터스텔라'의 감독은?",
                "choices": ["놀란", "스필버그", "제임스 카메론", "리들리 스콧"],
                "answer": 1
            },
            {
                "question": "애니메이션 '토이스토리'를 만든 회사는?",
                "choices": ["디즈니", "픽사", "드림웍스", "지브리"],
                "answer": 2
            },
            {
                "question": "영화 '아바타'의 배경 행성 이름은?",
                "choices": ["판도라", "타투인", "크립톤", "아스가르드"],
                "answer": 1
            }
        ]

    def show_menu(self): # 메뉴 출력
        print("\n" + "=" * 40)
        print("        QUIZ GAME        ")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def play_quiz(self): # 퀴즈 풀기
        print("퀴즈를 풀어보세요!")
    
    def add_quiz(self): # 퀴즈 추가
        print("퀴즈를 추가하세요!")

    def list_quizzes(self): # 퀴즈 목록
        print("퀴즈 목록을 확인하세요!")

    def check_score(self): # 점수 확인
        print("점수를 확인하세요!")
    
    def save_score(self): # 점수 저장
        print("점수를 저장하세요!") 
    
    def run(self): # 게임 실행
        while True:
            self.show_menu()
            choice = input("메뉴를 선택하세요 (1-5): ").strip()
            if not choice.isdigit() or int(choice) < 1 or int(choice) > 5:
                print("잘못된 입력입니다. 다시 선택해주세요.")
                continue 

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.list_quizzes()
            elif choice == "4":
                self.check_score()
            elif choice == "5":
                print("게임을 종료합니다.")
                # self.save_file()
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")
            
    