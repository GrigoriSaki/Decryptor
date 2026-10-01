import detectlanguage
import re
import os

api_key = os.getenv("DETECTLANG_API_KEY")
 
if not api_key:
    raise ValueError("Nie ustawiono klucza API w zmiennej środowiskowej")

detectlanguage.configuration.api_key = api_key

def decrypt (message, key):
     decrypted=""
     for letter in message:
            if 'a' <= letter <= 'z':
                
                if ord(letter) - key < ord('a'):
                 decrypted += chr(ord(letter) - key + 26)
                else:
                 decrypted += chr(ord(letter) - key)
            elif 'A' <= letter <= 'Z':

                if ord(letter) - key < ord('A'):
                 decrypted += chr(ord(letter) - key + 26)
                else:
                 decrypted += chr(ord(letter) - key)
            else: 
               decrypted += letter           
     return decrypted

message = "epomj ezno yudndve. nuopxuiv diozgdbzixev rkgtrv iv ivnuV xjyudzijnx. vwt fjiotipjrvx rturvidz, rtngde fjy uvyvidv iv: epomj.ezno.yudndve@vyzkxd.do"
best_confidence = None
best_decryption = None
sentence =""
results = []

for i in range(1,26):
   sentence = decrypt(message,i) 
   print(sentence)
   
   results = detectlanguage.detect(sentence)
   if not results:
        continue
   
   if results[0]['language'] == "pl" and (best_confidence is None or results[0]['score'] > best_confidence):
           best_confidence = results[0]['score']
           best_decryption = sentence

if best_decryption is None:
    print("Nie znaleziono polskiego tekstu. Sprawdź wiadomość lub spróbuj innego tekstu.")
    raise SystemExit(1)

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, best_decryption)

print("\n\nBest decryption:")
print(best_decryption)
print("\nExtracted email addresses:")
for email in emails:
    print(email)