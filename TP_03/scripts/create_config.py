import json
from jinja2 import Template, Environment,  FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))


def load_json_data_from_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        print(data)
    return data
    pass

def render_network_config(template_name, data):
    template = env.get_template(template_name)
    return template.render(data)
    pass

def save_built_config(file_name, data):
    with open(file_name,'w') as config_file:
        config_file.write(data)
    pass


def create_config_cpe_lyon_batA():
    R1_A=load_json_data_from_file('data/R1_CPE_LYON_BAT_A.json')
    R2_A=load_json_data_from_file('data/R2_CPE_LYON_BAT_A.json')
    ESW1_A=load_json_data_from_file('data/ESW1_CPE_LYON_BAT_A.json')
    R1_A_config_VLAN=render_network_config(template_name='vlan_router.j2',data=R1_A)
    R1_A_config_VRRP=render_network_config(template_name='vrrp_router.j2',data=R1_A)
    R1_A_config_OSPF=render_network_config(template_name='ospf_router.j2',data=R1_A)
    R1_A_config = [R1_A_config_VLAN,R1_A_config_VRRP,R1_A_config_OSPF]
    R1_A_config = ''.join(R1_A_config)
    R2_A_config_VLAN=render_network_config(template_name='vlan_router.j2',data=R2_A)
    R2_A_config_VRRP=render_network_config(template_name='vrrp_router.j2',data=R2_A)
    R2_A_config_OSPF=render_network_config(template_name='ospf_router.j2',data=R2_A)
    R2_A_config = [R2_A_config_VLAN,R2_A_config_VRRP,R2_A_config_OSPF]
    R2_A_config = ''.join(R2_A_config)
    print(R2_A_config)
    ESW1_A_config=render_network_config(template_name='vlan_switch.j2',data=ESW1_A)
    return {'r1':R1_A_config,'r2':R2_A_config,'esw1':ESW1_A_config}
    pass


def create_config_cpe_lyon_batB():
    R1_B=load_json_data_from_file('data/R1_CPE_LYON_BAT_B.json')
    R2_B=load_json_data_from_file('data/R2_CPE_LYON_BAT_B.json')
    ESW1_B=load_json_data_from_file('data/ESW1_CPE_LYON_BAT_B.json')
    R1_B_config_VLAN=render_network_config(template_name='vlan_router.j2',data=R1_B)
    R1_B_config_VRRP=render_network_config(template_name='vrrp_router.j2',data=R1_B)
    R1_B_config_OSPF=render_network_config(template_name='ospf_router.j2',data=R1_B)
    R1_B_config = [R1_B_config_VLAN,R1_B_config_VRRP,R1_B_config_OSPF]
    R1_B_config = ''.join(R1_B_config)
    print(R1_B_config)
    R2_B_config_VLAN=render_network_config(template_name='vlan_router.j2',data=R2_B)
    R2_B_config_VRRP=render_network_config(template_name='vrrp_router.j2',data=R2_B)
    R2_B_config_OSPF=render_network_config(template_name='ospf_router.j2',data=R2_B)
    R2_B_config = [R2_B_config_VLAN,R2_B_config_VRRP,R2_B_config_OSPF]
    R2_B_config = ''.join(R2_B_config)
    print(R2_B_config)
    ESW1_B_config=render_network_config(template_name='vlan_switch.j2',data=ESW1_B)
    return {'r1':R1_B_config,'r2':R2_B_config,'esw1':ESW1_B_config}
    pass
    
if __name__ == "__main__":
    """
        process question 3 to 5:
    """
    #question 3:
    config = create_config_cpe_lyon_batA()

    #question 4:
    save_built_config('config/R1_CPE_LYON_BAT_A.conf', config.get('r1'))
    save_built_config('config/R2_CPE_LYON_BAT_A.conf', config.get('r2'))
    save_built_config('config/ESW1_CPE_LYON_BAT_A.conf', config.get('esw1'))

    #question 5:
    config = create_config_cpe_lyon_batB()
    save_built_config('config/R1_CPE_LYON_BAT_B.conf', config.get('r1'))
    save_built_config('config/R2_CPE_LYON_BAT_B.conf', config.get('r2'))
    save_built_config('config/ESW1_CPE_LYON_BAT_B.conf', config.get('esw1'))
    