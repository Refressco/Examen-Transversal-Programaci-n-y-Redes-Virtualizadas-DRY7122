# sitio_login.py

import sqlite3
import bcrypt
from flask import Flask, request, redirect, render_template_string

# Inicializa Flask
app = Flask(__name__)

# Configura DB
DB_NAME = 'usuarios.db'

# Crea tabla si no existe
def crear_tabla():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            clave_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Agrega usuarios (una vez)
def insertar_usuarios():
    usuarios = [
        {"nombre": "Carlos", "clave": "Duoc.2025"},
        {"nombre": "Maria", "clave": "Duoc.2026"},
        {"nombre": "Francisco", "clave": "Duoc.2027"},
        {"nombre": "Sebastian", "clave": "Duoc.2028"}
    ]

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for user in usuarios:
        hash_pw = bcrypt.hashpw(user["clave"].encode('utf-8'), bcrypt.gensalt())
        cursor.execute("INSERT INTO usuarios (nombre, clave_hash) VALUES (?, ?)", (user["nombre"], hash_pw))
    
    conn.commit()
    conn.close()

# Verifica login
def verificar_usuario(nombre, clave):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT clave_hash FROM usuarios WHERE nombre = ?", (nombre,))
    row = cursor.fetchone()
    conn.close()

    if row and bcrypt.checkpw(clave.encode('utf-8'), row[0]):
        return True
    return False

# HTML básico
login_html = '''
<!doctype html>
<title>Login Examen</title>
<h2>Login de Usuarios</h2>
<form method=post>
  Nombre: <input type=text name=nombre><br><br>
  Clave: <input type=password name=clave><br><br>
  <input type=submit value=Ingresar>
</form>
<p>{{ mensaje }}</p>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        clave = request.form['clave']
        if verificar_usuario(nombre, clave):
            mensaje = f"Bienvenido, {nombre} ✅"
        else:
            mensaje = "Usuario o clave incorrectos ❌"
    return render_template_string(login_html, mensaje=mensaje)

# Inicialización
if __name__ == '__main__':
    crear_tabla()
    # SOLO ejecuta la siguiente línea UNA vez (o comenta después de la primera ejecución)
    insertar_usuarios()
    app.run(host='0.0.0.0', port=5800)

