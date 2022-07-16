from basic import db,Puppy

db.create_all()
# this creates all the tables, transform the model class to a DB Table

sam = Puppy('Sammy,',3)
frank = Puppy('Frankie',4)
# 2 puppy objects

# both will show none here, hasn't been given unique IDs yet until they get added to db
print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])

#alternatively you can add individually
# db.session.add(sam)
# db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank.id)
