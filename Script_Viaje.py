# viaje_chile_argentina.py

import openrouteservice
from openrouteservice import convert
import sys

API_KEY = 'eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImYyY2FkZjFhYmNhMzRlZGE5NmJiNmRkNWIwZThjYjg1IiwiaCI6Im11cm11cjY0In0='
client = openrouteservice.Client(key=API_KEY)

ciudades_coord = {
    "santiago": (-70.6483, -33.4569),
    "valparaiso": (-71.6127, -33.0472),
    "concepcion": (-73.0514, -36.8201),
    "mendoza": (-68.8458, -32.8908),
    "buenos aires": (-58.3816, -34.6037),
    "cordoba": (-64.1888, -31.4201)
}

transportes = {
    "1": "driving-car",
    "2": "cycling-regular",
    "3": "foot-walking"
}

while True:
    print("\n--- Calculadora de viajes Chile - Argentina ---")
    print("Escriba 's' para salir en cualquier momento.")

    origen = input("Ciudad de Origen: ").lower()
    if origen == 's':
        print("¡Hasta luego!")
        break

    destino = input("Ciudad de Destino: ").lower()
    if destino == 's':
        print("¡Hasta luego!")
        break

    if origen not in ciudades_coord or destino not in ciudades_coord:
        print("Una de las ciudades no está en la lista.")
        print(f"Ciudades disponibles: {', '.join(ciudades_coord.keys())}")
        continue

    print("\nSeleccione medio de transporte:")
    print("1. Auto")
    print("2. Bicicleta")
    print("3. Caminando")

    transporte_opcion = input("Opción: ").strip()
    if transporte_opcion == 's':
        print("¡Hasta luego!")
        break

    if transporte_opcion not in transportes:
        print("Opción de transporte no válida.")
        continue

    modo = transportes[transporte_opcion]

    coords = (ciudades_coord[origen], ciudades_coord[destino])
    try:
        ruta = client.directions(coords, profile=modo, format='geojson')
        resumen = ruta['features'][0]['properties']['summary']
        distancia_km = resumen['distance'] / 1000
        distancia_mi = distancia_km * 0.621371
        duracion_min = resumen['duration'] / 60

        print(f"\n🔹 De {origen.title()} a {destino.title()}")
        print(f"• Distancia: {distancia_km:.2f} km | {distancia_mi:.2f} millas")
        print(f"• Duración estimada: {duracion_min:.1f} minutos")

        print("\n🧭 Narrativa del viaje:")
        pasos = ruta['features'][0]['properties']['segments'][0]['steps']
        for paso in pasos:
            print(f"- {paso['instruction']}")

    except Exception as e:
        print("Error al calcular la ruta:", e)

