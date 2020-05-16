# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base Class
class Vehicle:
    def init(self):
        pass

# Subclass Flight Vehicle of Vehicle
class FlightVehicle(Vehicle):
    def init(self):
        pass 

# Subclass Starship of Flight Vehicle, Grandchild of Vehicle
class Starship(FlightVehicle):
    def init(self):
        pass

# Subclass Airplane of Flight Vehicle, Grandchild of Vehicle
class Airplane(FlightVehicle):
    def init(self):
        pass

# Subclass Ground Vehicle of Vehicle
class GroundVehicle(Vehicle):
    def init(self):
        pass
    
# Subclass Car of Ground Vehicle, Grandchild of Vehicle
class Car(GroundVehicle):
    def init(self):
        pass 

# Subclass Motorcycle of Ground Vehicle, Grandchild of Vehicle
class Motorcycle(GroundVehicle):
    def init(self):
        pass 
