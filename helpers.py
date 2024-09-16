import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


letters = string.ascii_letters
chars = string.ascii_letters + string.digits
digits = string.digits

def random_string_generator(str_size, charset = letters):
    return ''.join(random.choice(charset) for x in range(str_size))

def generate_random_string(str_size: int, hasDigits = False):
    if (hasDigits):
        return random_string_generator(str_size= str_size, charset=chars)
    else:
        return random_string_generator(str_size=str_size)
    
def generate_random_variable_string(min_size: int, max_size: int, hasDigits=False):
    str_size = random.randint(min_size, max_size)
    return generate_random_string(str_size,hasDigits)

def generate_random_integer(min: int, max: int):
    return random.randint(min, max)
        
def generate_random_email():
    username_size = random.randint(5, 18)
    domain_size = random.randint(4, 10)
    username = random_string_generator(username_size, charset=chars)
    domain = random_string_generator(domain_size)
    return f"{username}@{domain}.com"

def generate_random_month():
    return random.randint(1, 12)

def generate_random_year(twoDigits = True):
    if (twoDigits):
        return random.randint(25,35)
    else:
        return random.randint(2025, 2035)

def generate_invalid_credit_card_number():
    """
    Returns a credit card number that is invalid, verified by Luhn's algorithm
    """
    card_types = {
        'Visa': ['4'],
        'Mastercard': ['51', '52', '53', '54', '55'],
        'American Express': ['34', '37'],
        'Discover': ['6011']
    }
    card_type = random.choice(list(card_types.keys()))
    prefix = random.choice(card_types[card_type])

    # Generate the remaining digits
    remaining_length = 16 - len(prefix)  # Most cards are 16 digits, adjust for Amex
    if card_type == 'American Express':
        remaining_length = 15 - len(prefix)
    
    digits = [int(d) for d in prefix]
    digits.extend([random.randint(0, 9) for _ in range(remaining_length - 1)])
    
    # Calculate check digit using Luhn algorithm
    total = 0
    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]
        if (len(digits) - i) % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    
    # Make the check digit invalid by adding 1 (mod 10)
    check_digit = (10 - (total % 10)) % 10
    invalid_check_digit = (check_digit + 1) % 10
    digits.append(invalid_check_digit)
    
    # Format the card number
    card_number = ''.join(map(str, digits))
    if card_type == 'American Express':
        formatted_number = f"{card_number[:4]} {card_number[4:10]} {card_number[10:]}"
    else:
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
    
    return formatted_number

def generate_valid_credit_card_number():
    """
    Generates a credit card number from the 'Test Cards'. These cards conform to Luhn's algorithm, but they are not in use.
    """
    test_cards = [
        '4111111111111111',  # Visa
        '4012888888881881',
        '4222222222222',
        '4917484589897107',
        '4000056655665556',
        '4916577641065243',
        '5555555555554444',  # Mastercard
        '5105105105105100',
        '5431111111111111',
        '2223000048400011',
        '2223520043560014',
        '5200828282828210',
        '5577000055770004',
        '378282246310005',  # American Express
        '371449635398431',
        '374245455400126',
        '340000000000009',
        '378734493671000',
        '6011111111111117',  # Discover
        '6011000990139424',
        '6011981111111113',
        '6011667777777776',
        '6445644564456445',
        '3530111333300000',  # JCB
        '3566002020360505',
        '3588481389380004',
        '30569309025904',   # Diners Club
        '38520000023237',
        '36700102000000'
    ]

    return random.choice(test_cards)  

def find_element_by_xpath(driver, xpath, timeout=10):
    """
    Find an element by XPath with explicit wait.
    
    :param driver: Selenium WebDriver instance
    :param xpath: XPath of the element to find
    :param timeout: Maximum time to wait for the element (default 10 seconds)
    :return: The found WebElement
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except Exception as e:
        print(f"Error finding element with XPath '{xpath}': {e}")
        return None