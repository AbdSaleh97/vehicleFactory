import pytest
from vehicleFactory.motorcycle import Motorcycle
from vehicleFactory.car import Car

# Fixture to create a Car instance with default parameters
@pytest.fixture
def car_instance():
    return Car("Toyota", "petrol", "red")

# Fixture to create a Car instance with four doors
@pytest.fixture
def car_instance_with_four_doors():
    return Car("Honda", "electric", "blue", 4)

# Fixture to create a Motorcycle instance
@pytest.fixture
def motorcycle_instance():
    return Motorcycle("Harley Davidson", "petrol")

# Test car creation with default parameters
def test_car_creation(car_instance):
    assert car_instance._model_name == "Toyota"
    assert car_instance._fuel_type == "petrol"
    assert car_instance._color == "red"

# Test motorcycle creation
def test_motorcycle_creation(motorcycle_instance):
    assert motorcycle_instance._model_name == "Harley Davidson"
    assert motorcycle_instance._fuel_type == "petrol" 

# Test car creation with four doors
def test_car_creation_with_four_doors(car_instance_with_four_doors):
    assert car_instance_with_four_doors._model_name == "Honda"
    assert car_instance_with_four_doors._fuel_type == "electric"
    assert car_instance_with_four_doors._color == "blue"
    assert car_instance_with_four_doors._num_of_doors == 4

# Test changing fuel type of a car
def test_car_fuel_type_change(car_instance):
    car_instance.chng_fule_type("diesel")
    assert car_instance._fuel_type == "diesel"

# Test handling invalid fuel type for car
def test_invalid_fuel_type():
    with pytest.raises(ValueError):
        car_instance = Car("Toyota", "banzen", "red")

# Test handling invalid number of doors for car
def test_invalid_number_of_doors():
    with pytest.raises(ValueError):
        car_instance = Car("Honda", "electric", "blue", 3)

# Test changing fuel type of a motorcycle
def test_motorcycle_fuel_type_change():
    motorcycle_instance = Motorcycle("BMW", "electric")
    motorcycle_instance.chng_fule_type("diesel")
    assert motorcycle_instance._fuel_type == "diesel"

# Parametrized test to test car color change
@pytest.mark.parametrize("initial_color, new_color", [("red", "green"), ("blue", "yellow")])
def test_car_color_change(car_instance, initial_color, new_color):
    car_instance.change_color(new_color)
    assert car_instance._color == new_color

# Fixture with setup and teardown to prepare a motorcycle instance with a different fuel type
@pytest.fixture
def motorcycle_instance_with_different_fuel():
    motorcycle = Motorcycle("Suzuki", "petrol")
    yield motorcycle
    # Perform any cleanup if needed

# Test motorcycle fuel type change using a fixture with setup and teardown
def test_motorcycle_fuel_type_change_fixture(motorcycle_instance_with_different_fuel):
    motorcycle_instance_with_different_fuel.chng_fule_type("diesel")
    assert motorcycle_instance_with_different_fuel._fuel_type == "diesel"
