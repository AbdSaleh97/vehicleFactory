from abc import ABC, abstractmethod

class Factory:
    '''This is parent class'''
    _count = 0

    def __init__(self):
        # self.count +=1
        pass
    
    def read_attribute(self, attribute_name):
        if hasattr(self, attribute_name):
            return getattr(self, attribute_name)
        else:
            return None
        
    def chng_fule_type(self, new_fuel):
        """
        Changes the fuel type .
        """
        valid_fuel_types = ["electric", "petrol", "diesel"]
        if new_fuel.lower() not in valid_fuel_types:
            raise ValueError("Invalid fuel type. Must be electric, petrol, or diesel.")
        self._fuel_type = new_fuel.lower()
        return new_fuel


    @classmethod
    def printtotalcreated(cls):
        """
        Prints the total number of vehicles created.
        """
        print(f"Total {cls.__name__}s created:", cls._count)
        