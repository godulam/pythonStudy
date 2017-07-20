DL={'MS666':[5,4,3,2]}
tr_MS_id='MS666'

def averageSignal(terminalID):
   result=sum(DL[terminalID],(-4))/4
   return result

average_temp=averageSignal(tr_MS_id)

print(average_temp)
