# Игра Камень,ножници, бумага

import random

# Определяем возможные варианты выбора
choices = ["камень", "ножницы", "бумага"]

# Функция для выбора случайного варианта
def get_computer_choice():
    return random.choice(choices)

# Функция для проверки выигрыша
def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Ничья"
    elif player_choice == "камень" and computer_choice == "ножницы":
        return "Игрок выиграл"
    elif player_choice == "ножницы" and computer_choice == "бумага":
        return "Игрок выиграл"
    elif player_choice == "бумага" and computer_choice == "камень":
        return "Игрок выиграл"
    else:
        return "Компьютер выиграл"

# Основная функция игры
def play_game():
    player_wins = 0
    computer_wins = 0

    while player_wins < 5 and computer_wins < 5:
        # Запрос на выбор игрока
        player_choice = input("Введите ваш выбор (Камень, Ножницы, Бумага): ").lower()
        if player_choice not in ['камень', 'ножницы', 'бумага']:
            print("Неверный выбор. Попробуйте еще раз.")
            continue

        # Выбор компьютера
        computer_choice = get_computer_choice()

        # Проверка и вывод результата
        result = check_winner(player_choice, computer_choice)
        print(f"Ваш выбор: {player_choice.capitalize()}")
        print(f"Компьютер выбрал: {computer_choice.capitalize()}")
        print(f"Результат: {result}")

        if result == "Игрок выиграл":
            player_wins += 1
        elif result == "Компьютер выиграл":
            computer_wins += 1

    # Вывод результата игры
    if player_wins == 5:
        print("ПОБЕДА ИГРОКА!")
    elif computer_wins == 5:
        print("УВЫ ВЫ ПРОИГРАЛИ(((")
    else:
        print("Игра окончена. Ничья.")

# Запуск игры
play_game()
