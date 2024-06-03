import argparse
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    # Створення парсера
    parser = argparse.ArgumentParser(description='Print the provided text.')
    # Додавання аргументу
    parser.add_argument('text', type=str, help='Text to be printed')
    # Парсинг аргументів
    args = parser.parse_args()

    text_from_env = os.environ.get('TEST_TEXT')

    # Вивід тексту в консоль
    print(f'Provided text: {args.text}')
    print(f'Text from .env file: {text_from_env}')

if __name__ == '__main__':
    main()
