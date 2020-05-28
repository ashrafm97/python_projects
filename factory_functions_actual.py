#creating function for making dough
#water, flour = return dough
#else:return not dough
def make_dough(ingredient1, ingredient2):

    if ingredient1 == 'water' and ingredient2 == 'flour':
        return 'dough'
    else:
        return 'not dough'

#baking bread robot...
#when dough = baked
#return bread was baked
#else return bread not baked

def bake_bread(dough):

    if dough=='baked':
        return 'bread was baked'
    else:
        return 'bread not baked'



# wholeweat robot
# when given water, wholewheat flour
# return wholewheat dough
# else I want to return not wholewheat dough

def wholewheat(ingredient1, ingredient2):
    if ingredient1 == 'water' and ingredient2 =='wholewheat flour':
        return 'factory downtime more effective, trying new markets'
    else:
        return 'factory downtime less effective, no new markets'

# when wholewheat dough baked
# return sell to niche clients
# else return niche clients uninterested

def wholewheat_sell(dough):
    if dough=='baked':
        return 'sell to niche clients'
    else:
        return 'no niche clients :('