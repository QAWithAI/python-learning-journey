class Planet:
    def __init__(self,name,planet_type,star):

         # Validate all arguments are strings
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')
        
         # Validate all arguments are empty string
        if name == '' or planet_type =='' or star == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')

        self.name = name
        self.planet_type = planet_type
        self.star = star
    
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: '

# 3 instances
planet_1 = Planet('Earth',   'Terrestrial', 'Sun')
planet_2 = Planet('Mars',    'Terrestrial', 'Sun')
planet_3 = Planet('Jupiter', 'Gas Giant',   'Sun')

# Print each planet
print(planet_1)
print(planet_2)
print(planet_3)

# Call orbit on each
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())