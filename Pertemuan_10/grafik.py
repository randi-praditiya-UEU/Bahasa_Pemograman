#%%
import matplotlib.pyplot as plt

y = [2990, 2710, 2540, 3300, 2000]
x = [18, 19, 20, 21, 22]
plt.plot(x, y)

plt.xlabel('Tanggal (Januari)')
plt.ylabel('Harga')

plt.title('Harga Beras')
plt.grid(True)

plt.show()
# %%
