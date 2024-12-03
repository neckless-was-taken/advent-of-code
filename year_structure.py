import os
import re

new_year = 0

for _ in range(0,2):
    user_input = str(input("Input year in YYYY format: "))
    # user_input = "2015"

    if re.match(r'\b20\d{2}', user_input):
        try:
            new_year = str(int(user_input))
            break
        except:
            continue
    print(f'Input of "{user_input}" is not accepted. Only years 2000 - 2099 are accepted, try again')
    print()

if new_year == 0:
    print(f'Failed to enter a valid year, exiting')
    exit()

new_folder = "year_" + new_year
new_full_directory = os.path.join(os.getcwd(), new_folder)

confirmation = str(input(f'Confirm to create folder {new_full_directory} [Y/N]: '))
if re.match(r'\by|Y', confirmation):
    pass


try:
    # os.makedir(f'year_{new_year}')
    pass
except:
    print(f'Folder "Folder "{new_full_directory}" already exists')

