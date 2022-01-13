"""
    Possible Combinations of actors in a movie
    Of categories : Popular, good, average, flop

    Possible combinations with Popular

        popular and good -> 2 cases ->  1. p > gd     2. gd > p
        popular and ok   -> 2 cases ->  1. p > ok     2. ok > p
        popular and flop -> 2 cases ->  1. p > flop   2. flop > p

    Possible combinations with Good

        good and ok   -> 2 cases ->  1. p > ok     2. ok > p
        good and flop -> 2 cases ->  1. p > flop     2. flop > p

    Possible combinations with ok

        ok and flop


"""

p = gd = ok = flop = 0


def check():
    """ Possible combinations with Popular  """

    if p == 3:
        return 'msg'


def check_if_hit(cg):
    if (p + gd) == 3 and gd != 0 and p != 0:
        """ popular and good -> 
            2 cases ->  1. p > gd 
                        2. gd > p       """
        if p > gd:
            return 'msg'

        elif gd > p:
            return 'msg'

    elif (p + ok) == 3 and ok != 0 and p != 0:
        """ popular and ok -> 
            2 cases ->   1. p > ok
                        2. ok > p   """
        if p > ok:
            return 'msg'

        elif ok > p:
            return 'msg'

    elif (p + flop) == 3 and flop != 0 and p != 0:
        """ popular and flop ->
            1 case ->   p > flop       """

        if p > flop:
            return 'msg'

    elif gd == 3:
        return ''


def check_if_hit_Or_Average():
    if (gd + ok) == 3 and gd != 0 and ok != 0:
        """ Possible combinations with Good   """
        if gd > ok:
            return ''

        elif ok > gd:
            return ''

    elif (gd + flop) == 3 and gd != 0 and flop != 0:
        if gd > flop:
            return ''

        elif flop > gd:
            return ''


def check_if_Avg_or_Below():
    if (ok + flop) == 3 and ok != 0 and flop != 0:
        if ok == 3:
            return ''

        if ok > flop:
            return ''


dp = dok = dflop = 0
movie_success_category = []
if dp == 1:
    movie_success_category = ['Super-Hit', 'Hit', 'Average']
    if p == 3:
        return 'Super-Hit'

    elif p != 0:
        return check_if_hit(movie_success_category):

        elif p == 0:
        return check_if_hit_Or_Average(movie_success_category)

if dok == 1:
    movie_success_category = ['Hit', 'Average', 'Below Average', 'flop']
