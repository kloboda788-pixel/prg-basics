###
# Translates words from English to Polish
#
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

# lower() and strip() - "Mouse " is treated the same as "mouse"
word = input('Enter a word in English: ').lower().strip()

# 'in' on a dictionary checks the keys
if word in translations:
    print(f'{word} -> {translations[word]}')
else:
    print(f'Translation of "{word}" is unavailable.')