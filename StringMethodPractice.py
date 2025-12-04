import re
from re import split


# split
text = 'I love data science'
text.split()
line = 'Ali;34;27.3;True;Istanbul'
line.split(';')


# maxsplit en fazla 2 kere böler, 3 parça oluşturur.
sentence = "name: Ali age: 34 city: Istanbul"
sentence.split(' ', maxsplit=2)


#splitlines Satırlara bölmek:
text = "Ali\nAyşe\nMehmet"
text.splitlines()

# join ile tersini yapmak
# Split → string → liste
# Join → liste → string
words = ["data", "science", "is", "fun"]
' '.join(words)

fields = ["Ali", "34", "27.3", "True", "Istanbul"]
';'.join(fields)

# strip temizleme
# strip 2 tarafinida temizler
# lstrip left
# rstrip right

s = "   Ali  \n"
s.strip()
s.rstrip()
s.lstrip()

# lower hepsini kucultme

s = "I LOVE Data Science"
s.lower()

# replace
s = "I love Data-Science!"
s.replace('-',' ')

# startswith - endswith

s = "Machine learning is fun"
s.startswith('machine') #false
s.startswith('Machine') #true

s.endswith('fun') # true

s = "data_science.csv"
# birden fazla olasılık verebilirsin (tuple)
print(s.endswith(".csv"))                 # True
print(s.endswith((".csv", ".txt")))      # True (çünkü .csv ile bitiyor)
print(s.startswith(("data", "info")))

# find ve index
s = "I love data science"
s.find('data') # => 7 0dan baslar saymaya
s.index('data') # 7
# find: Bulamazsa -1 döner
# index: Bulamazsa hata fırlatır (ValueError)

s1 = "12345"
s2 = "abc"
s3 = "abc123"
s4 = "123a"
s5 = " 123"
s6 = "³"   # üst simge gibi şeyler

print(s1.isdigit())   # True
print(s2.isalpha())   # True
print(s3.isalnum())   # True (harf + sayı, ama boşluk yok)

print(s4.isdigit())   # False (çünkü içinde 'a' var)
print(s5.isdigit())   # False (başında boşluk var)
print(s3.isdigit())   # False (çünkü harf/sayı karışık)

print(" ".isdigit())  # False


# re.search(pattern, string)
# Verilen pattern’e u yan ilk eşleşmeyi bulur.
# Bulursa bir Match objesi döner, bulamazsa None.
text = "My ID is 12345."
pattern = r'\d+' # \d+ 1 veya daha fazla raka
match = re.search(pattern,text)
if match:
    print(f"bulunan sayi {match.group()}")
    print(f"baslangic indexi: {match.start()}")
    print(f'bitis indexi : {match.end()}')

# findall
# Verilen pattern’e uyan tüm eşleşmeleri bir liste halinde verir.

text = 'benim numara 123, 456, 789'
pattern  = r'\d+'
match = re.findall(pattern, text)
print(match)
for m in match:
    print(m)


#re metodu ile Text içindeki tüm kelimeleri çekmek
# split()
text = "I love data science, especially machine learning!"
words = text.lower().replace(",", "").replace("!", "").split()
print(words)
pattern = r'[a-zA-Z]+'
words = re.findall(pattern,text)


#%%
# Görev 1 – Cümleyi kelimelere böl

sentence = "Machine learning is a subfield of artificial intelligence"
# Kelime sayısını yazdır.
# Her kelimeyi tek tek satır satır yazdır.
words = sentence.split()
print(f"Kelime sayisi {len(words)}")
for w in words:
    print(w)

# Görev 2 – Hasta satırını parçala
line = "Ali,34,27.3,True,Istanbul"
# Sonra şu dict’i oluştur:
words = line.split(',')
patient = {
    "name": words[0],
    "age": words[1],
    "bmi": words[2],
    "smoker": words[3],
    "city": words[4]
}
patient
# Görev 3 – Temizle + split
raw = "   Ayşe;29;22.1;False;Ankara   \n"
# Önce strip() ile baş/son boşlukları ve \n’i temizle.
# Sonra split(";") ile ayır.
# name, age, bmi, smoker, city değişkenlerine sırayla ata.
# Ekrana düzgün bir formatta yaz:

new_raw = raw.strip().split(';')
p1 = {
    "name": new_raw[0],
    "age": new_raw[1],
    "bmi": new_raw[2],
    "smoker": new_raw[3],
    "city": new_raw[4]
}
print(f"Hastanin adi {p1['name']} yasi {p1['age']} bmi si {p1['bmi']} smoker mi {p1['smoker']} yasadigi sehir {p1['city']}")

# Görev 4 – join ile cümle oluştur
words = ["data", "cleaning", "is", "important", "for", "machine", "learning"]
' '.join(words)

# Görev 5 – Basit tokenizer
text = "I love Data Science, especially machine learning & deep learning!"
# Hepsini küçük harfe çevir (lower()).
# Noktalama işaretlerini temizle (virgül, ünlem, & yerine boşluk koymak için replace kullanabilirsin).
# Sonra split() ile kelimelere böl.
# Sonuçtaki kelime listesini yazdır.

fmt_Text = re.findall(r'[a-zA-Z]+', text.lower())
fmt_Text

#%%
# Bunları ayrı bir dosyada deneyebilirsin:
# 🧪 Görev 6 – “key: value” formatını parse et
line = "name: Ali | age: 34 | city: Istanbul | smoker: True"
# Yapman gereken:
# Önce ' | ' ile split et → parçalar: "name: Ali", "age: 34" vs.
# Her parçayı ": " ile tekrar split et → key, value al.
# Sonunda şöyle bir dict oluştur:
# {
#   "name": "Ali",
#   "age": 34,
#   "city": "Istanbul",
#   "smoker": True
# }
new_line = line.split(' | ')
dict_word = {}
for n in new_line:
    # k = n.split(': ')
    # dict_word[k[0]] = k[1]
    key,value = n.split(': ')
    dict_word[key] = value
dict_word

# Görev 7
# İstersen şimdi bir level daha atalım:
# Aynı formatta birden fazla satır olduğunu düşünelim:
lines = [
    "name: Ali | age: 34 | city: Istanbul | smoker: True",
    "name: Ayşe | age: 29 | city: Ankara | smoker: False",
]
# 👉 Bunları dolaşıp her satırı dict’e çevirip bir listeye atmayı dene:


# Burada da age → int, smoker → bool yaparsan süper.
# 🧪 Görev 8 – Basit log satırı ayrıştırma
# log = "[2025-12-05 19:45:12] INFO User 'emre' logged in from 192.168.1.10"
# Tarih-zaman kısmını ([ ... ] içini) çıkar.
# Log level’i al (INFO).
# Kullanıcı adını al (emre).
# IP adresini al (192.168.1.10).
# Sadece split, strip, replace ile yapmayı dene (regex gerekmez, sonra istersen regex versiyonu da bakarız).