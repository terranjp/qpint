import pint
from utils.unitUtilities import Unit

ur = pint.UnitRegistry()
Q_ = ur.Quantity


length = ['millimeter',
          'centimeter',
          'foot',
          'parsec',
          'meter',
          'light_year',
          'astronomical_unit']

velocity = ['meter/second',
            'speed_of_light',
            'knot',
            'KPH',
            'MPH']

area = ['ft**2', 'm**2']

mass = ['pound',
        'gram',
        'troy_pound',
        'ounce',
        'short_ton',
        'metric_ton',
        'grain']

volume = ['liter',
          'gallon',
          'cc',
          'stere']


force = ['newton',
         'kilonewton',
         'dyne',
         'force_kilogram',
         'force_gram',
         'force_ounce',
         'force_pound',
         'force_ton ',
         'kip']

def createUnitObjects(inUnits: list) -> list:

    units = []

    for u in inUnits:
        currentUnit = Unit(u)
        units.append(currentUnit)

    return units

velocity=createUnitObjects(velocity)
length=createUnitObjects(length)
area=createUnitObjects(area)

# myUnits = dict(, )

for unit in area:
    print(unit.display)