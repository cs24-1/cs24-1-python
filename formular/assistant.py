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


def create_form(questions: list[str], filename: str = "form.txt") -> None:
    """
    Erstellt ein Formular basierend auf den gegebenen Fragen und speichert es in einer Datei.

    Jede Frage wird in einer neuen Zeile geschrieben, gefolgt von einem Doppelpunkt und einem Leerzeichen, um Platz für Antworten zu lassen.

    Args:
        questions (list[str]): Eine Liste von Fragen, die im Formular enthalten sein sollen.
        filename (str, optional): Der Name der Datei, in die das Formular geschrieben werden soll. Standardmäßig "form.txt".

    Returns:
        None
    """

    with open(filename, "w") as file:
        for question in questions:
            file.write(f"{question} : \n")


def read_form(filename: str = "form.txt") -> dict[str, str]:
    """
    Liest ein Formular aus einer Datei und gibt die Fragen und Antworten als Dictionary zurück.

    Args:
        filename (str, optional): Der Name der Datei, aus der das Formular gelesen werden soll. Standardmäßig "form.txt".

    Returns:
        dict[str, str]: Ein Dictionary, in dem die Fragen als Schlüssel und die Antworten als Werte gespeichert sind.
    """

    answers: dict[str, str] = dict()

    with open(filename, "r") as file:
        for line in file.readlines():
            question, answer = line.strip().split(" : ")[0:2]
            answers[question] = answer

    return answers


def run():
    print("Hello, Formular Assistant!")

    #questions = ask_for_form()
    #create_form(questions)
    #print("Formular erstellt.")

    answers = read_form()
    print("Formular gelesen:")
    print(answers)
