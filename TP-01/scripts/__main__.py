import json
import yaml
from jinja2 import Template, Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("templates"))

def load_json_data_from_file(file_path):
    try :
        with open(file_path) as json_file:
            data = json.load(json_file)
            print(data)
    except FileNotFoundError:
        print("mauvais chemin spécifié")
    return data
    pass


def load_yaml_data_from_file(file_path):
    data = yaml.safe_load(open(file_path))
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


if __name__ == "__main__":


    #process R2
    #r2_data = load_json_data_from_file(file_path='data/R2.json')
    r2_data = load_yaml_data_from_file(file_path='data/R2.yaml')
    r2_config = render_network_config(template_name='R2.j2', data=r2_data)
    save_built_config('config/R2.conf', r2_config)

    #process ESW2
    esw2_data = load_json_data_from_file(file_path='data/ESW2.json')
    esw2_config = render_network_config(template_name='ESW2.j2', data=esw2_data)
    save_built_config('config/ESW2.conf', esw2_config)

    esw4_data = load_yaml_data_from_file(file_path='data/ESW4.yaml')
    esw4_config = render_network_config(template_name='ESW4.j2', data=esw4_data)
    save_built_config('config/ESW4.conf', esw4_config)

    pass