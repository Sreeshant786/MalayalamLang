
def translate_code(code, keywords):

    translated = code

    for key, value in keywords.items():

        translated = translated.replace(
            key,
            value
        )

    return translated