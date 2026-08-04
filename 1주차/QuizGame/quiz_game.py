class QuizGame:

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
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")
            
    