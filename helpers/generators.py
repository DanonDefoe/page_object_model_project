import random
import string


def generate_random_string(length=9):
    return ''.join(random.sample(string.ascii_lowercase, length))


def generate_random_email():
    return generate_random_string() + "@test.com"
