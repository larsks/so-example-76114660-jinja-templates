from importlib.metadata import files
import os
import yaml
from jinja2 import Environment, FileSystemLoader



def load_yaml_configs(dir: str = './dag_configs'):                                                                                                  
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            filepath = root + os.sep + name
            if filepath.endswith(("config.yaml", "config.yml")):
                r.append(os.path.join(root, name))

    for file in r:
       values = yaml.safe_load(open(file))
       # Load templates file from templates folder
       env = Environment(loader = FileSystemLoader('./templates'),   
       trim_blocks=True, lstrip_blocks=True)
       template = env.get_template('base_template.j2')

       file=open("./rendered_configs/"+values['dag_id']+"_dag"+".yaml", "w") 
       file.write(template.render(values))  
       file.close()


if __name__ == "__main__":

    load_yaml_configs()
