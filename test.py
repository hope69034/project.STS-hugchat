from translate import Translator

def translate_english_to_korean(text):
    translator = Translator(to_lang='ko', from_lang='en')
    translation = translator.translate(text)
    return translation

# Example usage
english_text = "Hello, how are you?"
korean_translation = translate_english_to_korean(english_text)
print(korean_translation)
