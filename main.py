import random, string

print( """
  ___         _   _ _   _  _ _ _              ___                       _           
 / __|_ _ ___| |_(_|_) | \| (_) |_ _ _ ___   / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
 \__ \ '_/ -_) / / | | | .` | |  _| '_/ _ \ | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
 |___/_| \___|_\_\_|_| |_|\_|_|\__|_| \___/  \___\___|_||_\___|_| \__,_|\__\___/_|  
                                                                                    
""")
amount = int(input('Koliko hocete kodova: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('kodovi.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GENERATED] {code}')
    value += 1
