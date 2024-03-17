import phonenumbers 
numberquestion = input("Whats the phone number(WITH COUNTRY CODE!)?")

number = str(numberquestion)

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))


from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
