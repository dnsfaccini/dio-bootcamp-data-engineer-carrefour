import phonenumbers

from phonenumbers import geocoder

phone = input('Digite um telegone no formato: +551140028922: ')

phone_numbers = phonenumbers.parse(phone)

# Mostra a cidade do telefone digitado
print(geocoder.description_for_number(phone_numbers, 'pt'))