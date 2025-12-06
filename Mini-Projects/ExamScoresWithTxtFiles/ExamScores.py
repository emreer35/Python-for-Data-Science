#%%
# cleanStudents(currentFile, passedFile, failedFile) fonksiyonu yaz:
# currentFile = students.txt
# passedFile = passed.txt
# failedFile = failed.txt
# Kurallar:
# students.txt dosyasını r+ modunda aç.
# Dosyadaki satırları oku, header’ı kaybetme.
# Passed kolonu:
# yes olanları → passed.txt dosyasına (append, yani a+)
# no olanları → failed.txt dosyasına (append, yani a+)
# students.txt içinde sadece yes olanlar kalsın:
# Yani şunu yap:
# En başa dön (seek(0))
# Sadece header + geçen öğrencileri tekrar yaz
# truncate() ile geri kalan kısmı kes
# Bu görev, senin yaptığın membership işiyle çok benzer, sadece kolon isimleri ve dosya sayısı arttı.


currentFile = '/Users/emreer/Desktop/Python for Data Science with Coursera/Mini-Projects/ExamScoresWithTxtFiles/Students.txt'
passedFile = '/Users/emreer/Desktop/Python for Data Science with Coursera/Mini-Projects/ExamScoresWithTxtFiles/passed.txt'
failedFile = '/Users/emreer/Desktop/Python for Data Science with Coursera/Mini-Projects/ExamScoresWithTxtFiles/failed.txt'
def clean_students(current_file,passed_file,failed_file):
    with open(current_file, 'r+') as cf:
        lines = cf.readlines()
        students = lines[1:]
        failed = [s for s in students if 'no' in s]
        passed = [s for s in students if 'no' not in s]

        with open(failed_file,'a+') as ff:
            for student in failed:
                ff.write(student)
        with open(passed_file, 'a+') as pf:
            for student in passed:
                pf.write(student)


clean_students(currentFile,passedFile,failedFile)
