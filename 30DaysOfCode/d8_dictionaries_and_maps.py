import re
pattern = re.compile(r'^\w+ \d{8}$')

n = int(input())

phone_book = {}
for _ in range(n):
    contact = input()        
    if not pattern.match(contact):
        break    
    contact_info = contact.split(" ")    
    phone_book[contact_info[0]] = contact_info[1]

while True:
    try:
        query = input()
    except EOFError:
        break
    
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")  
