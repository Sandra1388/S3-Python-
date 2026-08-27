'''
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
'''
if __name__ == '__main__':
    l1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l1.append((name,score))
    
    s = []
    for name, score in l1:
        s.append(score)
    s = list(set(s))
    s.sort()
    second_smallest = s[1]
    
    n = []
    for name, score in l1:
        if score == second_smallest:
            n.append(name)
    n.sort()
    for na in n:
        print(na)
