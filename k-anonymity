import hashlib
import requests
pw = input("Пароль: ")
full = hashlib.sha1(pw.encode()).hexdigest().upper()
prefix = full[:5]
suffix = full[5:]
r = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
x = r.text.splitlines()

for y in x:
    b = y.split(":")
    if b[0] == suffix:
        print(f"Found : {b[1]}")
        break
else:
    print("Not found")

