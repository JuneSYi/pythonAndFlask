from flask_bcrypt import Bcrypt

# to hash
bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed_password = bcrypt.generate_password_hash(password=password)


print(hashed_password)


#to check if password matches the hash

check = bcrypt.check_password_hash(hashed_password, 'wrongpassword')
crack = bcrypt.check_password_hash(hashed_password, 'supersecretpassword')

print(check)
print(crack)
