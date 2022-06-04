from os import path
from random import choice
import json
import requests


PATH_FILE = './words.json'
URL_FILE = 'https://www.randomlists.com/data/words.json'
WORDS = None


def check_word_file():
    if not path.exists(PATH_FILE) or path.getsize(PATH_FILE) < 22000:
        download_word_file()

def download_word_file():
    res = requests.get(URL_FILE)
    with open(PATH_FILE, 'wb') as file_words:
        file_words.write(res.content)

def load_words():
    global WORDS
    if not WORDS:
        with open(PATH_FILE, encoding='utf8') as file_words:
            WORDS = json.load(file_words)['data']

def get_random_word():
    return choice(WORDS)

def main():
    random_word_original = get_random_word()
    random_word = random_word_original.replace('-', '').replace(' ', '')
    valid_guess = ['-' for _ in random_word]
    word_guess_count = 0
    word_guess_max_count = 5 * len(random_word)
    
    while word_guess_count < word_guess_max_count and '-' in valid_guess:
        print('number of guesses left', word_guess_max_count - word_guess_count)        
        print(''.join(valid_guess))        
        char_guess = input('enter your char guess:')
        
        word_guess_count += 1
        
        if char_guess in random_word:
            for i in range(len(random_word)):
                if char_guess == random_word[i] and '-' == valid_guess[i]:
                    valid_guess[i] = char_guess
                    break

    if '-' not in valid_guess:    
        print('Congratulations you won' , random_word_original)
    else: 
        print('Game over!!! random word was', random_word_original)


check_word_file()
load_words()

MSG = 'if you want to play again press enter else enter ("quit", "q", "e", "exit"):'
while input(MSG) not in ('quit', 'q', 'e', 'exit'):
    main()
