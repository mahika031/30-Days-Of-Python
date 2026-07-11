#02-Done 

# Variables in Python

first_name = 'Mahika'
last_name = 'Singh'
country = 'India'
city = "Greater Noida"
age = 20
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Mahika',
    'lastname': 'Singh',
    'country': 'India',
    'city': 'Greater Noida'
}

# Printing the values stored in the variables

print('First name:', first_name)   #Mahika
print('First name length:', len(first_name))   #6
print('Last name: ', last_name)   #Singh
print('Last name length: ', len(last_name))   #5
print('Country: ', country)   #India
print('City: ', city)   #Greater Noida
print('Age: ', age)   #20
print('Married: ', is_married)   #False
print('Skills: ', skills)   #
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Mahika', 'Singh', 'Greater Noida', 20, False

print(first_name, last_name, country, age, is_married) 
print('First name:', first_name)   #Mahika
print('Last name: ', last_name)   #Singh
print('Country: ', country)   #India
print('Age: ', age)   #20
print('Married: ', is_married)   #False
