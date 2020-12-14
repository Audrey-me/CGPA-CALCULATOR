def degree_checker(grade):
    degree = 'Pass'
    y = ['first class honours', 'second class honours (upper division)', 'second class honours (lower division)',
         'third class honours']
    about = '''ABOUT
    The function takes in strings
    UOP students should include % while MAU students include gpa when entering grade.'''
    if type(grade) is not str:
        return about
    grade = grade.replace(' ', '')
    if '%' in str(grade):
        grade = grade.replace('%', '')
        grade = float(grade)
        grade = (grade / 100) * 5.0
        if 4.5 <= grade <= 5:
            degree = y[0]
        elif 3.5 <= grade <= 4.49:
            degree = y[1]
        elif 2.4 <= grade <= 3.39:
            degree = y[2]
        elif 1.5 <= grade <= 2.39:
            degree = y[3]
    elif 'gpa' in grade:
        grade = grade.replace('gpa', '')
        grade = float(grade)
        if 4.5 <= grade <= 5:
            degree = y[0]
        elif 3.5 <= grade <= 4.49:
            degree = y[1]
        elif 2.4 <= grade <= 3.39:
            degree = y[2]
        elif 1.5 <= grade <= 2.39:
            degree = y[3]
    else:
        return about
    return f'Dear student your CGPA is {grade:.2f}, you are a {degree} student.'


print(degree_checker('60%'))
print(degree_checker('4.5gpa'))