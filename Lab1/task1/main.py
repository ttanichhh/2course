from models import RubiksCube


def main():
    cube = RubiksCube()

    while True:
        print("\n" + "=" * 40)
        print("        КУБИК РУБИКА")
        print("=" * 40)
        print("1. Показать кубик")
        print("2. Повернуть переднюю грань по часовой")
        print("3. Повернуть переднюю грань против часовой")
        print("4. Повернуть правую грань по часовой")
        print("5. Повернуть правую грань против часовой")
        print("6. Повернуть левую грань по часовой")
        print("7. Повернуть левую грань против часовой")
        print("8. Повернуть верхнюю грань по часовой")
        print("9. Повернуть верхнюю грань против часовой")
        print("10. Повернуть нижнюю грань по часовой")
        print("11. Повернуть нижнюю грань против часовой")
        print("12. Повернуть заднюю грань по часовой")
        print("13. Повернуть заднюю грань против часовой")
        print("14. Перемешать кубик")
        print("15. Проверить, решено ли")
        print("16. Вернуть на свои места")
        print("0. ВЫЙТИ")
        print("=" * 40)

        try:
            choice = int(input("Выберите опцию: "))
        except ValueError:
            print("Пожалуйста, введите число!")
            continue

        if choice == 0:
            print("До свидания!")
            break
        elif choice == 1:
            cube.display()
        elif choice == 2:
            cube.rotate_front_clockwise()
            print("Передняя грань повернута по часовой стрелке")
        elif choice == 3:
            cube.rotate_front_counter_clockwise()
            print("Передняя грань повернута против часовой стрелки")
        elif choice == 4:
            cube.rotate_right_clockwise()
            print("Правая грань повернута по часовой стрелке")
        elif choice == 5:
            cube.rotate_right_counter_clockwise()
            print("Правая грань повернута против часовой стрелки")
        elif choice == 6:
            cube.rotate_left_clockwise()
            print("Левая грань повернута по часовой стрелке")
        elif choice == 7:
            cube.rotate_left_counter_clockwise()
            print("Левая грань повернута против часовой стрелки")
        elif choice == 8:
            cube.rotate_up_clockwise()
            print("Верхняя грань повернута по часовой стрелке")
        elif choice == 9:
            cube.rotate_up_counter_clockwise()
            print("Верхняя грань повернута против часовой стрелки")
        elif choice == 10:
            cube.rotate_down_clockwise()
            print("Нижняя грань повернута по часовой стрелке")
        elif choice == 11:
            cube.rotate_down_counter_clockwise()
            print("Нижняя грань повернута против часовой стрелки")
        elif choice == 12:
            cube.rotate_back_clockwise()
            print("Задняя грань повернута по часовой стрелке")
        elif choice == 13:
            cube.rotate_back_counter_clockwise()
            print("Задняя грань повернута против часовой стрелки")
        elif choice == 14:
            moves = input("Сколько перемешиваний? (по умолчанию 20): ")
            moves = int(moves) if moves.isdigit() else 20
            cube.scramble(moves)
            print(f"Кубик перемешан ({moves} движений)")
        elif choice == 15:
            if cube.is_solved():
                print("Кубик решен! 🎉")
            else:
                print("Кубик не решен")
        elif choice == 16:
            cube.initialize()
            print("Кубик возвращен в начальное состояние")
        else:
            print("Неверная опция!")


if __name__ == "__main__":
    main()