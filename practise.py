#%%
patients = [
    {"id": 1, "name": "Ali",  "age": 34, "bmi": 27.3, "smoker": True,  "city": "Istanbul"},
    {"id": 2, "name": "Ayşe", "age": 29, "bmi": 22.1, "smoker": False, "city": "Ankara"},
    {"id": 3, "name": "Mehmet", "age": 41, "bmi": 31.4, "smoker": True,  "city": "Izmir"},
    {"id": 4, "name": "Elif", "age": 36, "bmi": 24.8, "smoker": False, "city": "Istanbul"},
    {"id": 5, "name": "Can",  "age": 50, "bmi": 29.9, "smoker": True,  "city": "Bursa"},
    {"id": 6, "name": "Zeynep", "age": 23, "bmi": 19.5, "smoker": False, "city": "Izmir"},
]

# 30 yaşından büyük ve sigara içen hastaların isimlerini yazdır.

for patient in patients:

    if (patient["smoker"] == True and patient["age"] > 30):
        print(f" The {patient.get('name')} is smoking")

# Tüm hastaların ortalama BMI değerini hesapla.

total_bmi = 0
count = 0
for patient in patients:
    bmi = patient.get("bmi")
    total_bmi += bmi
    count +=1

average_bmi = total_bmi/count
average_bmi

# BMI değeri 30’un üzerinde olanları “obez” kabul edip, obez hastaların id ve isimlerini yazdır.

for patient in patients:
    if(patient.get("bmi") >30):
        print(f"Obez Hasta: {patient.get('id')} - {patient.get('name')}")


# Görev 4 – Set:
# Tüm hastaların yaşadığı şehirlerin benzersiz listesini bul.
# Önce boş bir set oluştur
# Döngü ile tüm patient’ların city alanını ekle
# Sonra ekrana yazdır.
# Beklenen: mesela {'Istanbul', 'Ankara', 'Izmir', 'Bursa'} gibi bir şey.
city_dict = set()
for patient in patients:
    city_dict.add(patient.get("city"))
print(city_dict)


# Görev 5 – Tuple:
# Tüm hastaların (id, name) bilgisini içeren bir tuple listesi oluştur.
# Yani şöyle bir yapı elde etmek istiyoruz:
list = []

for patient in patients:
    pat = patient.get('id'),patient.get('name')
    print(pat)
    list.append(pat)


def calculate_average_bmi(patients_list):
    """
    patients_list: içinde hasta sözlükleri olan liste
    return: float (ortalama bmi)
    """
    # burada for döngüsü ile toplam bmi ve hasta sayısını hesapla
    # sonra ortalamayı return et
    total_bmi = 0
    count = 0
    for patient in patients_list:
        bmi = patient.get('bmi')
        total_bmi += bmi
        count +=1
    average = total_bmi/count
    return average

avg = calculate_average_bmi(patients)
print('ortalama bmi ',avg)

def safe_average_bmi(patients_list):
    """
    Hasta listesi boşsa veya hatalı veri varsa çökmemeli.
    Hata durumunda None döndürebilir veya ekrana uyarı yazabilirsin.
    """
    try:
        # burada yine ortalama bmi hesapla
        total_bmi = 0
        count = 0
        for patient in patients_list:
            bmi = patient.get('bmi')
            total_bmi += bmi
            count +=1
        avg_bmi = total_bmi/count
        return avg_bmi
        # fakat:
        # - liste boşsa ZeroDivisionError olabilir
        # - yanlış bir key yazarsan KeyError olabilir
        # try bloğunda normal işlemini yap

    except ZeroDivisionError:
        print("HATA: Hasta listesi boş, ortalama hesaplanamadı.")
        return None
    except KeyError:
        print("HATA: Bir hastada beklenen alan (bmi) eksik.")
        return None

result = safe_average_bmi(patients)
print("Güvenli ortalama BMI sonucu:", result)

class Patient:
    def __init__(self,id, name, age, bmi, smoker,city):
        self.id = id
        self.name = name
        self.age = age
        self.bmi = bmi
        self.smoker = smoker
        self.city = city

    def is_obese(self):
        if self.bmi > 30:
            return True
        else:
            return False

    def info(self):
        print(f"ID:{self.id} | Hastanin adi: {self.name}| Hastanin Yasi: {self.age}| Hasta sigara iciyor mu? {self.smoker}"
              f" Hastanin bmi'si: {self.bmi}| Hastanin sehri: {self.city}")

    def smoker_stats(patients_list):
        """
        return: {"smoker": sayı, "non_smoker": sayı}
        """
        smoke_list = {}
        smoke = 0
        non_smoke = 0
        for p in patients_list:
            if p['smoker']:
                smoke +=1
            else:
                non_smoke+=1
        smoke_list['smoke'] = smoke
        smoke_list['non_smoke'] = non_smoke
        return smoke_list

    def count_by_city(patients_list):
        """
        return: {"Istanbul": 2, "Ankara": 1, ...} gibi bir dict
        """
        count_cities = {}
        for p in patients_list:
            city = p['city']
            if city not in count_cities:
                count_cities[city] = 0
            count_cities[city] += 1
        return  count_cities

    def average_bmi_by_city(patients_list):
        """
        return: {"Istanbul": 26.05, "Ankara": 22.1, ...}
        """
        # average_bmi = total[city] / count[city]
        totals = {}
        counts= {}
        for p in patients_list:
            city = p['city']
            bmi = p['bmi']
            if city not in totals:
                totals[city] = 0
                counts[city] = 0
            totals[city] += bmi
            counts[city] +=1

        averages = {}
        for city in totals:
            averages[city] = totals[city] / counts[city]
        return averages

    # BMI > 30 +2puan
    # sigara iciyorsa +2 puan
    # yas > 45 ise +1 puan
    def risk_score(patient):
        """
        patient: tek bir hasta dict'i
        return: int (risk skoru)
        """
        smoker = patient['smoker']
        bmi = patient['bmi']
        age = patient['age']
        score = 0
        if smoker:
            score +=2
        if bmi > 30:
            score +=2
        if age > 45:
            score+=1
        return int(score)

patient_object = []

for p in patients:
    obj = Patient(p["id"],p["name"],p["age"],p["bmi"],p["smoker"],p["city"])
    patient_object.append(obj)

for obese in patient_object:
    if obese.is_obese()== True:
        obese.info()

Patient.smoker_stats(patients)
Patient.count_by_city(patients)
Patient.average_bmi_by_city(patients)

for p in patients:
    score = Patient.risk_score(p)
    print(p["name"], "=> risk skoru:", score)

