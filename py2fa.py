import pyotp

# Genera una clave secreta aleatoria para el usuario
secret = pyotp.random_base32()

# Crea una instancia del generador TOTP con la clave secreta
totp = pyotp.TOTP(secret, interval=30)

# Imprime la URL para generar códigos QR (puedes escanearlo con una app de autenticación como Google Authenticator)
print("Escanee el siguiente código QR en su app de autenticación:")
print(totp.provisioning_uri("usuario_ejemplo@dominio.com", issuer_name="Nombre_de_la_Aplicación"))

# Simula la verificación del código TOTP ingresado por el usuario
codigo_ingresado = input("Ingrese el código TOTP generado por la app de autenticación: ")

while codigo_ingresado:
    # Verifica si el código ingresado es correcto
    if totp.verify(codigo_ingresado, valid_window=1):
        print("La autenticación de doble factor ha sido exitosa.")
    else:
        print("El código TOTP ingresado no es válido. La autenticación ha fallado.")
    
    # Simula la verificación del código TOTP ingresado por el usuario
    codigo_ingresado = input("Ingrese el código TOTP generado por la app de autenticación: ")
