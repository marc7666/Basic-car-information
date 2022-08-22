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
from colorama import Fore
import time


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
        """
        This function checks if the car type is electric, hybrid or combustion
        :return: True or raises an Exception
        """
        if (self.vehicle_type == "Hybrid" or self.vehicle_type == "hybrid" or
                self.vehicle_type == "electric" or self.vehicle_type == "Electric" or
                self.vehicle_type == "combustion" or self.vehicle_type == "Combustion"):
            return True
        else:
            raise VehicleTypeNotValidException("Vehicle type not valid")

    def check_vin(self):
        """
        Checks if the VIN has the appropriate length
        :return: True or raises and exception
        """
        if len(self.vin) == 17:
            return True
        else:
            raise VINException("VIN format error")

    def check_distinction(self):
        """
        Checks the environmental distinction type
        :return: True or raises and exception
        """
        if (self.environmental_distinction == "C" or self.environmental_distinction == "B" or
                self.environmental_distinction == "ECO" or self.environmental_distinction == "0"):
            return True
        else:
            raise EnvironmentalDistinctionException("Environmental distinction not valid")

    def check_km(self):
        """
        Checks if the number of km of the car is in the range 0, 999999
        :return: True or raises and exception
        """
        if self.km < 0:
            raise KmException("Too few kilometers")
        elif self.km > 999999:
            raise KmException("Too much kilometers")
        else:
            return True

    def check_fuel(self):
        """
        Checks the fuel type
        :return: True or raises and exception
        """
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
        """
        Checks the transmission type
        :return: True or raises and exception
        """
        if (self.propulsion_transmission == "Automatic" or self.propulsion_transmission == "automatic"
                or self.propulsion_transmission == "Manual" or self.propulsion_transmission == "manual" or
                self.propulsion_transmission == "Sequential" or self.propulsion_transmission == "sequential"):
            return True
        else:
            raise TransmissionException("Propulsion transmission type not valid")

    def check_traction(self):
        """
        Checks the traction type
        :return: True or raises and exception
        """
        if (self.traction == "AWD" or self.traction == "RWD"
                or self.traction == "FWD" or self.traction == "4AWD" or self.traction == "4"):
            return True
        else:
            raise TractionException("Traction type not valid")

    def check_speed_rating(self):
        """
        Checks the seed rating letter
        :return: True or raises and exception
        """
        if ("L" <= self.tyre_speed_rating <= "Y"
                or self.tyre_speed_rating == "(Y)"):
            return True
        else:
            raise SpeedRatingException("Speed rating exception not valid")

    def write_in_file(self):
        """
        Checks all the parameters before writing it in a txt file
        :return: void method
        """
        print(Fore.CYAN + "Checking the introduced parameters, please wait...")
        if (self.check_type() and self.check_vin() and self.check_distinction()
                and self.check_km() and self.check_fuel() and self.check_transmission()
                and self.check_traction() and self.check_speed_rating()):
            print(Fore.GREEN + "Vehicle type -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Car brand -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Car model -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Car VIN -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Country -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Registration plate -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Car environmental distinction -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Car km -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Car fuel type -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Engine displacement -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Car power -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Car transmission type -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Car traction site -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Tyre width -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Tyre profile -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Tyre rim size -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Tyre load index -> OK")
            time.sleep(2)
            print(Fore.GREEN + "Tyre speed rating -> OK")
            print(Fore.YELLOW + "All parameters OK, writing in file, please wait...")
            time.sleep(3)
            file = open("Car_information.txt", "w")
            file.write("Vehicle type -> " + self.vehicle_type + "\n")
            file.write("Vehicle brand -> " + self.brand + "\n")
            file.write("Vehicle model -> " + self.model + "\n")
            file.write("Vehicle VIN -> " + self.vin + "\n")
            file.write("Registration country -> " + self.country + "\n")
            file.write("Registration plate -> " + self.registration_plate + "\n")
            file.write("Environmental distinction -> " + self.environmental_distinction + "\n")
            file.write("Kilometers -> " + str(self.km) + "\n")
            file.write("Vehicle fuel -> " + self.fuel + "\n")
            file.write("Engine displacement -> " + str(self.engine_displacement) + "\n")
            file.write("Vehicle power -> " + str(self.power) + "\n")
            file.write("Vehicle transmission -> " + self.propulsion_transmission + "\n")
            file.write("Vehicle traction -> " + self.traction + "\n")
            file.write("Tyre measures -> " + str(self.tyre_width) + "/" + str(self.tyre_profile) +
                       " R " + str(self.tyre_rim_size) + " " + str(self.tyre_load_index) + self.tyre_speed_rating)
            file.close()
            print(Fore.MAGENTA + "All information written in \"Car_information.txt\" file")


if __name__ == "__main__":
    car = CarInfo("Hybrid", "Toyota", "Yaris Cross", "4788 MMM", "Spain", "12345678945217985", "ECO",
                  2000, "Gasoline/Electric", 115, 1500, "Automatic",
                  "FWD", 215, 55, 17, 94, "V")
    car.write_in_file()
