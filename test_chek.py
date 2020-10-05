from app import parse_kanji, convert_simple_number, calc_all


big_unit = ["兆","億","万"]
short_unit = ["千","百","拾"]

name = "壱兆九拾九億七万五千参百弐拾参"







sum = calc_all(name, big_unit, short_unit)
print(sum)
    
    




