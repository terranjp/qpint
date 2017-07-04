from . import Q_, ur


length = ['millimeter',
          'centimeter',
          'foot',
          'inch',
          'yard',
          'mile',
          'kilometer',
          'parsec',
          'meter',
          'light_year',
          'astronomical_unit',
          'survey_foot',
          'survey_mile ',
          'league',
          'fathom']

mass = ['pound',
        'gram',
        'troy_pound',
        'ounce',
        'short_ton',
        'metric_ton',
        'grain',
        'stone']

volume = ['liter',
          'gallon',
          'cc',
          'ft**3',
          'm**3',
          'pint',
          'quart',
          'fluid_ounce',
          'teaspoon',
          'tablespoon',
          'shot',
          'cup',
          'barrel',
          'oil_barrel']

velocity = ['meter/second',
            'meter/hour',
            'mile/hour',
            'speed_of_light',
            'knot',
            'kph',
            'mph']

force = ['newton',
         'kilonewton',
         'dyne',
         'force_kilogram',
         'force_gram',
         'force_ounce',
         'force_pound',
         'force_ton ',
         'kip']

linearDensity = ['lbf/ft',
                 'kgf/m',
                 'kip/ft',
                 'newton/m',
                 'kilonewton/m']


area = ['ft**2',
        'm**2',
        'hectare',
        'acre']

class Unit:
    def __init__(self, baseUnit):
        self.unit = Q_(1, ur[baseUnit])

    def __str__(self):
        return str(self.unit.u)

    def __repr__(self):
        return '<{}({})'.format(self.__class__.__name__, self.unit.u)

    @property
    def display(self):

        prettyUnit = '{:P}'.format(self.unit.u)
        prettyUnit = str(prettyUnit).replace('_', ' ')

        return '{} ({:~P})'.format(prettyUnit, self.unit.u)


def convertUnit(value: float, oldUnit: str, newUnit: str) -> ur.Quantity:

    quantity = Q_(value, ur[oldUnit]).to(newUnit)

    return str(quantity.magnitude)


def createUnitObjects(inUnits: list) -> list:

    units = []

    for u in sorted(inUnits):
        currentUnit = Unit(u)
        units.append(currentUnit)

    return units

myUnits = {'Velocity': createUnitObjects(velocity),
           'Length': createUnitObjects(length),
           'Area': createUnitObjects(area),
           'Volume': createUnitObjects(volume),
           'Force': createUnitObjects(force),
           'Mass': createUnitObjects(mass),
           'Linear Density': createUnitObjects(linearDensity)}