from quiz_game import QuizGame

def main():
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되었습니다. 게임을 종료합니다.")

if __name__ == "__main__":
    main()