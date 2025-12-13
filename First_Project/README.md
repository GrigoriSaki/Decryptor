# PolishDecryptor

Prosty skrypt w Pythonie do odszyfrowania tekstu szyfrem Cezara, wyboru najbardziej prawdopodobnego zdania po polsku przy użyciu Detect Language API oraz wyciągania adresu e-mail.

## Wymagania

- Python 3.10+
- Biblioteka: `detectlanguage`
- Klucz API do [Detect Language](https://detectlanguage.com/)

## Instalacja

1. Sklonuj repo: https://github.com/GrigoriSaki/Decryptor.git
2. Zainstaluj: pip install detectlanguage
3. Ustaw klucz API o nazwie: "DETECTLANG_API_KEY" w zmiennej środowiskowej lub pliku .env