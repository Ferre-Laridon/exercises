# Write your code here
def format_grades(grades):
    def calc_average(list):
        return round(sum(list)/len(list))

    return '\n'.join(f'{name}: {calc_average(grades)}' for name, grades in grades.items())
