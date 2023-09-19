class Planets_distance_from_Earth():
  def __init__(self, name, distance):
    self.name = name
    self.distance = distance
       
mercury = Planets_distance_from_Earth('Mercury', '56,970,000')
venus = Planets_distance_from_Earth('Venus', '25,700,000')
mars = Planets_distance_from_Earth('Mars', '140,000,000')
jupiter = Planets_distance_from_Earth('Jupiter', '345,000,000')
saturn = Planets_distance_from_Earth('Saturn', ' 792,000,000')
uranus = Planets_distance_from_Earth('Uranus', "1'700,000,000")
neptune = Planets_distance_from_Earth('Neptune', "2'703,000,000")

planets_options = [ '1) Mercury.',
                    '2) Venus.',
                    '3) Mars.',
                    '4) Jupiter.',
                    '5) Saturn.',
                    '6) Uranus.',
                    '7) Neptune.',
                    '8) Return to Hall menu.'
                    ]
