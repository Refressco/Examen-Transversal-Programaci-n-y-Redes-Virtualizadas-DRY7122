# vlan_checker.py
vlan = int(input("Ingrese el número de VLAN: "))

if 1 <= vlan <= 1005:
    print("VLAN pertenece al rango NORMAL.")
elif 1006 <= vlan <= 4094:
    print("VLAN pertenece al rango EXTENDIDO.")
else:
    print("Número de VLAN inválido.")

