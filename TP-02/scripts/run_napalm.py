import json
import re
from napalm import get_network_driver
from datetime import datetime
import os



def get_inventory():
    with open('inventory/host.json') as f:
        host = json.load(f)
        print(host)
        return host
    pass


def get_json_data_from_file(file):
    pass

def question_26(device):
    commands = ['show ip int brief']
    output = device.cli(commands)
    print(output)
    pass


def question_27(device):
    commands = ['show ip int brief']
    output = device.cli(commands)
    print(type(output))
    key_list = list(output.keys())
    print(key_list)
    pass


def question_28(device):
    output = device.get_arp_table()
    print(output)
    pass

def question_29(device):
    output = device.get_arp_table()
    print(type(output))
    pass


def question_30(device):
    with open('config/loopback_R01.conf') as f:
        fichier = f.read()
    device.load_merge_candidate(config=fichier)
    print(device.compare_config())
    device.commit_config()
    command = ["sh ip int brief"]
    output = device.cli(command)
    print(output)
    pass


def question_31():
    pass


def question_32():
    inventaire = get_inventory()
    i=1
    for materiel in inventaire :
        if re.match(r"R0*",materiel['hostname']):
            print(materiel['hostname'])
            hostname = materiel['ip']
            username = materiel['username']
            password = materiel['password']
            materiel= {'hostname':hostname,'username':username,'password':password}
            driver = get_network_driver('ios')
            routeur = driver(**materiel)
            routeur.open()
            with open('config/ospf_R0'+str(i)+'.conf') as f:
                fichier = f.read()
            routeur.load_merge_candidate(config=fichier)
            print(routeur.compare_config())
            routeur.commit_config()
            i += 1
        
    pass


def question_34():
    backup_folder= "config/backup/"
    inventaire = get_inventory()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    for materiel in inventaire:
        #on utilise get_config
        hostname = materiel['ip']
        username = materiel['username']
        password = materiel['password']
        materiel= {'hostname':hostname,'username':username,'password':password}
        driver = get_network_driver('ios')
        routeur = driver(**materiel)
        routeur.open()
        output = routeur.get_config()
        print(output)
        backup_filename = f"{hostname}_{timestamp}.txt"
        bakcup_path = os.path.join(backup_folder,backup_filename)
        
        with open(bakcup_path,'w') as f:
            f.write(output['running'])
                
 
    pass



if __name__ == "__main__":
    r01 = {
        'hostname':'172.16.100.126',
        'username': "cisco",
        'password': "cisco"
    }

    driver = get_network_driver('ios')
    device  = driver(**r01)
    device.open()
    
    #question_26(device)
    #question_27(device)
    #question_28(device)
    #question_29(device)
    #question_30(device)
    #question_31()
    question_32()
    #question_34()