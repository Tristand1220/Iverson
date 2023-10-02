import json
from difflib import get_close_matches


def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:  # 'r' = read mode
        data: dict = json.load(file)
    return data


def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:  # 'w' = read mode
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1,
                                      cutoff=0.6)  # 'n' chooses the best answer, "cutoff" is an accuracy measure
    return matches[0] if matches else None


def get_answer(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q in ["question"] == question:
            return q["answer"]


def iverson():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input('You :')

        if user_input.lower == 'quit':
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer(best_match, knowledge_base)
            print(f'Iverson: {answer}')
        else:
            print('Iverson: I don\'t have all the answers. Can you teach me?')
            new_answer: str = input('Type answer or "skip" to skip: ')

            if new_answer.lower != 'skip':
                knowledge_base["questions"].append({"questions": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Iverson: Thank you but we\'re talking about practice... ')


if __name__ == '__main__':
    iverson()