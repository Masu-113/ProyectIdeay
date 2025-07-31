from netmiko import ConnectHandler

#  Información del dispositivo
device = {
    'device_type': 'cisco_ios',  #  O el tipo de dispositivo adecuado
    'host':   '169.254.288.9',
    'username': r'.\Administrador',
    'password': '1d3@y2022*',
    'port' : 22,          #  O el puerto SSH adecuado
}

#  Comandos de configuración
commands = [
    'interface Ethernet 2',
    'switchport mode access',
    'switchport access vlan 10',  #  Reemplaza 10 con la VLAN deseada
    'end',
    'wr' # Guardar cambios
]

try:
    #  Establecer conexión  
    with ConnectHandler(**device) as net_connect:
        print(f"Conectado a {device['host']}")

        #  Enviar comandos de configuración
        output = net_connect.send_config_set(commands)
        print(output)

        print("Cambios realizados y guardados exitosamente.")

except Exception as e:
    print(f"Error: {e}")