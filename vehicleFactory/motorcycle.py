from vehicleFactory.factory import Factory

class Motorcycle(Factory):
    _count = 0  # Initialize class variable
    
    def __init__(self, model_name, fuel_type, num_of_wheels=2):
        super().__init__()
        self._num_of_wheels = num_of_wheels
        self._model_name = model_name
        self._fuel_type = super().chng_fule_type(fuel_type)  
        Motorcycle._count += 1
        
    def chng_model_name(self, new_name):
        self._model_name = new_name
    
    def __str__(self):
        return f"Model: {self._model_name}, Fuel Type: {self._fuel_type}, Number of Wheels: {self._num_of_wheels}"
