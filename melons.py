"""This file should have our melon-type classes in it."""


# class WatermelonOrder(object):
#     species = "Watermelon"
#     color = "green"
#     imported = False
#     shape = 'natural'
#     seasons = ['Fall', 'Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""
#         base_cost = 5.00
#         total = base_cost
#         if self.imported == True:
#             total += (base_cost *1.5)
#         if self.shape == 'square':
#             total += 2.00

#         if qty >= 3:
#             total *= 0.75
#         return total * qty 

# class CantaloupeOrder(object):
#     species = "Cantaloupe"
#     color = "tan"
#     imported = False
#     shape = 'natural'
#     seasons = ['Spring', 'Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""
#         base_cost = 5.00
#         total = base_cost
#         if self.imported == True:
#             total += (base_cost *1.5)
#         if self.shape == 'square':
#             total += 2.00

#         if qty >=5:
#             total *= 0.5
#         return total * qty

# class CasabaOrder(object):
#     species = "Casaba"
#     color = "green"
#     imported = True
#     shape = 'natural'
#     seasons = ['Spring', 'Summer', 'Fall', 'Winter']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""
#         base_cost = 6.00
#         total = base_cost
#         if self.imported == True:
#             total += (base_cost *1.5)
#         if self.shape == 'square':
#             total += 2.00
#         return total * qty 

# class SharlynOrder(object):
#     species = "Sharlyn"
#     color = "tan"
#     imported = True
#     shape = 'natural'
#     seasons = ['Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""
#         base_cost = 5.00
#         total = base_cost
#         if self.imported == True:
#             total += (base_cost *1.5)
#         if self.shape == 'square':
#             total += 2.00
#         return total * qty

# class SantaClauseOrder(object):
#     species = "Santa Claus"
#     color = "green"
#     imported = True
#     shape = 'natural'
#     seasons = ['Winter', 'Spring']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""
#         base_cost = 5.00
#         total = base_cost
#         if self.imported == True:
#             total += (base_cost *1.5)
#         if self.shape == 'square':
#             total += 2.00
#         return total * qty

# class ChristmasOrder(object):
#     species = "Christmas"
#     color = "green"
#     imported = False
#     shape = 'natural'
#     seasons = ['Winter']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""
#         base_cost = 5.00
#         total = base_cost
#         if self.imported == True:
#             total += (base_cost *1.5)
#         if self.shape == 'square':
#             total += 2.00
#         return total * qty

# class HornedOrder(object):
#     species = "Horned Melon"
#     color = "yellow"
#     imported = True
#     shape = 'natural'
#     seasons = ['Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""
#         base_cost = 5.00
#         total = base_cost
#         if self.imported == True:
#             total += (base_cost *1.5)
#         if self.shape == 'square':
#             total += 2.00
#         return total * qty

# class XiguaOrder(object):
#     species = "Xigua"
#     color = "black"
#     imported = True
#     shape = 'square'
#     seasons = ['Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""
#         base_cost = 5.00
#         total = base_cost
#         if self.imported == True:
#             total += (base_cost *1.5)
#         if self.shape == 'square':
#             total += 2.00
#         return total * qty

# class OgenOrder(object):
#     species = "Ogen"
#     color = "tan"
#     imported = False
#     shape = 'natural'
#     seasons = ['Spring', 'Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""
#         base_cost = 6.00
#         total = base_cost
#         if self.imported == True:
#             total += (base_cost *1.5)
#         if self.shape == 'square':
#             total += 2.00
#         return total * qty


class MelonOrder(object):
    species = " "
    color = "green"
    imported = False
    shape = 'natural'
    seasons = []

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.species == "Ogden" or self.species == "Casaba":
            base_cost = 6.00
        else:
            base_cost = 5.00
        
        total = base_cost
        if self.imported == True:
            total += (base_cost *1.5)
        if self.shape == 'square':
            total += 2.00
        
        if self.species == "Watermelon" and qty >= 3:
            multiplier = 0.75
        if self.species == "Cantaloupe" and qty >= 5:
            multiplier = 0.5
        else:
            multiplier = 1

        return total * qty * multiplier


class WatermelonOrder(MelonOrder):
    """An order of watermelons"""

    def __init__(self, species="Watermelon", seasons=['Fall','Summer']):
        self.species = species
        self.seasons = seasons 

class CantalopeOrder(MelonOrder):
    """An order of cantalopes"""

    def __init__(self, species="Cantaloupe", color='tan', seasons=['Spring','Summer']):
        self.species = species
        self.color = color
        self.seasons = seasons 

class CasabaOrder(MelonOrder):
    """An order of casabas"""

    def __init__(self, species="Casaba", imported=True, seasons=['Spring', 'Summer', 'Fall', 'Winter']):
        self.species = species
        self.imported = imported
        self.seasons = seasons 

class SharlynOrder(MelonOrder):
    """An order of sharlyns"""

    def __init__(self, species="Sharlyn", color='tan', imported=True, seasons=['Summer']):
        self.species = species
        self.color = color
        self.imported = imported
        self.seasons = seasons 

class SantaClausOrder(MelonOrder):
    """An order of santa claus melons"""

    def __init__(self, species="Santa Claus", imported=True, seasons=['Winter', 'Spring']):
        self.species = species
        self.imported = imported
        self.seasons = seasons 

class ChristmasOrder(MelonOrder):
    """An order of christmas melons"""

    def __init__(self, species="Christmas Melon",seasons=['Winter']):
        self.species = species
        self.seasons = seasons 

class HornedOrder(MelonOrder):
    """An order of horned melons"""

    def __init__(self, species="Horned Melon", color='yellow', imported=True, seasons=['Summer']):
        self.species = species
        self.color = color
        self.imported = imported
        self.seasons = seasons 

class XiguaOrder(MelonOrder):
    """An order of santa claus melons"""

    def __init__(self, species="Xigua", color='black', imported=True, seasons=['Summer']):
        self.species = species
        self.color = color
        self.imported = imported
        self.seasons = seasons 

class OgenOrder(MelonOrder):
    """An order of santa claus melons"""

    def __init__(self, species="Ogen", color='tan', seasons=['Spring', 'Summer']):
        self.species = species
        self.color = color
        self.seasons = seasons 