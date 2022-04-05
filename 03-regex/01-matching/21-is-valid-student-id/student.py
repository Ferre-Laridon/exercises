# Write your code here
import re

def is_valid_student_id(string):
    return re.fullmatch('[rsRS]\d{7}', string)