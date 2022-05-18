import time

#programa printa na msm linha 
#print escreve e \r volta e sobreescreve

for i in range(100):
    print(f"\r{i}",end='',flush=True)
    time.sleep(0.1)
