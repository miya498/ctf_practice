import itertools

def brute_force_password(charset, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            yield ''.join(attempt)

password = "abc"
charset = "abcdefghijklmnopqrstuvwxyz"
for attempt in brute_force_password(charset, max_length=3):
    if attempt == password:
        print(f"Password found: {attempt}")
        break
