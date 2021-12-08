#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    joursensecondes = temps[0]*(3600*24)
    heuresensecondes = temps[1]*3600
    minutesensecondes = temps[2]*60
    secondes = temps[3]
    sommedessecondes = joursensecondes + heuresensecondes + minutesensecondes + secondes
    return sommedessecondes

temps = (3,22,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    temps[0] = temps // (3600*24)
    temps[1] =  (temps % (3600*24) // 24)
    temps[2] = (temps % (3600*24) % 24) // 60
    temps[3] = (temps % (3600*24) % 24) % 60
    return 
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")