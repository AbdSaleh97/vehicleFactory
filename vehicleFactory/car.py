from vehicleFactory.factory import Factory

class Car(Factory):
    _count = 0  # Initialize class variable
    
    def __init__(self, model_name, fuel_type, color, num_of_doors=4):
        super().__init__()
        self._model_name = model_name
        self._color = color
        Car._count += 1
        self._num_of_doors = self.change_number_of_doors(num_of_doors)
        self._fuel_type = super().chng_fule_type(fuel_type)  
        
    def chng_model_name(self, new_name):
        self._model_name = new_name
    
    def change_color(self, new_color):
        self._color = new_color
    
    def change_door_num(self, new_door_num):
        if new_door_num in [2, 4]:
            self._num_of_doors = new_door_num
        else:
            return None
    def change_number_of_doors(self, new_number_of_doors):
        """
        Changes the number of doors of the car.
        """
        if new_number_of_doors not in [2, 4]:
            raise ValueError("Invalid number of doors. Must be 2 or 4.")
        else:
            self._num_of_doors = new_number_of_doors
            return new_number_of_doors
        
    def __str__(self):
        return f"Model: {self._model_name}, Fuel Type: {self._fuel_type}, Color: {self._color}, Number of Doors: {self._num_of_doors}"
