def celsius_to_f(c):
    return (c * 1.8) + 32

def bmi(weight_kg, height_m):
    return weight_kg / (height_m**2)

def is_prime(n):
    if n < 2:
        return False
    prime = True

    for i in range(2, n-1):
        if n % i== 0:
            prime=False
            break
    return prime

def word_count(text):
    return len(text.split())