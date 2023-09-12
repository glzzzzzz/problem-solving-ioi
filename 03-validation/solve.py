'''

Template for France-IOI programming tasks with debugger in gitpod

The Python version on gitpod is 3.11, whereas the python version on france-ioi
is sadly stuck at 3.4.2 ... This means no type hints, no dataclasses, ... The
code should therefore remain pretty basic to run flawlessly on france-ioi

'''

##################################################################
# read input from file tests/test1.in as if type on the keyboard
# This shouldn't run on France-IOI
# replace this with the name of your test file
test_file = 'test1.in'

import sys, os, platform
# only if executed on Python 3.11 (gitpod), will be false on france-ioi
if platform.python_version_tuple()[:2] == ('3', '11'):
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join('tests', test_file), "r")
##################################################################



def parse_input():
    '''
    
    Parses the input data and returns a dictionary with everything
    well structured.
    
    '''
    probleme ={}
    nb_livres, nb_jours = [int(x) for x in input().split(' ')]
    probleme['nb_livres']= nb_livres
    probleme['nb_jours']=nb_jours
    probleme['jours']=[]

    for i_jour in range(nb_jours):
        #charger les donnés du jour et les mettre dans la liste probleme['jours']
        nb_clients = int(input())
        jour = {
            'nb_clients': nb_clients,
            'reservations': []
        }
        for i_client in range(nb_clients):
            i_livre, duree = [int(x) for x in input().split(' ')]
            reservation = {
                'i_livres':i_livre,
                'duree' : duree
            }
            jour['reservations'].append(reservation)
        probleme['jours'].append(jour)
    return probleme

def solve(problem):
    result=[]

    nb_jours_empruntes = [0] * problem['nb_livres']

    for i_jour,jour in enumerate(problem['jours']):

        for r in jour['reservations']:
            
            if nb_jours_empruntes[r['i_livres']]<=i_jour:
                result.append(1)
                nb_jours_empruntes[r['i_livres']] = i_jour + r['duree']
                
            
            else:
                result.append(0)
                
    
    return result
        
    
    
def output(result):
    for r in result:
        print(r)
    
            


if __name__ == '__main__':
    problem = parse_input()
    result = solve(problem)
    output(result)