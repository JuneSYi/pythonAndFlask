# BASIC.PY
# create entries into the tables
from models import db,Puppy,Owner,Toy

# CREATING 2 PUPPIES
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# ADD PUPPIES TO THE DB
db.session.add_all([rufus,fido])
db.session.commit()

# Check on the saved puppies in db
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# CREATE OWNER OBJECT
jose = Owner('Jose',rufus.id)

# give rufus some toys
toy1 = Toy('Chew Toy',rufus.id)
toy2 = Toy('ball',rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

print('test after commiting with owner and toys')
print(rufus)

# GRAB RUFUS AFTER THOSE ADDITIONS
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

print(rufus.report_toys())
