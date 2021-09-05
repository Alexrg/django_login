from django.db import models

class Person(models.Model):
    """
    Personal and main information about the user.

        first_name = Their first name.
        last_name = Their last name.
        genre = Their genre name.
        birthday = Their birth day.
    """
    GENRES = (
        ('M', 'Masculine'),
        ('F', 'Femenine'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    genre = models.CharField(max_length=1, choices=GENRES)
    birthday = models.DateField()

class User(models.Model):
    """
    User information.

        id_person = Relation between the user and it's data8u
        email = User's email.
        password = User's password.
    """
    id_person = models.ForeignKey("Person", related_name='users', on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)