from deep_translator import GoogleTranslator

text = input("Enter text: ")
source = input("From language (e.g. en): ")
target = input("To language (e.g. hi): ")

translation = GoogleTranslator(
    source=source,
    target=target

)
translate(text)

print("Translation:", translation)