import psutil
import subprocess
import socket

def obtener_adaptadores_red():
    """Obtiene los nombres, estados, IPs, máscaras y VLAN de los adaptadores de red."""
    adaptadores = psutil.net_if_addrs()
    estados = {}
    
    # Ejecuta el comando de PowerShell para obtener los adaptadores
    resultado = subprocess.run(
        ["powershell", "-Command", "Get-NetAdapter | Select-Object Name, Status, ifIndex"],
        capture_output=True, text=True
    )
    
    lineas = resultado.stdout.splitlines()
    for linea in lineas[3:]:  # Ignorar las tres primeras lineas
        partes = linea.split()
        if len(partes) >= 3:
            nombre = ' '.join(partes[:-2])  # Espacios entre nombres
            estado = partes[-2]
            if_index = partes[-1]
            estados[nombre] = {'estado': estado, 'ip': None, 'mascara': None, 'vlan': None}

            # Obtener la IP y la máscara de subred
            if nombre in adaptadores:
                for direccion in adaptadores[nombre]:
                    if direccion.family == socket.AF_INET:
                        estados[nombre]['ip'] = direccion.address
                        estados[nombre]['mascara'] = direccion.netmask

            # Obtener la VLAN usando PowerShell
            resultado_vlan = subprocess.run(
                ["powershell", "-Command", f"Get-NetAdapterVlan -InterfaceIndex {if_index} | Select-Object -ExpandProperty VLANID"],
                capture_output=True, text=True
            )
            vlan_lineas = resultado_vlan.stdout.splitlines()
            if vlan_lineas:
                estados[nombre]['vlan'] = vlan_lineas[0].strip()

    return estados

if __name__ == "__main__":
    adaptadores = obtener_adaptadores_red()
    for adaptador, info in adaptadores.items():
        print(f"{adaptador}: Estado: {info['estado']}, IP: {info['ip']}, Máscara: {info['mascara']}, VLAN: {info['vlan']}")
