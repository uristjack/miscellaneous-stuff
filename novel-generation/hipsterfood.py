import random
import pycorpora

def hfg():
    """Creates a description of a hipster food with the structure
    'A {animal} {sausage}, with a {fruit} chutney upon {bread}.',
    where the items in braces are randomly picked."""
    fruit = random.choice(pycorpora.foods.fruits["fruits"])
    bread = random.choice(pycorpora.foods.breads_and_pastries["breads"])
    animal = random.choice(pycorpora.animals.common["animals"])
    beer = random.choice(pycorpora.foods.beer_styles["beer_styles"])
    sausage = random.choice(pycorpora.foods.sausages["sausages"])
    
    return("A %s %s, with a %s chutney upon %s." % (animal, sausage, fruit, bread))

def hfg2():
    """Creates a description of a hipster food with the structure
    'A {curd} spiced with {spice} upon a slice of {bread}', where
    the items in braces are randomly picked."""
    curd = random.choice(pycorpora.foods.curds["curds"])
    spice = random.choice(pycorpora.foods.herbs_n_spices["spices"])
    bread = random.choice(pycorpora.foods.breads_and_pastries["breads"])

    return("A %s spiced with %s upon %s." % (curd, spice, bread))
