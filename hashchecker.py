import hashlib

wordlist = ["dragon", "hello", "qwerty", "letmein", "monkey"]
target = "d0763edaa9d9bd2a9516280e9044d885"

for word in wordlist:
    h = hashlib.md5(word.encode()).hexdigest()
    if h == target:
        print("Хэш найден:", word)
        break
else:
    print("Пароль не найден")
