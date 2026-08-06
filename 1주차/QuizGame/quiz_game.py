import Quiz, json, os

quiz_file = "quizzes.json"
state_file = "state.json"


class QuizGame:
    def __init__(self):
        self.quizzes = []  # 퀴즈 목록
        self.best_score = 0  # 점수

        self.load_quizzes()  # 퀴즈 불러오기 quizzes.json
        self.load_state()  # 점수 불러오기 state.json
    
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

    def get_input(self, prompt): # 입력 시 오류 처리하기위해 
        try:
            return input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되었습니다. 게임을 종료합니다.")
            return None

    def save_quizzes(self):
        try:
            with open(quiz_file, 'w', encoding='utf-8') as f:
                json.dump([quiz.__dict__ for quiz in self.quizzes], f, ensure_ascii=False, indent=4)
            print("퀴즈가 저장되었습니다.")
        except Exception as e:
            print(f"퀴즈 저장 중 오류 발생: {e}")   

    def load_quizzes(self):
        if not os.path.exists(quiz_file):
            self.quizzes = [Quiz.Quiz(**q) for q in self.get_default_quizzes()]
            self.save_quizzes()
            return
        try:
            with open(quiz_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if isinstance(data, list):
                self.quizzes = [Quiz.Quiz(**q) for q in data]
            else:
                # 파일은 존재하지만 예상 형식이 아닌 경우
                raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")
        except Exception as e:
            # 파일이 비어있거나 JSON 파싱 실패 등 손상된 경우
            print(f"퀴즈 로드 중 오류 발생: {e}")
            print("퀴즈 파일이 손상되었거나 형식이 잘못되었습니다. 기본 퀴즈로 복구합니다.")
            # 기본 퀴즈로 복원하고 저장
            self.quizzes = [Quiz.Quiz(**q) for q in self.get_default_quizzes()]
            try:
                self.save_quizzes()
            except Exception as save_e:
                print(f"기본 퀴즈 저장 중 오류 발생: {save_e}")

    def save_state(self):
        try:
            with open(state_file, 'w', encoding='utf-8') as f:
                json.dump({"score": self.best_score}, f, ensure_ascii=False, indent=4)
            print("점수가 저장되었습니다.")
            print(f"현재 점수: {self.best_score}")
        except Exception as e:
            print(f"점수 저장 중 오류 발생: {e}")

    def load_state(self):
        if not os.path.exists(state_file):
            self.best_score = 0
            return  
        try:
            with open(state_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if isinstance(data, dict) and 'score' in data:
                self.best_score = data['score']
            else:
                raise ValueError("상태 데이터 형식이 올바르지 않습니다.")
        except Exception as e:
            print(f"상태 로드 중 오류 발생: {e}")
            print("상태 파일이 손상되었거나 형식이 잘못되었습니다. 점수를 초기화합니다.")
            self.best_score = 0
            try:
                self.save_state()
            except Exception as save_e:
                print(f"점수 초기화 저장 중 오류 발생: {save_e}")

    def play_quiz(self):  # 퀴즈 풀기
        print("퀴즈를 풀어보세요!")

        score = 0

        if not self.quizzes:
            print("퀴즈가 없습니다. 퀴즈를 추가해주세요.")
            return

        total_quizzes = len(self.quizzes)
        print("-" * 40)
        print(f"총 {total_quizzes}개의 퀴즈가 있습니다.")
        print("-" * 40)
        print(f"BEST SCORE : {self.best_score}")
        print("-" * 40)

        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"\n문제 {i}: {quiz.question}")
            for j, choice in enumerate(quiz.choices, start=1):
                print(f"{j}. {choice}")

            while True:
                answer = self.get_input("정답 번호를 입력하세요 (1-4): ")
                if answer is None:
                    return
                if answer.isdigit() and 1 <= int(answer) <= 4:
                    answer = int(answer)
                    break
                else:
                    print("잘못된 입력입니다. 1에서 4 사이의 숫자를 입력해주세요.")

            if answer == quiz.answer:
                print("정답입니다!")
                score += 1
            else:
                print(f"틀렸습니다! 정답은 {quiz.answer}번입니다.")

        if score > self.best_score:
            self.best_score = score
            self.save_state()
            print(f"\n축하합니다! 새로운 최고 점수 {self.best_score}점을 기록했습니다!")
        else:
            print(f"\n이번 점수: {score}점. 최고 점수: {self.best_score}점.")   

    def add_quiz(self):  # 퀴즈 추가
        print("퀴즈를 추가하세요!")

        question = self.get_input("문제를 입력하세요: ")
        if question is None:
            return

        choices = []

        for i in range(4):
            choice = self.get_input(f"선택지 {i+1}를 입력하세요: ")
            if choice is None:
                return
            choices.append(choice)

        while True:
            answer = self.get_input("정답 번호 (1-4)를 입력하세요: ")
            if answer is None:
                return
            if answer.isdigit() and 1 <= int(answer) <= 4:
                answer = int(answer)
                break
            else:
                print("잘못된 입력입니다. 1에서 4 사이의 숫자를 입력해주세요.")

        new_quiz = Quiz.Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_quizzes()  # 퀴즈 저장
        print("퀴즈가 추가되었습니다.")  

    def list_quizzes(self): # 퀴즈 목록
        if not self.quizzes:
            print("퀴즈가 없습니다. 퀴즈를 추가해주세요.")
            return
        
        print("=" * 40)
        print("퀴즈 목록을 확인하세요!")
        print("=" * 40)
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")
            
    def check_score(self): # 점수 확인
        print("점수를 확인하세요!")
        print
        print(f"현재 최고 점수: {self.best_score}점")
    
    def run(self): # 게임 실행
        while True:
            self.show_menu()
            choice = self.get_input("메뉴를 선택하세요 (1-5): ")
            if choice is None:
                break
            if not choice.isdigit() or int(choice) < 1 or int(choice) > 5:
                print("잘못된 입력입니다. 다시 선택해주세요.")
                continue 

            if choice == "1": # 풀기
                self.play_quiz()
            elif choice == "2": # 추가
                self.add_quiz()
            elif choice == "3": # 목록
                self.list_quizzes()
            elif choice == "4": # 확인
                self.check_score()
            elif choice == "5": # 종료
                print("게임을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")
            
    