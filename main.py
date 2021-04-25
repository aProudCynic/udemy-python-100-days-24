INPUT_FOLDER = 'Input'

def create_letter_content_for(name: str):
    with open(f'{INPUT_FOLDER}/Letters/starting_letter.txt', 'r') as template_letter:
        letter_content = template_letter.read()
    return letter_content.replace('[name]', name)

def save_letter_file(name: str, letter_content: str):
    with open(f'Output/ReadyToSend/LetterTo{name}.txt', 'w') as letter_file:
        letter_file.write(letter_content)

def create_letter_for(name: str):
    letter_content = create_letter_content_for(name)
    save_letter_file(name, letter_content)

with open(f'{INPUT_FOLDER}/Names/invited_names.txt', 'r') as invited_names:
    names = invited_names.readlines()
for name in names:
    cleaned_name = name.strip()
    create_letter_for(cleaned_name)
