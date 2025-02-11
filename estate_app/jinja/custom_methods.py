import frappe
import datetime

def greet_user(name):
    return f"Hello, {name}! Welcome to our system."
def format_date(value, format="%d-%m-%Y"):
    if isinstance(value, datetime.date):
        return value.strftime(format)
    return value
def add_custom_jinja_methods_and_filters():
    return {
        "methods": {
            "greet_user": greet_user
        },
        "filters": {
            "format_date": format_date
        }
    }
