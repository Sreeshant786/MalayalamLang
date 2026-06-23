from keywords import KEYWORDS

def translate_code(code):

    translated = code

    for malayalam_word, python_word in KEYWORDS.items():
        translated = translated.replace(
            malayalam_word,
            python_word
        )

    return translated