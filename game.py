import json
import random
import os
import time


def initialize_game():
    """
    Initialize the game by printing the welcome message and the instructions.
    """
    print(
        "\033[1m\033[34m\n\n"
        + "W E L C O M E . T O . T H E . B E S T . E - B O A R D G A M E . E V E R"
        + "\033[0m"
    )
    print(
        "1. Choose a category from the list.\n"
        + "2. A random question will be displayed.\n"
        + "3. If you want to play again, type 'yes'.\n"
        + "4. If you want to exit, type 'no'.\n"
    )
    input("\nPress ENTER to start the game...")
    os.system("cls")
    return None


def read_questions(json_file: str) -> dict:
    """
    Read the questions from the json file and return them as a dictionary.

    Args:
        json_file (str): The path to the json file.

    Returns:
        data (dict): The questions as a dictionary
    """
    with open(json_file) as f:
        data = json.load(f)
    return data


def ask_category(data: dict) -> str:
    """
    Ask the user to choose a category from the list of categories.

    Args:
        data (dict): The questions as a dictionary

    Returns:
        category (str): The chosen category
    """
    categories = list(data.keys())

    print("\033[1m\n" + "CHOOSE A CATEGORY:" + "\033[0m")

    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")

    while True:
        choice = input("\033[1m\n" + "Enter the number of the category: " + "\033[0m")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(categories):
                os.system("cls")
                print(f"\nYou chose the category: {categories[choice-1]}")
                return categories[choice - 1]
            else:
                print(
                    "\033[91m"
                    + "Invalid number. Please enter a number from the list."
                    + "\033[0m"
                )
        else:
            print(
                "\033[91m" + "Invalid input. Please enter a valid number." + "\033[0m"
            )


def select_question(questions: list) -> list:
    """
    Select a random question from the list of questions and print it.
    Then remove the question from the list.

    Args:
        questions (list): The list of questions

    Returns:
        questions (list): The updated list of questions
    """
    number = random.randint(0, len(questions) - 1)
    question = questions[number]
    print("\033[1m\033[32m" + question + "\033[0m")
    questions.pop(number)
    return questions


def play_again():
    """
    Ask the user if they want to play again.

    Args:
        None

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    while True:
        answer = input("\nWould you like to play again? ")
        if answer.lower() == "yes":
            os.system("cls")
            return True
        elif answer.lower() == "no":
            os.system("cls")
            print("\033[1m\n" + "Thank you for playing. Goodbye!" + "\033[0m")
            time.sleep(2)
            os.system("cls")
            return False
        else:
            print("\033[91mInvalid input. Please enter 'yes' or 'no'.\033[0m")


def main():
    """
    The main function that runs the game.
    """
    initialize_game()
    data = read_questions("questions.json")

    while True:
        category = ask_category(data)
        questions = data[category]

        if not questions:
            print("\033[91m" + "No more questions in this category." + "\033[0m")
            continue
        data[category] = select_question(questions)

        if not play_again():
            break


if __name__ == "__main__":
    main()
