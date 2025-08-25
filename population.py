import matplotlib.pyplot as plt
import numpy as np
genders = ['Male','Female','Non-binary','Prefer Not to say']
counts = [50,60,5,3]
ages = np.random.normal(loc=30, scale=10,size=1000) # Mean age 30, std dev 10
plt.figure(figsize=(8,6))
plt.bar(genders,counts,color=['skyblue','lightcoral','lightgreen','gold'])
plt.xlabel('Gender')
plt.ylabel('count')
plt.title('Distribution of Genders in a population')
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.show()
plt.figure(figsize=(10,7))
plt.hist(ages, bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages in a Population')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
