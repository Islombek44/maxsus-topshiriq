# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ltgY0n1wrlJpphE06_ybSnOrXI3gdllT
"""

import numpy as np
import matplotlib.pyplot as plt

# Sinus funksiyasining grafigini chizish
# X o'qi uchun nuqtalarni yaratish
x = np.linspace(0, 2 * np.pi, 100)  # 0 dan 2pi gacha 100 ta nuqta
y = np.sin(x)  # Sinus funksiyasi

# Grafikni chizish
plt.figure(figsize=(10, 6))  # Grafik o'lchamini sozlash
plt.plot(x, y, label='Sinus funksiyasi')  # X va Y nuqtalarini chizish
plt.title('Sinus Funktsiyasining Grafigi')  # Sarlavha qo'yish
plt.xlabel('X')  # X o'qi nomi
plt.ylabel('Y')  # Y o'qi nomi
plt.grid(True)  # Tarmoq chizish
plt.legend()  # Eslatma qo'yish
plt.show()

# Tasodifiy nuqtalar scatter grafigini chizish
# Tasodifiy nuqtalar yaratish
x_random = np.random.rand(50)  # 50 ta tasodifiy nuqta X o'qi uchun
y_random = np.random.rand(50)  # 50 ta tasodifiy nuqta Y o'qi uchun

# Scatter grafikni chizish
plt.figure(figsize=(10, 6))  # Grafik o'lchamini sozlash
plt.scatter(x_random, y_random, color='red', label='Tasodifiy Nuqtalar')  # Scatter grafi chizish
plt.title('Tasodifiy Nuqtalar Scatter Grafigi')  # Sarlavha qo'yish
plt.xlabel('X')  # X o'qi nomi
plt.ylabel('Y')  # Y o'qi nomi
plt.grid(True)  # Tarmoq chizish
plt.legend()  # Eslatma qo'yish
plt.show()

from google.colab.patches import cv2_imshow
import cv2

# Fayllarni ro'yxatga olish
fayllar = ['picture.jpg', 'rasm.jpg', 'surat.jpg']

oq_qora_rasmlar = []  # Oq-qora rasmlar saqlanadigan ro'yxat

for fayl in fayllar:
    # Tasvirni o'qish
    rasm = cv2.imread(fayl)
    if rasm is None:
        print(f"Fayl topilmadi: {fayl}")
        continue

    # Oq-qora rangga o'zgartirish
    oq_qora = cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
    oq_qora_rasmlar.append(oq_qora)

# Barcha oq-qora rasmlarni birdaniga ko'rsatish
for idx, oq_qora_rasm in enumerate(oq_qora_rasmlar, start=1):
    print(f"Oq-qora {idx}-rasm:")
    cv2_imshow(oq_qora_rasm)

import pandas as pd

# Read the CSV file
file_path = "/content/WHO COVID-19 cases.csv"  # Replace with the actual file path
data = pd.read_csv(file_path)

# Display the first few rows of the data
print(data.head())

# Apply a filter (e.g., filter rows where 'Region' is 'Europe')
filtered_data = data[data['Continent'] == 'Europe']  # Replace 'Region' with your actual column name

# Display the filtered data
print(filtered_data)

# Optionally, save the filtered data to a new CSV file
filtered_data.to_csv("filtered_data.csv", index=False)