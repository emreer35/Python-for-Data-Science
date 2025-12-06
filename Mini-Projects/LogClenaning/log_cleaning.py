#%%
# app.log dosyasını düşün. İçinde tonla log var.
# Senin görevin: Sadece son 10 satırı bırakan bir fonksiyon yazmak.

# 🧠 İstenen:
# filename dosyasını r+ modunda aç.
# Tüm satırları listeye al: lines = f.readlines()
# Son line_count satırı bul: lines[-line_count:]
# Sonra:
# seek(0) ile başa dön
# Sadece bu son satırları tekrar yaz
# truncate() ile dosyanın geri kalanını kes
# 💡 Bu görev log rotation / log trimming mantığını öğretir ve r+ + truncate()’ı çok güzel pekiştirir.

log_file = '/Users/emreer/Desktop/Python for Data Science with Coursera/Mini-Projects/LogClenaning/daily_logs.txt'
def keepLastLines(filename, line_count=10):

    with open(filename,'r+') as lf:
        lines = lf.readlines()
        last_lines = lines[-line_count:]
        lf.seek(0)
        for ll in last_lines:
            lf.write(ll)
        lf.truncate()


# test

with open(log_file, 'r', encoding='utf-8') as f:
    print("Before:")
    print(f.read())

keepLastLines(log_file, 3)

with open(log_file, 'r', encoding='utf-8') as f:
    print("After:")
    print(f.read())