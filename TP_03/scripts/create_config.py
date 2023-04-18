import json
from jinja2 import Template, Environment,  FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))


def load_json_data_from_file(file_path):
    pass

def render_network_config(template_name, data):
    pass

def save_built_config(file_name, data):
    pass


def create_config_cpe_lyon_batA():
    pass


def create_config_cpe_lyon_batB():
    pass
    
if __name__ == "__main__":
    """
        process question 3 to 5:
    """
    #question 3:
    #config = create_config_cpe_lyon_batA()

    #question 4:
    # save_built_config('config/R1_CPE_LYON_BAT_A.conf', config.get('r1'))
    # save_built_config('config/R2_CPE_LYON_BAT_A.conf', config.get('r2'))
    # save_built_config('config/ESW1_CPE_LYON_BAT_A.conf', config.get('esw1'))

    #question 5:
    # config = create_config_cpe_lyon_batB()
    # save_built_config('config/R1_CPE_LYON_BAT_B.conf', config.get('r1'))
    # save_built_config('config/R2_CPE_LYON_BAT_B.conf', config.get('r2'))
    # save_built_config('config/ESW1_CPE_LYON_BAT_B.conf', config.get('esw1'))
    