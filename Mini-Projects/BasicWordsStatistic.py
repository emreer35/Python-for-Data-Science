
#%%
import re
text = "Yapay zekâ (YZ) teknikleri hukuk alanında büyük bir potansiyele sahiptir. Hukukta yazılı metinler ağırlıklı olarak kullanıldığından, yapay zekâ tekniklerinin kullanımı hukuki metinlerin hızlı ve etkin bir şekilde işlenmesini sağlayarak karar verme süreçlerine yardımcı olabilir. Bunun yanında, yapay zekâ teknikleri hukuki süreçlerin iyileştirilmesinde ve davaların olası sonuçlarını tahmin etmede de kullanılabilir. Bu çalışmada, adli ve idari yargıdaki iki Yüksek Mahkeme olan Yargıtay ve Danıştay’ın kararları ele alınmıştır ve yapay zekâ tabanlı bir karar destek sistemi geliştirilmesi amaçlanmıştır. Yargıtay ve Danıştay kararları; hukuki birliğin sağlanması, bireylerin hak ve özgürlüklerinin korunması ve adaletin sağlanması açısından büyük önem taşımaktadır. Bu kapsamda, Ulusal Yargı Ağı Projesindeki Mevzuat ve İçtihat programından alınan her iki Yüksek Mahkemeye ait karar metinleri kullanılmış olup bu kararların %11’i onama, %89’u ise bozma kararıdır. Bu nedenle, ele alınan problem, dengesiz sınıflandırma problemi olarak tanımlanmıştır. Öncelikle veri ön işleme ve doğal dil işleme (NLP) teknikleri kullanılarak karar metinlerinden öznitelikler çıkarılmıştır. Sonrasında, verideki dengesizliği gidermek amacıyla üst örnekleme yöntemlerinden Sentetik Azınlık Aşırı Örnekleme Tekniği (SMOTE) ve rastgele alt örnekleme uygulanmıştır. Son olarak, mahkeme kararlarının tahmin edilmesi amacıyla k-en yakın komşuluk, karar ağacı, destek vektör makinesi, rassal orman, LightGBM, XGBoost ve yapay sinir ağları ile sınıflandırma modelleri geliştirilerek modellerin performansları karşılaştırılmıştır. Elde edilen deneysel sonuçlar, önerilen karar destek sisteminin hukuk profesyonellerine fayda sağlama potansiyeli olduğunu göstermektedir."

# Metni parçalamak (cümle, kelime seviyesinde)
# Döngüler ve dict ile sayımlar yapmak
# Küçük rapor üretmek

# Yapman gerekenler:
# Kullanıcıdan bir metin al (input ile veya kod içine string koy).

# Şunları hesapla:
# Toplam karakter sayısı (boşluk dahil ve hariç ayrı ayrı)
# Toplam kelime sayısı
# Farklı kelime sayısı
# En sık geçen ilk 5 kelimeyi bul (küçük/büyük harfe dikkat: önce hepsini lower() ile küçült).
# Noktalama işaretlerini istersen çıkar (örneğin .,!?;: gibi karakterleri boşluğa çevir).
# Küçük bir rapor yazdır:

class TextAnalyzer():
    def __init__(self,text):
        replacement = {"â":"a"}
        for old, new in replacement.items():
            text = text.replace(old,new)
            pattern = r'[A-Za-zÇĞİÖŞÜçğıöşü]+'
            fmt_Text = re.findall(pattern, text.lower())
            self.text = fmt_Text


    def freqAll(self):
        freq_dict = {}
        words =  self.text

        for word in set(words) :
            freq_dict[word] = words.count(word)
        return freq_dict

    def word_sum(self):
        words = self.freqAll()
        word_count = 0
        for value in words.values():
            word_count+=value
        return word_count

    def sum_of_the_char(self):
        words = self.freqAll()
        count = 0
        for key,value in words.items():
            count += (len(key) * value)
        return count

    def firs_5_words(self):
        words = self.freqAll()
        first_5 = sorted(words.items(), key=lambda x:x[1], reverse=True)[:5]
        return first_5



a = TextAnalyzer(text)

differenet_words = len(a.freqAll())
sum_of_word = a.word_sum()
sum_of_the_char = a.sum_of_the_char()
first_5 = a.firs_5_words()


print("toplam karakter bosluklu sayisi " , len(text))
print("toplam karakter sayisi ", sum_of_the_char)
print("toplam kelime " , sum_of_word)
print("Farkli Kelime Sayisi: ", differenet_words)
print("ilk 5 Kelime Sayisi: ", first_5)







