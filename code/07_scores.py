from pprint import pprint

grade_lookups = [(95, 'A'),
                 (89, 'B'),
                 (83, 'C'),
                 (75, 'D'),
                 (0, 'F')]

with open('data/testscores.dat') as scores:
    names_score = {}
    for line in scores:
        name, score = line.rstrip().split(":")

        for grade_lookup in grade_lookups:
            if int(score) >= grade_lookup[0]:
                grade = grade_lookup[1]
                break
        names_score[name] = (score, grade)



    for name, score_grade in sorted(names_score.items()):
        print(name, score_grade[0], score_grade[1])
