import ipaddress

ip = '192.168.0.0/24'  # é possivel testar para diferentes redes

rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(ip)

endereco = ipaddress.ip_address(ip)

print(endereco + 57)
