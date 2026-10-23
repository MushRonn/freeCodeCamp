#step 1
email = 'alice.johnson@company.com'
print(f'Email: {email}')

#step 2
at_position = email.find('@')
print(f'Position of @: {at_position}')

#step 3
username = email[:at_position]
print(f'Username: {username}')

#step 4
has_at = '@' in email
print(f'Has @ symbol: {has_at}')

#step 5
has_com = '.com' in email
print(f'Has .com: {has_com}')

#step 6
messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")

#step 7 : cleaning a messy name on step 6
clean_name = messy_name.title()
print(clean_name)

#step 8 : further cleaning using strip().title()
clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

#step 9 : using .lower to clean messy email
messy_email = '  SARAH.DAVIS@COMPANY.COM  '
print(f"Original email: '{messy_email}'")

clean_email = messy_email.strip().lower()
print(f"Cleaned email: '{clean_email}'")

#step 10 : using .upper
name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')

#step 11 : finding @ and use slicing to extract username from email
at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]
print(f'Email: {clean_email}')
print(f'Username: {email_user}')

#step 12 : using .replace method
display_name = email_user.replace('.', ' ')
print(f'Display name: {display_name}')

phone = '123-456-7890'
phone_clean = phone.replace('-', '')
print(f'Phone with dashes: {phone}')
print(f'Phone without dashes: {phone_clean}')

#step 13: using .split to split a string into a list
full_address = '123 Main Street, Springfield, IL'
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}')

rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')

#step 14 : using .startswith and .endswith to check if a string starts and ends with a specific substring
employee_code = 'EMP-2024-SD'
starts_with_emp = employee_code.startswith('EMP')

ends_with_com = clean_email.endswith('.com')

print(f'Code: {employee_code}')
print(f'Starts with EMP: {starts_with_emp}')
print(f'Clean email: {clean_email}')
print(f'Ends with .com: {ends_with_com}')

#step 15 : using .count to count occurrences of a substring in a string
dot_count = clean_email.count('.')
dash_count = employee_code.count('-')
print(f'Dots in email: {dot_count}')
print(f'Dashes in code: {dash_count}')