import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


student = User(
    first_name='Артем',
    last_name='Трунилин',
    email='trunilin@mail.com',
    gender='Male',
    phone_number='8910787986',
    date_of_birth='06 April,1992',
    subject='English',
    hobby='Sports',
    picture='photo.jpg',
    address='Мирная 186 д1',
    state='NCR',
    city='Delhi'
)
