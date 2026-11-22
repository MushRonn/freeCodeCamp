# Building a Salary Tracker
# Worth 40 steps

class Employee:
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000
    }
    
    def __init__(self, name, level):
        if not isinstance(name, str) or not isinstance(level, str):
            raise TypeError("'name' and 'level' attributes must be of type 'str'.")
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        
        self._name = name
        self._level = level
    
    def __str__(self):
        return f'{self.name}: {self.level}'
    
    def __repr__(self):
        return f'Employee({self.name!r}, {self.level!r})'
    
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level

charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)

# Step 10 is to remove these 2 lines below, so I commented them out instead

# print(charlie_brown.name)
# print(charlie_brown.level)

# Step 13 is to remove the print repr, so I commented it out instead.

#print(repr(charlie_brown))