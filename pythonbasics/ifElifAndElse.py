if 1<2:
    print('Yep!')
username = "admin"
check = 'admin'
if username==check:
    print('Access Granted')
if 2<1:
    print('it is')
else:
    print('2 is actually greater than 1, not less than')
if 1==2:
    print('good')
elif 1==1:
    print('nice')
else:
    print('loop complete')
permission = True
if username == 'admin' and permission:
    print('full access')
elif username == 'admin' and permission == False:
    print('guest access only')
else:
    print('no access')
