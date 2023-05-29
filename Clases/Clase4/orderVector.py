import numpy as np

vector = np.zeros(5)

for i in range(len(vector)):
    vector[i]=input(f"Ingrese le valor #{i}: ")

for i in range(len(vector)):
    if i+1<len(vector):
        if vector[i]>vector[i+1]:
            vector[i]=vector[i+1]
            vector[i+1]=vector[i]

print(vector)
