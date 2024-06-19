def Kalendar(year):
    zodiac_animals = ['крысы', 'коровы', 'тигра', 'зайца', 'дракона', 'змеи', 'лошади', 'овцы', 'обезьяны', 'курицы', 'собаки', 'свиньи']
    zodiac_elements = ['зелёного', 'красного', 'жёлтого', 'белого', 'чёрного']
    
    start_year = 1984
    start_animal_index = 0
    
    year_diff = year - start_year
    animal_index = (start_animal_index + year_diff) % 12
    element_index = year_diff // 2 % 5
    
    animal = zodiac_animals[animal_index]
    element = zodiac_elements[element_index]
    
    return f'С новым {year} годом! Это год {element} {animal}! Вам положен соицальный кредит и кошка-жена.'
input_year = int(input("Введите номер года -> "))
print(Kalendar(input_year))
