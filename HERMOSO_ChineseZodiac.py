def find_chinese_zodiac_sign(year):
    zodiac_animals = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep']
    starting_year = 1900
    offset = (year - starting_year) % 12
    zodiac_sign = zodiac_animals[offset]
    return zodiac_sign

# Input the year for which you want to find the Chinese zodiac sign
year = int(input("Enter a year: "))

if year >= 1900:
    zodiac_sign = find_chinese_zodiac_sign(year)
    print(f"The Chinese zodiac sign for the year {year} is {zodiac_sign}.")
else:
    print("Please enter a year greater than or equal to 1900.")



