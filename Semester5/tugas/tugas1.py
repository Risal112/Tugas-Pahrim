import itertools

def brute_force_password_crack(possible_characters, password_length, target_password):
    attempts = 0
    for combination in itertools.product(possible_characters, repeat=password_length):
        attempts += 1
        guess = ''.join(combination)
        if guess == target_password:
            return guess, attempts
    return None, attempts

# Contoh penggunaan
characters = "dan"  # Karakter yang tersedia
length = 3          # Panjang kata sandi
target = "ada"      # Kata sandi yang harus ditemukan

result, attempts = brute_force_password_crack(characters, length, target)
if result:
    print(f"Kata sandi ditemukan: {result} dalam {attempts} percobaan.")
else:
    print("Kata sandi tidak ditemukan.")
