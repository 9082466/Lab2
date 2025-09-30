import random
from faker import Faker
fake = Faker()
import datetime

coupon_codes = ['SAVE10', 'HOLIDAY25', 'WELCOME5', 'BLACKFRIDAY50','']
cities = ['TORONTO', 'Vancouver', 'Montreal', 'CALGARY', 'OTTAWA', 'Edmonton', '']

for i in range(500):
    # generate random unique customer_id
    customer_id = random.randint(1000, 9999) 
    coupon_code = random.choice(coupon_codes)
    city = random.choice(cities)
    print(f" INSERT INTO customers (customer_id, coupon_code, city) VALUES ({customer_id}, '{coupon_code}', '{city}');")