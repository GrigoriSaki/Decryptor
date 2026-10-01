Skrypt w Pythonie, który łamie szyfr Cezara metodą brute force, sam wybiera poprawne polskie zdanie i wyciąga z niego adres e-mail.

Projekt powstał jako rozwiązanie zadania konkursowego: w zaszyfrowanej wiadomości ukryty był adres e-mail, który trzeba było odnaleźć.

Jak to działa
Skrypt próbuje wszystkich 25 możliwych przesunięć szyfru Cezara.
Każdy z 25 wyników jest wysyłany do Detect Language API.
Spośród wyników rozpoznanych jako polski wybierany jest ten z najwyższym współczynnikiem pewności.
Z wybranego tekstu wyrażenie regularne wyciąga adresy e-mail.

Wielkość liter jest zachowana, a znaki spoza alfabetu łacińskiego (spacje, cyfry, interpunkcja) pozostają bez zmian.

Przykład

Wejście:

epomj ezno yudndve. nuopxuiv diozgdbzixev rkgtrv iv ivnuV xjyudzijnx. vwt fjiotipjrvx rturvidz, rtngde fjy uvyvidv iv: epomj.ezno.yudndve@vyzkxd.do

Wyjście (skrócone):

(...wyniki dla pozostałych przesunięć...)

Best decryption:
jutro jest dzisiaj. sztuczna inteligencja wplywa na naszA codzienosc. aby kontynuowac wyzwanie, wyslij kod zadania na: jutro.jest.dzisiaj@adepci.it

Extracted email addresses:
jutro.jest.dzisiaj@adepci.it

W tym przykładzie poprawne przesunięcie to 21.

Wymagania
Python 3.10 lub nowszy
Biblioteka detectlanguage
Darmowy klucz API z detectlanguage.com
Połączenie z internetem
Instalacja
bash
git clone https://github.com/GrigoriSaki/Decryptor.git
cd Decryptor
pip install -r requirements.txt
Konfiguracja

Klucz API jest odczytywany ze zmiennej środowiskowej DETECTLANG_API_KEY. Nie jest zapisany w kodzie.

Windows (PowerShell):

powershell
$env:DETECTLANG_API_KEY = "twoj_klucz"

Jeśli zmienna nie jest ustawiona, skrypt kończy działanie z czytelnym komunikatem błędu.

Uruchomienie

Tekst do odszyfrowania ustawiasz w zmiennej message w pliku decryptor.py, a następnie:

bash
python decryptor.py

Ograniczenia
Obsługiwany jest wyłącznie alfabet łaciński (a-z, A-Z). Polskie znaki diakrytyczne (ą, ę, ż itd.) nie są przesuwane.
Wybór poprawnego wyniku zależy od trafności wykrywania języka. Bardzo krótkie teksty mogą być rozpoznane błędnie.
Skrypt wysyła 25 zapytań do API na jedno odszyfrowanie, więc działa wolniej i zużywa limit darmowego konta.