from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get,napalm_configure, napalm_cli
from nornir_netmiko.tasks import netmiko_send_config,netmiko_send_command, netmiko_save_config, netmiko_commit


def hello_world(task: Task) -> Result:
    return Result(
    host=task.host,
    result=f"{task.host.name} says hello world!"
    )
def save (task: Task) -> Result:
    r = task.run(napalm_cli, commands=["wr"])
    return Result(
    host=task.host,
    result=r.result
    )

def state (task: Task) -> Result:
    r = task.run(netmiko_send_command, command_string="show ip int brief")
    return Result(
    host=task.host,
    result=r.result
    )



def question_13(nr):
    print(nr.__dict__)
    pass

def question_14(nr):
    host = nr.inventory.hosts
    print(host)
    print(type(host))
    pass

def question_15(nr):
    premier = nr.inventory.hosts['R1-CPE-BAT-B']
    print(premier)
    print(type(premier))
    pass

def question_16(nr):
    premier = nr.inventory.hosts['R1-CPE-BAT-B']
    print(dir(premier))
    name = premier.name
    password = premier.password
    ip = premier.hostname
    print(name)
    print(password)
    print(ip)
    pass

def question_17(nr):
    premier = nr.inventory.hosts['R1-CPE-BAT-B']
    print((premier.keys()))
    pass

def question_18(nr):
    premier = nr.inventory.hosts['R1-CPE-BAT-B']
    print(premier.__getitem__("room"))
    pass

def question_19(nr):
    premier = nr.inventory.hosts['R1-CPE-BAT-B']
    print(nr.inventory.groups)
    pass

def question_20(nr):
    premier = nr.inventory.hosts['R1-CPE-BAT-B']
    groupes = nr.inventory.hosts.get('R1-CPE-BAT-A').groups
    print(groupes)
    pass

def question_21(nr):
    premier = nr.inventory.hosts['R1-CPE-BAT-B']
    groupeskey = nr.inventory.hosts.get('R1-CPE-BAT-A').groups[0].keys()
    print(groupeskey)
    pass

def question_22(nr):
    premier = nr.inventory.hosts['R1-CPE-BAT-A']
    groupeskey = nr.inventory.hosts.get('R1-CPE-BAT-A').groups[0].get('vendor')
    print(groupeskey)
    pass

def question_23(nr):
    nr = InitNornir(config_file="inventory/config.yaml")
    hostname = nr.inventory.hosts
    for host in hostname:
        ip = nr.inventory.hosts.get(host).hostname
        print(ip) 
    pass

def question_24(nr):
    print(nr.filter(device_type="router").inventory.hosts.keys())
    pass

def question_25(nr):
    print(nr.filter(device_type="router_switch").inventory.hosts.keys())
    pass

def question_26(nr):
    result = nr.run(task=hello_world)
    print(result)
    pass

def question_27(nr):
    result = nr.run(task=hello_world)
    print(type(result))
    pass

def question_29(nr):
    result = nr.run(task=hello_world)
    print_result(result)
    pass

def question_30(nr):
    test_group = nr.filter(device_type="router_switch")
    result = test_group.run(task=hello_world)
    print_result(result)
    pass

def question_32(nr):
    test_group = nr.filter(device_type="router")
    result = test_group.run(task=napalm_get, getters=["arp_table"])
    pass
 
def question_33(nr):
    test_group = nr.filter(device_type="router_switch")
    result = test_group.run(task=napalm_get, getters=["arp_table"])
    print_result(result)
    pass

def question_34(nr):
    Router1_A = nr.filter(device_name="R1-CPE-BAT-A")
    result = Router1_A.run(task=napalm_configure, configuration="interface Loopback 1 \n ip address 1.1.1.1 255.255.255.255")
    print_result(result)
    Router2_A = nr.filter(device_name="R2-CPE-BAT-A")
    result = Router2_A.run(task=napalm_configure, configuration="interface Loopback 1 \n ip address 2.2.2.2 255.255.255.255")
    print_result(result)
    pass

def question_35(nr):
    result = nr.run(task=save)
    print_result(result)
    pass

def question_36(nr):
    result = nr.run(task=state)
    print_result(result)
    pass

def question_37(nr):
    Router1_A = nr.filter(device_name="R1-CPE-BAT-A")
    result = Router1_A.run(task=netmiko_send_config, config_commands=["interface Loopback 2","ip address 1.1.1.2 255.255.255.255"])
    print_result(result)
    Router2_A = nr.filter(device_name="R2-CPE-BAT-A")
    result = Router2_A.run(task=netmiko_send_config, config_commands=["interface Loopback 2","ip address 2.2.2.3 255.255.255.255"])
    print_result(result)
    pass

def question_38(nr):
    Router1_A = nr.filter(device_name="R1-CPE-BAT-A")
    result = Router1_A.run(task=netmiko_save_config)
    print_result(result)
    Router2_A = nr.filter(device_name="R2-CPE-BAT-A")
    result = Router2_A.run(task=netmiko_save_config)
    print_result(result)
    pass

def question_39(nr):
    hostname = nr.inventory.hosts
    for host in hostname:
        filter = nr.filter(device_name=host)
        result = filter.run(task=netmiko_send_config, config_commands=["ip scp server enable"])
    Router1_A = nr.filter(device_name="R1-CPE-BAT-A")
    with open("config/R1_CPE_LYON_BAT_A.conf") as f:
        config = f.read()
    result = Router1_A.run(task=napalm_configure, configuration=config)
    print_result(result)
    result = Router1_A.run(task=netmiko_save_config)
    print_result(result)
    Router2_A = nr.filter(device_name="R2-CPE-BAT-A")
    with open("config/R2_CPE_LYON_BAT_A.conf") as f:
        config = f.read()
    result = Router2_A.run(task=napalm_configure, configuration=config)
    print_result(result)
    result = Router2_A.run(task=netmiko_save_config)
    print_result(result)
    ESW1_A = nr.filter(device_name="ESW1-CPE-BAT-A")
    with open("config/ESW1_CPE_LYON_BAT_A.conf") as f:
        config = f.read()
    result = ESW1_A.run(task=napalm_configure, configuration=config)
    print_result(result)
    result = ESW1_A.run(task=netmiko_save_config)
    print_result(result)
    Router1_B = nr.filter(device_name="R1-CPE-BAT-B")
    with open("config/R1_CPE_LYON_BAT_B.conf") as f:
        config = f.read()
    result = Router1_B.run(task=napalm_configure, configuration=config)
    print_result(result)
    result = Router1_B.run(task=netmiko_save_config)
    print_result(result)
    Router2_B = nr.filter(device_name="R2-CPE-BAT-B")
    with open("config/R2_CPE_LYON_BAT_B.conf") as f:
        config = f.read()
    result = Router2_B.run(task=napalm_configure, configuration=config)
    print_result(result)
    result = Router2_B.run(task=netmiko_save_config)
    print_result(result)
    ESW1_B = nr.filter(device_name="ESW1-CPE-BAT-B")
    with open("config/ESW1_CPE_LYON_BAT_B.conf") as f:
        config = f.read()
    result = ESW1_B.run(task=napalm_configure, configuration=config)
    print_result(result)
    result = ESW1_B.run(task=netmiko_save_config)
    print_result(result)
    pass

def question_39_d(nr):
    
    pass

def question_40(nr):
    Router1_A = nr.filter(device_name="R1-CPE-BAT-A")
    with open("config/R1_CPE_LYON_BAT_A.conf") as f:
        config = f.read()
    result = Router1_A.run(task=napalm_configure, configuration=config)
    print_result(result)
    result = Router1_A.run(task=netmiko_save_config)
    print_result(result)
    Router2_A = nr.filter(device_name="R2-CPE-BAT-A")
    with open("config/R2_CPE_LYON_BAT_A.conf") as f:
        config = f.read()
    result = Router2_A.run(task=napalm_configure, configuration=config)
    print_result(result)
    result = Router2_A.run(task=netmiko_save_config)
    print_result(result)
    Router1_B = nr.filter(device_name="R1-CPE-BAT-B")
    with open("config/R1_CPE_LYON_BAT_B.conf") as f:
        config = f.read()
    result = Router1_B.run(task=napalm_configure, configuration=config)
    print_result(result)
    result = Router1_B.run(task=netmiko_save_config)
    print_result(result)
    Router2_B = nr.filter(device_name="R2-CPE-BAT-B")
    with open("config/R2_CPE_LYON_BAT_B.conf") as f:
        config = f.read()
    result = Router2_B.run(task=napalm_configure, configuration=config)
    print_result(result)
    result = Router2_B.run(task=netmiko_save_config)
    print_result(result)
    pass
    

if __name__ == "__main__":
    nr = InitNornir(config_file="inventory/config.yaml")

    #question_13(nr)
    #question_14(nr)
    #question_15(nr)
    #question_16(nr)
    #question_17(nr)
    #question_18(nr)
    #question_19(nr)
    #question_20(nr)
    #question_21(nr)
    #question_22(nr)
    #question_23(nr)
    #question_24(nr)
    #question_25(nr)
    #question_26(nr)
    #question_27(nr)
    #question_29(nr)
    #question_30(nr)

    #○question_32(nr)
    #question_33(nr)
    #question_34(nr)
    #question_35(nr)
    #question_36(nr)
    #question_37(nr)
    #question_38(nr)
    #question_39(nr)
    #question_39_d(nr)

    question_40(nr)
    pass
