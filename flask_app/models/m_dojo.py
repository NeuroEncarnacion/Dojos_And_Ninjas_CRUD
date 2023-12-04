from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models.m_ninja import Ninja


from flask import flash
from .m_ninja import Ninja

db = "dojos_and_ninjas_schema"


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


# Save dojo to database
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO dojos (name)
                VALUE ( %(name)s )
                """
        result = connectToMySQL(db).query_db(query, data)
        return result


# Get all data for dojos in database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos


    @classmethod
    def get_one_with_ninjas(cls, data):
        query = """
                SELECT * FROM dojos
                LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id 
                WHERE dojos.id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'age' : row['age'],
                'dojo_id' : row['dojo_id'],
                'created_at': row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(n))
        print(dojo)
        return dojo
