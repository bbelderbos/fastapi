from random import choice

from emoji import EMOJI_UNICODE
from pyperclip import copy

LANGUAGE = 'en'
QUIT = 'q'
RANDOM_MODE = True


def get_matching_emojis(words: list[str],
                        at_random: bool = RANDOM_MODE) -> list[str]:
    matches = []
    for word in words:
        emojis = get_emojis_for_word(word)
        if len(emojis) == 0:
            continue
        select_func = choice if at_random else select_emoji_interactively
        selected_emoji = emojis[0] if len(emojis) == 1 else select_func(emojis)
        matches.append(selected_emoji)
    return matches


def get_emojis_for_word(word: str, lang: str = LANGUAGE) -> list[str]:
    return [emo for name, emo in EMOJI_UNICODE[lang].items()
            if word in name]


def select_emoji_interactively(emojis: list[str]) -> str:
    while True:
        try:
            for i, emo in enumerate(emojis, start=1):
                print(i, emo)
            user_input = input("Select which emoji you want? ")
            idx = int(user_input)
            return emojis[idx - 1]
        except ValueError:
            print(f"{user_input} is not an integer: ")
            continue


def main():
    while True:
        user_input = input("Type one or more emoji related words (type 'q' for exit): ")
        user_input = user_input.lower()
        if user_input == QUIT:
            print('Bye')
            break

        words = user_input.split()
        matches = get_matching_emojis(words)

        all_matching_emojis = ' '.join(matches)
        print(f"Copying {all_matching_emojis} to clipboard")
        copy(all_matching_emojis)


if __name__ == "__main__":
    main()
