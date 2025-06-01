def ask_for_form() -> list[str]:
    """
    Fragt den Benutzer nach Fragen für ein Formular und gibt eine Liste der Fragen zurück.
    """

    questions: list[str] = []

    while True:
        question = input("Gib eine Frage ein (oder 'fertig' zum Beenden): ")
        if question.lower() == "fertig":
            break
        questions.append(question)

    return questions


def run():
    print("Hello, Formular Assistant!")

    questions = ask_for_form()
    print(questions)
