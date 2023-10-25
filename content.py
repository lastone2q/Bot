

def faculty():
    faculty = []
    f = open('subjects/faculty.txt', 'r')
    fr = f.readlines()
    for i in fr:
        i = i.strip()
        faculty.append(i)
    return faculty

def subjects(x):
    for i in faculty():
        if x == i:
            s = open(f'subjects/{i}_sub.txt', 'r')
            sr = s.readlines()
            return sr
      


 