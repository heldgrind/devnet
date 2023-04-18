import json
from napalm import get_network_driver


def get_inventory():
    with open('../inventory/host.json') as f:
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
    result= device.load_merge_candidate(config='/home/config/loopback_R01.conf')
    print(device.compare_config())
    device.commit_config()
    pass


def question_31():
    pass


def question_32():
    pass


def question_34():
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
    question_30(device)
    #question_31()
    #question_32()
    #question_34()