
def valence():
    element_group = {'H': 1, 'Li': 1, 'Na': 1, 'K': 1, 'Rb': 1, 'Cs': 1, 'Fr': 1, 
    'Be': 2,'Mg': 2, 'Ca': 2, 'Sr': 2, 'Ba': 2, 'Ra': 2, 'B': 3, 'Al': 3, 'Ga': 3,
    'In': 3, 'Tl': 3, 'C': 4, 'Si': 4, 'Ge': 4, 'Sn': 4, 'Pb': 4, 'N': 5,
    'P': 5, 'As': 5, 'Sb': 5, 'Bi': 5, 'O': 6, 'S': 6, 'Se': 6, 'Te': 6,
    'Po': 6, 'F': 7, 'Cl': 7, 'Br': 7, 'I': 7, 'At': 7,'Xe':8}

    return element_group

def geometrys(all_electron, lonepair):
    geometry = {20:'Linear',30:'Trigonal Planar',31:'Bent',40:'Tetrahedral',
                41:'Trigonal Pyramidal',50:'Trigonal Bipyramidal',51:'See Saw',52:'T-Shaped',
                60:'Octahedral',61:'Square Pyramid',62:'Square Planar',70:'Pentagonal Bipyramidal'}

    if all_electron == 2 or all_electron == 1:
        return geometry[20] ,180
    if all_electron == 3 :
        if lonepair == 0 :
            return geometry[30] ,120
        if lonepair == 1 :
            return geometry[31],119
    if all_electron == 4 :
        if lonepair == 0 :
            return geometry[40],109.5
        if lonepair == 1 :
            return geometry[41],107
        if lonepair == 2 :
            return geometry[31],119
    if all_electron == 5 :
        if lonepair == 0 :
            return geometry[50],'90, 120, 180'
        if lonepair == 1 :
            return geometry[51],'173.1, 101.6'
        if lonepair == 2 :
            return geometry[52],'87.5, <180'
        if lonepair == 3 :
            return geometry[20],180
    if all_electron == 6 :
        if lonepair == 0 :
            return geometry[60],'90, 180'
        if lonepair == 1 :
            return geometry[61],'84.8, 180'
        if lonepair == 2 :
            return geometry[62],'90, 180'
        if lonepair == 3 :
            return geometry[52],'87.5, <180'
        if lonepair == 4 :
            return geometry[20],180
    if all_electron == 7 :
        if lonepair == 0 :
            return geometry[70],'72, 90, 180'
        if lonepair == 1 : 
            return 'Pentagonal pyramidal',72
        if lonepair == 2 : 
            return 'Pentagonal planar','72, 90'
    if all_electron == 8 or (all_electron == 9 and lonepair == 1):
        return 'Square antiprismatic','70.5, 99.6 ,109.5' 
    else :
        return ''


def Vsepr_model(molecule : str): #POCL3

    if len(molecule) <= 1 :
        return 'Not Found'

    #F2 , all X2
    try :
        if len(molecule) == 2 and int(molecule[-1]) == 2 :
            return 'Linear','form' ,'do not have middle atom',1,'180',molecule[0], '', '',molecule[-1],'',''
    except :
        pass

    #O3
    if molecule.upper() == 'O3' :
        return 'Bent','form' ,1,2,'<120', 'O', '', '',3,'',''

    #H2O -> OH2
    if molecule[-1] != '-' and molecule[-1] != '+' :
        try :
            if int(molecule[1]) >= 2: 
                molecule = molecule[-1] + molecule[:-1]
        except :
            pass
    

    two_char = ['Be', 'Cl', 'Li' , 'Na' , 'Rb' , 'Cs', 'Fr', 'Mg' , 'Ca', 'Sr' , 'Ba' , 'Ra' , 'Al' , 'Ga' , 'In' , 
                 'Tl', 'Si', 'Ge', 'Sn', 'Pb', 'As', 'Sb', 'Bi', 'Se' , 'Te','Cl', 'Br','At','Xe']
    two_char = [element.upper() for element in two_char]


    if '+' in molecule or '-' in molecule :  
        #ICl4-
        ion = molecule[-1] # '-'
        
        try:
            element2_number = int(molecule[-2]) #4
        except :
            element2_number = 1 #HCL

        try :
            #SO4 2-
            if isinstance(int(molecule[-2]), int) and isinstance(int(molecule[-3]), int) :
                ion_num = int(molecule[-2]) #2
                element2_number = int(molecule[-3])
                molecule = molecule[:-3].upper() #SO
                
        except :
            #I3-
            if  len(molecule) < 4 :
                ion_num = int(molecule[-2]) 
            else :
                ion_num = 1
            molecule = (molecule[:-2].upper() if element2_number !=1 else molecule[:-1].upper())#ICL

            #I3-
            if molecule[0] == molecule[-1] :
                ion_num = 1

    else : #NH3
        ion = ''
        ion_num = 1
        try :
            element2_number = int(molecule[-1]) #3 , 4
        except :
            element2_number = 1
        
        #POCL4
        molecule = (molecule[:-1].upper() if element2_number !=1 else molecule[:].upper())#NH


    if len(molecule) > 2 :
        for element in two_char :  
            if molecule.startswith(element): #BeCL
                element1 = molecule[:2] #Be
                break           #if True then next section
            else : #NH
                element1 = molecule[0] #N
        molecule = molecule.removeprefix(element1)


        for element in two_char :  
            if molecule.endswith(element): #BeCl
                element2 = molecule[-1:-3:-1] #Cl
                element2 = ''.join(reversed(element2))
                break
            else : #NH
                element2 = molecule[-1] #H
        molecule = molecule.removesuffix(element2)

            
    else :
        element1 = molecule[0]
        element2 = molecule[-1]
        molecule = ''

    #print(element1, element2 , element2_number)
    #group -> valence electron
    element_group =  valence()

    #POCL3
    if molecule != '' :
        element3 = molecule #O
        want_electron = int((8 - element_group[element3.capitalize()]))
        element_group[element1.capitalize()] -= want_electron
    else :
        element3 = ''
    
    
    

    #when have ion -> electronegativity(EN)
    #if ion- F > O > N > Cl > Br > I , else H
    EN = {'F':4,'O':3.5,'N':3,'CL':3,'BR':2.8,'I':2.5,'S':2.5,'C':2.5,'P':2.1,'XE':0}


    #XeF5-
    if ion != '' :
        if ion == '-' :
            if element1 in EN and element2 in EN : #ICL4- --> 7 - 3 / 2 = 2

                #I3-
                    if EN[element1.upper()] < EN[element2.upper()] and ion_num == 1:
                        element2_number -= 1

                    #SO4 2-
                    else : #2

                        element_group[element1.capitalize()] += ion_num # 6 + 2 = 8
            
        else :
            element_group[element1.capitalize()] -= 2 # NH4+ -- > (5-2) - 3 /2 = 0
            element2_number -= 1
    
    #N -> 5  , NH3 ==> (5 - 1(3))/2 -> 1
    out_of_oxtate = ['H']
    if element1 == element2 :
        want_electron = int(8 - element_group[element2.capitalize()]) + ion_num
        element2_number -=1
        lonepair = int((element_group[element1.capitalize()] - ((want_electron)*(element2_number)))/2)
    else :
        want_electron = int((8 - element_group[element2.capitalize()] if element2 not in out_of_oxtate else 1)) #oxtate
        # want H-> 1 , NH3 lp =  5 - 3 /2 = 1 ,   all = 3 + 1 = 4
        lonepair = int((element_group[element1.capitalize()] - ((want_electron)*element2_number))/2)

    if ion_num == 1 :
        all_electron = (element2_number + lonepair if ion == '' else element2_number + 1 + lonepair)
    else :
        all_electron = (element2_number + lonepair)
    
    if element1 == element2 :
        all_electron = (element2_number + lonepair)

    if element3 != '' :
        all_electron += 1

    geometry =  geometrys(all_electron, lonepair)

    #OH2 - > H2O
    excepts = ['BE','B','C','N']
    if element2 == 'H' and  element1 not in excepts:
        try :
            element2 = element1
            element1 = 'H'
            return geometry[0],'form' ,lonepair, all_electron-lonepair,geometry[1], element1, element3, element2, element2_number,ion_num, ion
            
        except :
            pass
    if element3 != '':
        element2_number =  all_electron-lonepair - 1
        return geometry[0],'form' ,lonepair, all_electron-lonepair,geometry[1], element1, element3, element2, element2_number,ion_num, ion

    return geometry[0],'form' ,lonepair, all_electron-lonepair,geometry[1], element1, element3, element2, element2_number,ion_num, ion



# while True :
#     v = input(': ')
#     print(Vsepr_model(v))