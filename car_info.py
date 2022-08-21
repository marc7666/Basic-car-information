"""
@project: CarInfo
@author: marc on 21/08/2022
"""
from Exceptions.EnvironmentalDistinctionException import EnvironmentalDistinctionException
from Exceptions.FuelException import FuelException
from Exceptions.KmException import KmException
from Exceptions.SpeedRatingException import SpeedRatingException
from Exceptions.TractionException import TractionException
from Exceptions.TransmissionException import TransmissionException
from Exceptions.VINException import VINException
from Exceptions.VehicleTypeNotValidException import VehicleTypeNotValidException


# pylint: disable=C0103, R0902, R0903, R0913
class CarInfo:
    """
    This class collects the basic information of a vehicle and saves it in a txt file
    """

    def __init__(self, vehicle_type, brand, model, registration_plate,
                 country, vin, environmental_distinction,
                 km, fuel, power, engine_displacement,
                 propulsion_transmission, traction, tyre_width, tyre_profile,
                 tyre_rim_size, tyre_load_index, tyre_speed_rating):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.model = model
        self.registration_plate = registration_plate
        self.country = country
        self.vin = vin
        self.environmental_distinction = environmental_distinction
        self.km = km
        self.fuel = fuel
        self.power = power
        self.engine_displacement = engine_displacement
        self.propulsion_transmission = propulsion_transmission
        self.traction = traction
        self.tyre_width = tyre_width
        self.tyre_profile = tyre_profile
        self.tyre_rim_size = tyre_rim_size
        self.tyre_load_index = tyre_load_index
        self.tyre_speed_rating = tyre_speed_rating

    def check_type(self):
        if (self.vehicle_type == "Hybrid" or self.vehicle_type == "hybrid" or
                self.vehicle_type == "electric" or self.vehicle_type == "Electric" or
                self.vehicle_type == "combustion" or self.vehicle_type == "Combustion"):
            return True
        else:
            raise VehicleTypeNotValidException("Vehicle type not valid")

    def check_vin(self):
        if len(self.vin) == 17:
            return True
        else:
            raise VINException("VIN format error")

    def check_distinction(self):
        if (self.environmental_distinction == "C" or self.environmental_distinction == "B" or
                self.environmental_distinction == "ECO" or self.environmental_distinction == "0"):
            return True
        else:
            raise EnvironmentalDistinctionException("Environmental distinction not valid")

    def check_km(self):
        if self.km < 0:
            raise KmException("Too few kilometers")
        elif self.km > 999999:
            raise KmException("Too much kilometers")

    def check_fuel(self):
        if self.vehicle_type == "Hybrid" or self.vehicle_type == "hybrid":
            if self.fuel == "Gasoline/Electric" or self.fuel == "gasoline/electric":
                return True
            else:
                raise FuelException("Fuel type not valid")
        elif self.vehicle_type == "Electric" or self.vehicle_type == "electric":
            if self.fuel == "electric battery" or self.fuel == "Electric battery":
                return True
            else:
                raise FuelException("Fuel type not valid")
        elif self.vehicle_type == "Combustion" or self.vehicle_type == "combustion":
            if self.fuel == "diesel" or self.fuel == "Diesel" or self.fuel == "gasoline" or self.fuel == "Gasoline":
                return True
            else:
                raise FuelException("Fuel type not valid")

    def check_transmission(self):
        if (self.propulsion_transmission == "Automatic" or self.propulsion_transmission == "automatic"
                or self.propulsion_transmission == "Manual" or self.propulsion_transmission == "manual" or
                self.propulsion_transmission == "Sequential" or self.propulsion_transmission == "sequential"):
            return True
        else:
            raise TransmissionException("Propulsion transmission type not valid")

    def check_traction(self):
        if (self.traction == "AWD" or self.traction == "RWD"
                or self.traction == "FWD" or self.traction == "4AWD" or self.traction == "4"):
            return True
        else:
            raise TractionException("Traction type not valid")

    def check_speed_rating(self):
        if ("L" <= self.tyre_speed_rating <= "Y"
        or self.tyre_speed_rating == "(Y)"):
            return True
        else:
            raise SpeedRatingException("Speed rating exception not valid")

    def write_in_file(self):
        if(self.check_type() and self.check_vin() and self.check_distinction()
        and self.check_km() and self.check_fuel() and self.check_transmission()
        and self.check_traction() and self.check_speed_rating()):
