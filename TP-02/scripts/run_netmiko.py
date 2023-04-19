import json
from netmiko import ConnectHandler


def question_9(net_connect):
    net_connect = ConnectHandler(**r01)
    print(getattr(net_connect))
    print(net_connect)
    pass

def question_10(net_connect):
    net_connect = ConnectHandler(**r01)
    commands = ['show ip int brief']
    output = net_connect.send_command(commands[0])
    print(output)
    pass

def question_11(net_connect):
    net_connect = ConnectHandler(**r01)
    output = net_connect.send_command('show ip int brief', use_textfsm=True)
    print(output)
    pass


def question_12(net_connect):
    net_connect = ConnectHandler(**r01)
    output = net_connect.send_command('show ip route', use_textfsm=True)
    print(output)
    pass

def question_13(net_connect):
    net_connect = ConnectHandler(**r01)
    output = net_connect.send_command('sh ip int brief', use_textfsm=True)
    print(output)
    # on récupère toutes les interfaces
    for interface in output:
        output = net_connect.send_command('sh ip int brief ' + interface['intf'])
        print(output)
    pass


def question_14(net_connect):
    net_connect = ConnectHandler(**r01)
    commands =[
        'int l0',
        'desc test loopback interface from netmiko',
        "ip addr 192.168.1.1 255.255.255.255"
    ]
    output = net_connect.send_config_set(commands)
    output = net_connect.save_config()
    pass


def question_15(net_connect):
    net_connect = ConnectHandler(**r01)
    commands =[
        'int l0',
        'no desc test loopback interface from netmiko',
        "no ip addr 192.168.1.1 255.255.255.255"
    ]
    output = net_connect.send_config_set(commands)
    output = net_connect.save_config()
    pass

def question_16(net_connect):
    net_connect = ConnectHandler(**r01)
    output = net_connect.send_config_from_file('../config/loopback_R01.conf')
    output=net_connect.save_config()
    pass


def question_17(net_connect):
    pass


def get_inventory():
    with open('../inventory/host.json') as f:
        host = json.load(f)
        print(host)
        return host
    pass


def question_20():
    inventaire = get_inventory()
    for materiel in inventaire :
        device_type = materiel['device_type']
        host = materiel['ip']
        username = materiel['username']
        password = materiel['password']
        materiel = { 'device_type': device_type, 'host': host, 'username': username, 'password': password }
        net_connect = ConnectHandler(**materiel)
        output = net_connect.send_command('show ip int brief gigabitEthernet 0/0.99')
        print(output)
    pass


def question_21():
    inventaire = get_inventory()
    for materiel in inventaire:
        name = materiel['hostname']
        dict = { 'device_type': materiel['device_type'], 'host': materiel['ip'], 
            'username': materiel['username'], 'password': materiel['password'] }
        net_connect = ConnectHandler(**dict)
        output = net_connect.send_config_from_file('../config/vlan_'+name+'.conf')
        output = net_connect.save_config()
    pass

if __name__ == "__main__":    
    r01 = {
        'device_type': 'cisco_ios',
        'host':   '172.16.100.126',
        'username': 'cisco',
        'password': 'cisco'
    }
    net_connect = ConnectHandler(**r01)
 

    #question_10(net_connect)
    #question_11(net_connect)
    #question_12(net_connect)
    #question_13(net_connect)
    #question_14(net_connect)
    #question_15(net_connect)
    #question_16(net_connect)
    #question_17(net_connect)
    # hosts = get_inventory()
    # print(hosts)
    #question_20()
    #question_21()