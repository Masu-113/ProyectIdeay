import wmi

def cambiar_nombre_ethernet_windows(nombre_actual, nuevo_nombre):
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(ServiceName="Ethernet"):
        if interface.Description == nombre_actual:
            try:
                interface.Rename(NewName=nuevo_nombre)
                print(f"Nombre del puerto ethernet '{nombre_actual}' cambiado a '{nuevo_nombre}'")
                return True
            except Exception as e:
                print(f"Error al cambiar el nombre: {e}")
                return False
    print(f"No se encontro el puerto ethernet con nombre '{nombre_actual}'")
    return False

# Ejemplo de uso:
nombre_actual = "Ethernet2"
nuevo_nombre = "MiConexionEthernet"
cambiar_nombre_ethernet_windows(nombre_actual, nuevo_nombre)