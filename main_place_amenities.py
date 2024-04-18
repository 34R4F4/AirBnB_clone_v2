#!/usr/bin/python3
"""Test Many-To-Many link between Place and Amenity"""

import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Create a State instance
state = State(name="California")
state.save()

# Create a City instance
city = City(state_id=state.id, name="San Francisco")
city.save()

# Create a User instance
user = User(email="john@snow.com", password="johnpwd")
user.save()

# Create two Place instances
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# Create three different Amenity instances
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# Link place_1 with two amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# Link place_2 with three amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

# Save changes to the database
models.storage.save()

print("OK")
