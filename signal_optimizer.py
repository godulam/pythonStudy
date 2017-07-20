import re

# FUNCTIONS

'''
if len(tr_dir[tr_MS_id])>=4:
       average=averageSignal(tr_dir,tr_MS_id)
       print('Average signal: ',average)
else:
       print('Not enough input measurements')
'''

'''
def missing():
   if (tr_signal=='missing') and (missingFlag==0):
       missingFlag = 1

       tr_dir[tr_MS_id].append(tr_dir[tr_MS_id][-1])
#weź -1 element z listy i append
       print('our list is: ', DL)

       print('missing 1 element')

   elif (tr_signal == 'missing') & (missingFlag == 1):
       print('missing 2 elements')
#append -95 dB
       tr_dir[tr_MS_id].append(-95)
       print('our list is: ', DL)

   elif (tr_signal!='missing'):
       missingFlag=0
       print('Flag:  ',missingFlag)
'''

def averageSignalDL(terminalID):
   result=sum(DL[terminalID],(-4))/4
   return result

def averageSignalUL(terminalID):
   result=sum(UL[terminalID],(-4))/4
   return result

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



def decision(average):
   if average < -70 and average > -80:
       nochange()
   elif average < -80:
       increase(average)
   elif average > -70:
       decrease(average)


def increase(average):
   difference = abs(average + 75)
   if difference < 8:
       print("%s S0 %s INC %s" % (tr_dir, tr_MS_id, difference))
   else:
       print("%s S0 %s INC 8" % (tr_dir, tr_MS_id))


def decrease(average):
   difference = abs(average + 75)
   if difference < 4:
       print("%s S0 %s DEC %s" % (tr_dir, tr_MS_id, difference))
   else:
       print("%s S0 %s DEC 4" % (tr_dir, tr_MS_id))


def nochange():
   print("%s S0 %s NCH" % (tr_dir, tr_MS_id))

# VARIABLES AND DICTIONARIES

DL = {}
UL = {}
missingFlag= 0
mobile_station_pattern = re.compile("^MS\d\d\d$")
cell_id_pattern = re.compile('^N\d$')

while True:

   user_input = input('Put here following data, separated by two spaces:\n  DL/UL  Cell ID(S0/N1,N2 etc.)  Mobile Station ID(MS***)  dB  quality\n >')
   input_list = user_input.split('  ')

   if len(input_list) in [4, 5]:
       tr_dir = input_list[0]
       tr_cell_id = input_list[1]
       tr_MS_id = input_list[2]
       tr_signal = int(input_list[3])
       if len(input_list) == 5:
           tr_quality = input_list[4]

       try:

           if tr_dir == 'DL' and tr_cell_id == 'S0' and mobile_station_pattern.match(tr_MS_id) and ((int(
                   tr_signal) <= -45 and int(tr_signal) >= -95) or tr_signal=='missing') and int(tr_quality) >= 0 and int(tr_quality) <= 5:
               append_to_dictionary(input_list)
               if len(DL[tr_MS_id])>=4:
                   average_temp=averageSignalDL(tr_MS_id)
                   print('Average signal: ',average_temp)
                   decision(average_temp)
                   continue
               else:
                   print('Not enough input measurements')
                   continue

           elif tr_dir == 'UL' and tr_cell_id == 'S0' and mobile_station_pattern.match(tr_MS_id) and ((int(
                   tr_signal) <= -45 and int(tr_signal) >= -95) or tr_signal=='missing') and int(tr_quality) >= 0 and int(tr_quality) <= 5:
               append_to_dictionary(input_list)
               if len(UL[tr_MS_id])>=4:
                   average_temp=averageSignalUL(tr_MS_id)
                   print('Average signal: ',average_temp)
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
