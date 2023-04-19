import json
from jinja2 import Template, Environment,  FileSystemLoader

env = Environment(loader=FileSystemLoader("/home/cpe/Desktop/devnet/TP-02/templates"))

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


def create_vlan_config_cpe_marseille():
    r02_data= load_json_data_from_file(file_path='../data/R2.json')
    esw2_data = load_json_data_from_file(file_path='../data/ESW2.json')
    r02_config = render_network_config(template_name='vlan_router.j2',data=r02_data)
    ESW2_config = render_network_config(template_name="vlan_switch.j2",data=esw2_data)
    return r02_config,ESW2_config
    pass


def create_vlan_config_cpe_paris():
    r03_data = load_json_data_from_file(file_path='../data/R3.json')
    esw3_data = load_json_data_from_file(file_path='../data/ESW3.json')
    r03_config = render_network_config(template_name="vlan_router.j2",data=r03_data)
    esw3_config = render_network_config(template_name="vlan_switch.j2",data=esw3_data)
    return r03_config,esw3_config
    pass

def create_ospf(boucle):
    ospf_data = load_json_data_from_file(file_path='data/ospf_r0'+str(boucle)+'.json')
    ospf_config = render_network_config(template_name="ospf.j2",data=ospf_data)
    return ospf_config
if __name__ == "__main__":
    """
        process question 1 to 5:
    """
    #r02_config, esw2_config = create_vlan_config_cpe_marseille()
    #save_built_config('../config/vlan_R02.conf', r02_config)
    #save_built_config('../config/vlan_ESW2.conf', esw2_config)
    
    #r03_config, esw3_config = create_vlan_config_cpe_paris()
    #save_built_config('../config/vlan_R03.conf', r03_config)
    #save_built_config('../config/vlan_ESW3.conf', esw3_config)
    for i in range(1,4):
        save_built_config('config/ospf_R0'+str(i)+'.conf',data=create_ospf(i))
