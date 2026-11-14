height_cm="175"
weight_kg="68.5"
height_m=int(height_cm) / 100
weight=float(weight_kg)
bmi=weight / (height_m * height_m)
print("BMI:",bmi)