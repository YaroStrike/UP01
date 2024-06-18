def chinese_zodiac(year):
    zodiac_animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
    zodiac_elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
    
    start_year = 1984
    start_animal_index = 0  # Index of 'Rat' in the zodiac_animals list
    
    year_diff = year - start_year
    animal_index = (start_animal_index + year_diff) % 12
    element_index = year_diff // 2 % 5
    
    animal = zodiac_animals[animal_index]
    element = zodiac_elements[element_index]
    
    return f'The Chinese Zodiac animal for the year {year} is {element} {animal}.'

input_year = int(input("Введите номер года: "))
print(chinese_zodiac(input_year))
