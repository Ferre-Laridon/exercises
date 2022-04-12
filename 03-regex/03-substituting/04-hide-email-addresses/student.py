# Write your code here
import re


def hide_email_addresses(string):
    def replace(match):
        lengte = len(match.group(0))
        return '*'*lengte
    
    return re.sub(r'[A-Za-z0-9.]+@[A-Za-z0-9.]+', replace, string)