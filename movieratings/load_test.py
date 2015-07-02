# from data_app.models import Movie, Rating, User
import pandas as pd

with open('some_data/movies.dat', encoding='windows-1252') as file:
    data = file.readlines()


datus = pd.read_csv('some_data/movies.dat', encoding='windows-1252',
                    sep='::', engine='python', names=["id", "title", 'genres'])


datum = pd.read_csv('some_data/users.dat', sep='::', engine='python',
                    names=["id", "gender", "age", "occupation", "zipcode"])

print(datum.head())



from data_app.models import Movie, Rating, User
import pandas as pd


def load_user_data(apps, schema_editor):
    datum = pd.read_csv('some_data/users.dat', sep='::', engine='python',
                        names=["id", "gender", "age", "occupation", "zipcode"])

    for row in datum.iterrows():
        user_object = row[1]
        User.objects.create(user_id=user_object.id, gender=user_object.gender,
                            age=user_object.age,
                            occupation=user_object.occupation,
                            zipcode=user_object.zipcode)
