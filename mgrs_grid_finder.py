def mgrs_to_utm_function(GRIDREF):

    mgrs_coord_components = list(GRIDREF)

    utm_zone = []
    mgrs_grid_Comps = []

    if mgrs_coord_components[0].isdigit() == False:
        utm_zone = ['invalid entry']

    if (mgrs_coord_components[0] == str('1') and
        str(mgrs_coord_components[1]).isdigit() == False):
            utm_zone = ['1']

            if (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[2:]

            elif (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[1:]

    if (mgrs_coord_components[0] == str('2') and
        str(mgrs_coord_components[1]).isdigit() == False):
            utm_zone = ['2']

            if (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[2:]

            elif (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[1:]

    if (mgrs_coord_components[0] == str('3') and
        str(mgrs_coord_components[1]).isdigit() == False):
            utm_zone = ['3']

            if (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[2:]

            elif (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[1:]

    if (mgrs_coord_components[0] == str('4') and
        str(mgrs_coord_components[1]).isdigit() == False):
            utm_zone = ['4']

            if (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[2:]

            elif (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[1:]

    if (mgrs_coord_components[0] == str('5') and
        str(mgrs_coord_components[1]).isdigit() == False):
            utm_zone = ['5']

            if (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[2:]

            elif (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[1:]

    if (mgrs_coord_components[0] == str('6') and
        str(mgrs_coord_components[1]).isdigit() == False):
            utm_zone = ['6']

            if (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[2:]

            elif (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[1:]

    if (mgrs_coord_components[0] == str('7') and
        str(mgrs_coord_components[1]).isdigit() == False):
            utm_zone = ['7']

            if (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[2:]

            elif (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[1:]

    if (mgrs_coord_components[0] == str('8') and
        str(mgrs_coord_components[1]).isdigit() == False):
            utm_zone = ['8']

            if (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[2:]

            elif (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[1:]

    if (mgrs_coord_components[0] == str('9') and
        str(mgrs_coord_components[1]).isdigit() == False):
            utm_zone = ['9']

            if (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[2:]

            elif (mgrs_coord_components[1] == str(' ') and mgrs_coord_components[2] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[1:]

    if (mgrs_coord_components[0] == str('1') and
        mgrs_coord_components[1] == str('0') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['10']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('1') and
        mgrs_coord_components[1] == str('1') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['11']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('1') and
        mgrs_coord_components[1] == str('2') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['12']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('1') and
        mgrs_coord_components[1] == str('3') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['13']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('1') and
        mgrs_coord_components[1] == str('4') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['14']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('1') and
        mgrs_coord_components[1] == str('5') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['15']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('1') and
        mgrs_coord_components[1] == str('6') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['16']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('1') and
        mgrs_coord_components[1] == str('7') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['17']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('1') and
        mgrs_coord_components[1] == str('8') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['18']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('1') and
        mgrs_coord_components[1] == str('9') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['19']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('2') and
        mgrs_coord_components[1] == str('0') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['20']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('2') and
        mgrs_coord_components[1] == str('1') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['21']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('2') and
        mgrs_coord_components[1] == str('2') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['22']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('2') and
        mgrs_coord_components[1] == str('3') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['23']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('2') and
        mgrs_coord_components[1] == str('4') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['24']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('2') and
        mgrs_coord_components[1] == str('5') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['25']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('2') and
        mgrs_coord_components[1] == str('6') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['26']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('2') and
        mgrs_coord_components[1] == str('7') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['27']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('2') and
        mgrs_coord_components[1] == str('8') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['28']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('2') and
        mgrs_coord_components[1] == str('9') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['29']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('3') and
        mgrs_coord_components[1] == str('0') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['30']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('3') and
        mgrs_coord_components[1] == str('1') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['31']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('3') and
        mgrs_coord_components[1] == str('2') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['32']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('3') and
        mgrs_coord_components[1] == str('3') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['33']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('3') and
        mgrs_coord_components[1] == str('4') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['34']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('3') and
        mgrs_coord_components[1] == str('5') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['35']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('3') and
        mgrs_coord_components[1] == str('6') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['36']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('3') and
        mgrs_coord_components[1] == str('7') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['37']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('3') and
        mgrs_coord_components[1] == str('8') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['38']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('3') and
        mgrs_coord_components[1] == str('9') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['39']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('4') and
        mgrs_coord_components[1] == str('0') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['40']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('4') and
        mgrs_coord_components[1] == str('1') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['41']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('4') and
        mgrs_coord_components[1] == str('2') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['42']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('4') and
        mgrs_coord_components[1] == str('3') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['43']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('4') and
        mgrs_coord_components[1] == str('4') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['44']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('4') and
        mgrs_coord_components[1] == str('5') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['45']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('4') and
        mgrs_coord_components[1] == str('6') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['46']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('4') and
        mgrs_coord_components[1] == str('7') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['47']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('4') and
        mgrs_coord_components[1] == str('8') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['48']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('4') and
        mgrs_coord_components[1] == str('9') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['49']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('5') and
        mgrs_coord_components[1] == str('0') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['50']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('5') and
        mgrs_coord_components[1] == str('1') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['51']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('5') and
        mgrs_coord_components[1] == str('2') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['52']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('5') and
        mgrs_coord_components[1] == str('3') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['53']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('5') and
        mgrs_coord_components[1] == str('4') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['54']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('5') and
        mgrs_coord_components[1] == str('5') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['55']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('5') and
        mgrs_coord_components[1] == str('6') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['56']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('5') and
        mgrs_coord_components[1] == str('7') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['57']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('5') and
        mgrs_coord_components[1] == str('8') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['58']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('5') and
        mgrs_coord_components[1] == str('9') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['59']

            if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[3:]

            elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                mgrs_grid_Comps = mgrs_coord_components[4:]
            else:
                mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_coord_components[0] == str('6') and
        mgrs_coord_components[1] == str('0') and
        str(mgrs_coord_components[2]).isdigit() == False):
            utm_zone = ['60']

            def mgrs_grid_Comps_function(mgrs_coord_components):

                if (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] != str(' ')):
                    mgrs_grid_Comps = mgrs_coord_components[3:]

                elif (mgrs_coord_components[2] == str(' ') and mgrs_coord_components[3] == str(' ')):
                    mgrs_grid_Comps = mgrs_coord_components[4:]
                else:
                    mgrs_grid_Comps = mgrs_coord_components[2:]

    if (mgrs_grid_Comps[1] == str(' ') and mgrs_grid_Comps[2] != str(' ')):
        mgrs_map_ref = mgrs_grid_Comps[2:]

    elif (mgrs_grid_Comps[1] == str(' ') and mgrs_grid_Comps[2] == str(' ')):
        mgrs_map_ref = mgrs_grid_Comps[3:]
    else:
        mgrs_map_ref = mgrs_grid_Comps[1:]

    if (mgrs_coord_components[0] == str('6') and
        int(mgrs_coord_components[1]) > 0):
        utm_zone = ['invalid entry']

    if mgrs_coord_components[2].isdigit() == True:
        utm_zone = ['invalid entry']

    if (mgrs_coord_components[0] == str('7') and
        mgrs_coord_components[1].isdigit() == True):
        utm_zone = ['invalid entry']

    if (mgrs_coord_components[0] == str('8') and
        mgrs_coord_components[1].isdigit() == True):
        utm_zone = ['invalid entry']

    if (mgrs_coord_components[0] == str('9') and
        mgrs_coord_components[1].isdigit() == True):
        utm_zone = ['invalid entry']

    utm_zone_str = ''
    for element in utm_zone:
        utm_zone_str += str(element)

    mgrs_grid_str = ''
    for element in mgrs_grid_Comps:
        mgrs_grid_str += str(element)

    mgrs_map_ref_str = ''
    for element in mgrs_map_ref:
        mgrs_map_ref_str += str(element)

    return utm_zone_str, mgrs_grid_str, mgrs_map_ref_str, mgrs_coord_components

utm_zone, mgrs_grid_ref, mgrs_map_ref, mgrs_list_components = mgrs_to_utm_function('59  ASD3456')

print('UTM zone: ' + utm_zone)
print('MGRS latitude band: ' + mgrs_grid_ref[0:1])
print('MGRS map reference: ' + mgrs_map_ref[0:2])
print(mgrs_list_components)
