from werkzeug.security import generate_password_hash, check_password_hash   

def is_valid_url(url):
    return True

def convert_to_hash(plain_text):
    hashed_text = generate_password_hash(plain_text)
    return hashed_text

def check_hash(plain_text, hashed_text):
    check = check_password_hash(hashed_text, plain_text)
    return check