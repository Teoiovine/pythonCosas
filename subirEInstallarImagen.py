#Importar librerias

from paramiko import SSHClient, AutoAddPolicy
from getpass import getpass
from scp import SCPClient

#Declaracion de variables
#Para hacer: Poder cambiar el puerto y agregar llave. No me interesa ahora.
host = input("Nombre o IP: ")
username = input("Usuario: ")
password = getpass("Contraseña: ")
port = 22
key = None

#Conexion SSH necesaria para el SCP
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(host, port, username, password, key, timeout=4)

#Hace la transferencia
#with es un metodo de Python. No se muy bien que es, pero hace todo mas prolijo
#Para hacer: ver como decidir el tema de los directorios y archivos
with SCPClient(ssh.get_transport()) as scp:
	scp.put("/mnt/c/Users/tiovine/Documents/f5/Imagenes/BIGIP-14.1.2.3-0.0.5.iso", remote_path="/shared/images/BIGIP-14.1.2.3-0.0.5.iso")