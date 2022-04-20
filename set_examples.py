lakshmi_countries = ['Spain', 'Portugal', 'Burkina Faso',
                     'Mongolia', 'Tuvalu', 'Spain', 'Spain',
                     'Peru', 'Uruguay', 'Laos', 'New Zealand',
                     'Laos', 'Tuvalu']

amanda_countries = ['Portugal', 'Spain', 'Laos', 'Germany',
                    'Poland', 'Paraguay', 'Uruguay',
                    'Tuvalu', 'France', 'UK']

lakshmi = set(lakshmi_countries)
amanda = set(amanda_countries)
amanda.add('Belgium')
amanda.add('Moldova')
lakshmi.add('Kazakhstan')

print(lakshmi)
print(amanda)

print("COMMON:", lakshmi & amanda)  #  intersection
print("NOT COMMON:", lakshmi ^ amanda) # xor
print("ALL:", lakshmi | amanda)  # union
print("Just Lakshmi:", lakshmi - amanda)
print('Just Amanda', amanda - lakshmi)

