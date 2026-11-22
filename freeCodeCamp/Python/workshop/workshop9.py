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
        # if not isinstance(name, str) or not isinstance(level, str):
            # raise TypeError("'name' and 'level' attributes must be of type 'str'.")
            
        # if not isinstance(level, str):
            # raise TypeError("'level' attribute must be of type 'str'.") 
            
        # if level not in Employee._base_salaries:
            # raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        
        self.name = name
        self.level = level
        self.salary = Employee._base_salaries[level]
    
    def __str__(self):
        return f'{self.name}: {self.level}'
    
    def __repr__(self):
        return f'Employee({self.name!r}, {self.level!r})'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self._name}'.")
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    
    def level(self, new_level):
        if not isinstance(new_level, str):
            raise TypeError("'level' must be a string.")
        
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        
        if hasattr(self, '_level') and new_level == self.level:
            raise ValueError(f"'{new_level}' is already the selected level.")
        
        if (hasattr(self, '_level')
            and Employee._base_salaries[new_level] < Employee._base_salaries [self.level]):
            raise ValueError('Cannot change to lower level.')
        
        print(f"'{self.name}' promoted to '{new_level}'.")
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        
        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(
                f'Salary must be higher than minimum salary '
                f'${Employee._base_salaries[self.level]:.2f}.'
            )
        self._salary = new_salary
        print(f'Salary updated to ${self._salary:.2f}.')

charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)

# Step 10 is to remove these 2 lines below, so I commented them out instead

# print(charlie_brown.name)
# print(charlie_brown.level)

# Step 13 is to remove the print repr, so I commented it out instead.

#print(repr(charlie_brown))

# Step 19
print(f'Base salary: ${charlie_brown.salary:.2f}')
# charlie_brown.name = 'Charles Brown'
charlie_brown.level = 'junior'

# Last and final step
charlie_brown.salary = 2550.5