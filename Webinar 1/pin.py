pin = "0034"

# for i in range(0, 10000):
#     i = str(i)
    
#     if len(i) == 1:
#         i = "000" + str(i)
#     if len(i) == 2:
#         i = "00" + str(i)
#     if len(i) == 3:
#         i = "0" + str(i)
    
#     if i == pin:
#         print(i)
        
        
plen = len(pin)
for i in range(0, 10**plen):
    i = str(i)
    
    if len(i) < plen:
        i = "0" * (plen - len(i)) + i
    
    if i == pin:
        print(i)