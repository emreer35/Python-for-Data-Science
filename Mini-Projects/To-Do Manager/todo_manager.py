#%%
# addTask → a+ kullan
# markDone → r+ kullan, seek + truncate
# cleanDone → senin membership projesine çok benziyor
# sadece done == yes olanlar archive.txt gibi bir yere gidecek

file = '/Users/emreer/Desktop/Python for Data Science with Coursera/Mini-Projects/To-Do Manager/todos.txt'


def addTask(filename, taskText):
    # Dosyayı r+ modunda kullan
    with open(filename, "r+", encoding="utf-8") as f:

        lines = f.readlines()
        last_id = 0
        for line in lines[1:]:
            parts = line.strip().split(";")
            if parts[0].isdigit() :
                current_id = int(parts[0])
                if current_id > last_id:
                    last_id = current_id
            else:
                print("not")

        new_id = last_id + 1

        new_line = f"{new_id};{taskText};no\n"
        if lines and not lines[-1].endswith("\n"):
            f.write("\n")

        f.write(new_line)

def mark_done(file, task_id):
    # ilgili id'yi bul, done i yes yap
    # başa dön  hepsini tekrar yaz  truncate
    with open(file, 'r+') as f:
        lines = f.readlines()
        if not lines:
            return
        new_lines = []
        new_lines.append(lines[0])
        todos = lines[1:]
        for todo in todos:
            freqTodo = todo.strip('\n').split(';')
            current_id_str = freqTodo[0]
            if current_id_str.isdigit():
                current_id = int(current_id_str)
                if current_id == task_id:
                    freqTodo[2] = 'yes'

            list_todo = ';'.join(freqTodo)
            new_lines.append(list_todo+'\n')

        f.seek(0)
        for line in new_lines:
            f.write(line)
        f.truncate()
# bunun mantigini yeni eklenenler todos a no olarak kaydedlecek
# yapilanlar direkt archive atilacak
archive_file = '/Users/emreer/Desktop/Python for Data Science with Coursera/Mini-Projects/To-Do Manager/archive.txt'
def clean_done(filename, archive_file):
    with open(filename,'r+') as f:
        lines = f.readlines()
        header = lines[0]
        todos = lines[1:]

        completed = []
        remaining = []
        for todo in todos:
            line = todo.strip()
            if not line:
                continue

            parts = line.split(";")  # ["id", "task", "done"]
            if len(parts) < 3:
                continue

            done_flag = parts[2]

            # done alanina bak
            if done_flag == "yes":
                completed.append(";".join(parts) + "\n")
            else:
                remaining.append(";".join(parts) + "\n")

        f.seek(0)
        f.write(header)
        for line in remaining:
            f.write(line)
        f.truncate()

        with open(archive_file,'a+') as af:
            af.seek(0,2)
            if af.tell() == 0:
                af.write(header)
            for line in completed:
                af.write(line)



#
# addTask(file, "Finish Coursera homework")
# addTask(file, "Practice Python file I/O")
#
# with open(file, "r") as f:
#     print(f.read())


#
# mark_done(file, 1)
#
# with open(file, "r", encoding="utf-8") as f:
#     print(f.read())
#

clean_done(file, archive_file)

with open(file, 'r', encoding='utf-8') as f:
    print("TODOS:\n", f.read())

with open(archive_file, 'r', encoding='utf-8') as f:
    print("ARCHIVE:\n", f.read())