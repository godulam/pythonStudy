# import re library. functions from this library are used in input validation
import re

# FUNCTIONS

def missingDL():
    global missingFlag
    if tr_signal=='missing' and missingFlag==0:
        print('missing 1 element')
        missingFlag = 1
        DL[tr_MS_id].append(DL[tr_MS_id][-1])
        print('our list is: ', DL[tr_MS_id])
    elif tr_signal == 'missing' and missingFlag == 1:
        print('missing 2 elements')
        DL[tr_MS_id].append(-95)
        print('our list is: ', DL[tr_MS_id])
    elif (tr_signal!='missing'):
        missingFlag=0
        print('Flag: ',missingFlag)

def missingUL():
    global missingFlag
    if tr_signal=='missing' and missingFlag==0:
        print('missing 1 element')
        missingFlag = 1
        UL[tr_MS_id].append(UL[tr_MS_id][-1])
        print('our list is: ', UL[tr_MS_id])
    elif tr_signal == 'missing' and missingFlag == 1:
        print('missing 2 elements')
        UL[tr_MS_id].append(-95)
        print('our list is: ', UL[tr_MS_id])
    elif (tr_signal!='missing'):
        missingFlag=0
        print('Flag: ',missingFlag)

# averageSignalDL takes a list with at least 4 signal values and returns average from last 4 elements of the list.
# for DL dictionary
def averageSignalDL(terminalID):
    result = round(sum(DL[terminalID], (-4)) / 4)
    return result


# averageSignalUL takes a list with at least 4 signal values and returns average from last 4 elements of the list.
# for UL dictionary
def averageSignalUL(terminalID):
    result = round(sum(UL[terminalID], (-4)) / 4)
    return result


# append_to_dictionary appends a new value to chosen dictionary[key]
def append_to_dictionary(input_list):
    global DL
    global UL
    if input_list[0] == 'DL':
        if input_list[2] not in DL.keys():
            ms = input_list[2]
            val = int(input_list[3])
            DL[ms] = [val]
        else:
            ms = input_list[2]
            val = int(input_list[3])
            DL[ms].append(val)
    elif input_list[0] == 'UL':
        if input_list[2] not in UL.keys():
            ms = input_list[2]
            val = int(input_list[3])
            UL[ms] = [val]
        else:
            ms = input_list[2]
            val = int(input_list[3])
            UL[ms].append(val)


# decision function evaluates which subfunction (nochange(), increase() or decrease()) has to be called based on given average
def decision(average):
    if average <= -70 and average >= -80:
        nochange()
    elif average < -80:
        increase(average)
    elif average > -70:
        decrease(average)


# increase function prints command with value to increase based on given average
def increase(average):
    difference = round(abs(average + 75))
    if difference < 8:
        print("%s S0 %s INC %s" % (tr_dir, tr_MS_id, difference))
    else:
        print("%s S0 %s INC 8" % (tr_dir, tr_MS_id))


# decrease function prints command with value to decrease based on given average
def decrease(average):
    difference = round(abs(average + 75))
    if difference < 4:
        print("%s S0 %s DEC %s" % (tr_dir, tr_MS_id, difference))
    else:
        print("%s S0 %s DEC 4" % (tr_dir, tr_MS_id))


# nochange function prints nochange command
def nochange():
    print("%s S0 %s NCH" % (tr_dir, tr_MS_id))


# VARIABLES AND DICTIONARIES

# initialization of empty dictionaries
DL = {}
UL = {}
# initialization of empty missingFlag variable
missingFlag = 0
# initialization of 2 variables containing patters used in input validation
mobile_station_pattern = re.compile("^MS\d\d\d$")
cell_id_pattern = re.compile('^N\d$')

# main loop
while True:

    user_input = input(
        'Put here following data, separated by two spaces:\n  DL/UL  Cell ID(S0/N1,N2 etc.)  Mobile Station ID(MS***)  dB  quality\n >')
    input_list = user_input.split('  ')

    if len(input_list) in [4, 5]:
        tr_dir = input_list[0]
    tr_cell_id = input_list[1]
    tr_MS_id = input_list[2]
    if input_list[3] == 'missing':
        tr_signal = input_list[3]
    else:
        tr_signal = int(input_list[3])
    if len(input_list) == 5:
        tr_quality = input_list[4]

    try:

        if tr_dir == 'DL' and tr_cell_id == 'S0' and mobile_station_pattern.match(tr_MS_id) \
                and ((int(tr_signal) <= -45 and int(tr_signal) >= -95) or tr_signal == 'missing') \
                and int(tr_quality) >= 0 and int(tr_quality) <= 5:
            missingDL()
            append_to_dictionary(input_list)
            if len(DL[tr_MS_id]) >= 4:
                average_temp = averageSignalDL(tr_MS_id)
                print('Average signal: ', average_temp)
                decision(average_temp)
                continue
            else:
                print('Not enough input measurements')
                continue

        elif tr_dir == 'UL' and tr_cell_id == 'S0' and mobile_station_pattern.match(tr_MS_id) \
                and ((int(tr_signal) <= -45 and int(tr_signal) >= -95) or tr_signal == 'missing') \
                and int(tr_quality) >= 0 and int(tr_quality) <= 5:
            append_to_dictionary(input_list)
            if len(UL[tr_MS_id]) >= 4:
                average_temp = averageSignalUL(tr_MS_id)
                print('Average signal: ', average_temp)
                decision(average_temp)
                continue
            else:
                print('Not enough input measurements')
                continue

        elif cell_id_pattern.match(tr_cell_id):
            print('\n', end='')
            continue

        else:
            print('\nPlease provide correct input\n')
            continue

    except:
        pass

    else:
        print('\nPlease provide correct input\n')
        continue
