# Exercise 1)
# 1. create an abstract class called SpaceShip which will simulate a spaceship for a video game.
# 	a. You can assume such simple properties as:
# 		i. position, size, displayName, speed
	
# 	b. Create a number of concrete classes such as:
# 		MilleniumFalcon
# 		UNSCInfinity
# 		USSEnterprise
# 		Serenity

# Using the Simple Factory Method create a factory implementation that will create each of these instances
from abc import ABC, abstractmethod
from enum import Enum

class SpaceShip(ABC):
	def __init__(self, position, size, display_name, speed):
		self.position = position
		self.size = size
		self.display_name = display_name
		self.speed = speed
		self.type = self.__class__.__name__

	def present(self):
		return (
			f"🚀 SpaceShip Overview:\n"
			f"  - Name: {self.display_name} ({self.type})\n"
			f"  - Position: {self.position}\n"
			f"  - Size: {self.size}\n"
			f"  - Speed: {self.speed} km/h\n"
		)	
class MilleniumFalcon(SpaceShip):
	pass
class UNSCInfinity(SpaceShip):
	pass
class USSEnterprise(SpaceShip):
	pass
class Serenity(SpaceShip):
	pass

class SpaceShipTypes(Enum):
	MilleniumFalcon = MilleniumFalcon.__name__
	UNSCInfinity = UNSCInfinity.__name__
	USSEnterprise = USSEnterprise.__name__
	Serenity = Serenity.__name__

class SpaceShipFactory:
	@staticmethod
	def create_ship(context: dict):
		_type = context.pop('type')
		if _type == SpaceShipTypes.MilleniumFalcon.value:
			return MilleniumFalcon(**context)
		elif _type == SpaceShipTypes.UNSCInfinity.value:
			return UNSCInfinity(**context)
		elif _type == SpaceShipTypes.USSEnterprise.value:
			return USSEnterprise(**context)
		elif _type == SpaceShipTypes.Serenity.value:
			return Serenity(**context)
		else:
			raise NotImplementedError("Type of ship not supported")

print(
SpaceShipTypes.MilleniumFalcon.value
)

mf = SpaceShipFactory.create_ship( {
	'type' : "MilleniumFalcon",
	'position': (1, 2),
	'size': "10m",
	'display_name': "Kraken",
	'speed': "30km/h"
	})
print(
	mf.present()
)





# Exercise 2)
# 1. You can try to implement the exact factory from Exercise#1 but using the classic Factory Method Pattern.
# 	a. This entails that you need to create a specific factory for each of the concrete SpaceShip class types.
# 	b. When you need to create for example USSEnterprise you will in fact delegate to USSEnterpriseFactory
# 	c. This means that the creation will need to be in some sort of switch to sort out which factory to use.
	
