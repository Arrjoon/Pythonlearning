class User:
    first_neme = "Arjun"
    last_neme = "Nepali"


class AbstractUser:
    is_staff = True
    is_customer = False
    email = "nepaliarjun"


class User(AbstractUser):
    color = 'red'


a = User
print(a.email)
print(a.color)
b = AbstractUser
print(b.is_staff)
