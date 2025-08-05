from netmiko import ConnectHandler

#  Información del dispositivo
device = {
    'device_type': 'cisco_ios', 
    'host':   '169.254.288.9',
    'username': 'msaurez',
    'password': 'M@rpas013*',
    'port' : 22,
}

#  Comandos de configuración
commands = [
    'interface Ethernet 2',
    'switchport mode access',
    'switchport access vlan 10',
    'end',
    'wr' 
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