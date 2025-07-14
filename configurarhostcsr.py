# config_netconf.py

from ncclient import manager

router = {
    "host": "192.168.56.102",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!"
}

# Cambiar nombre de host y crear Loopback 11
config_data = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Hernandez-Duran-Olivares-Contreras</hostname>
    <interface>
      <Loopback>
        <name>11</name>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

def aplicar_config():
    with manager.connect(host=router["host"],
                         port=router["port"],
                         username=router["username"],
                         password=router["password"],
                         hostkey_verify=False,
                         device_params={"name": "csr"},
                         look_for_keys=False,
                         allow_agent=False) as m:
        respuesta = m.edit_config(target="running", config=config_data)
        print(respuesta)

if __name__ == "__main__":
    aplicar_config()

