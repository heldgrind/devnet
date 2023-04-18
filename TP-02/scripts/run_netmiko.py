import json
from netmiko import ConnectHandler


def question_9(net_connect):
    pass

def question_10(net_connect):
    pass

def question_11(net_connect):
    pass


def question_12(net_connect):
    pass

def question_13(net_connect):
    pass


def question_14(net_connect):
    pass


def question_15(net_connect):
    pass

def question_16(net_connect):
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
    pass


def question_21():
    pass

if __name__ == "__main__":    
    r01 = {
        'device_type': 'cisco_ios',
        'host':   '172.16.100.126',
        'username': 'cisco',
        'password': 'cisco'
    }
    inventaire = get_inventory()
    for materiel in inventaire:
        name = materiel['hostname']
        dict = { 'device_type': materiel['device_type'], 'host': materiel['ip'], 
            'username': materiel['username'], 'password': materiel['password'] }
        net_connect = ConnectHandler(**dict)
        output = net_connect.send_config_from_file('../config/vlan_'+name+'.conf')
        output = net_connect.save_config()

    #question_9(net_connect)
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