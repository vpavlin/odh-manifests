from jinja2 import Template, FileSystemLoader, Environment
import os
import pprint
import sys

def load_template(fname):
    template = None
    with open(fname, "r") as fp:
        template = fp.read()

    return template


def analyze_component(component_path):
    if not os.path.isdir(component_path):
        return None
    component_dir = os.listdir(component_path)
    components = []
    component_values = {'name': parse_name(component_path), 'components': components}
    direct_base = False
    if 'base' in component_dir:
        direct_base = True
        component_dir = [component_path]
    for sub_comp in component_dir:
        if direct_base and sub_comp == component_path:
            sub_comp_path = sub_comp
        else:
            sub_comp_path = os.path.join(component_path, sub_comp)

        if not os.path.isdir(sub_comp_path):
            continue
        component = {}
        component['path'] = sub_comp_path.strip("/")
        component['name'] = parse_name(sub_comp)
        component['kfdef_name'] = sub_comp_path.strip("/").replace("/", "-")
        component['parameters'] = analyze_parameters(os.path.join(sub_comp_path, "base", "params.env"))
        component['overlays'] = analyze_overlays(os.path.join(component_path, sub_comp, "overlays"))

        components.append(component)

    return component_values

def analyze_overlays(path):
    overlays = []
    if not os.path.exists(path):
        return overlays

    overlays_dir = os.listdir(path)
    for overlay in overlays_dir:
        overlay_dict = {}
        overlay_dict['name'] = overlay

        overlays.append(overlay_dict)

    return overlays

def analyze_parameters(path):
    params = []
    if not os.path.exists(path):
        return params
    with open(path, "r") as fp:
        params = fp.readlines()

    params = [{'name': param.split("=")[0]} for param in params]
    return params

def parse_name(path):
    return path.strip("/").split("/")[-1]

def template(values):
    file_loader = FileSystemLoader('scripts/templates')
    env = Environment(loader=file_loader)
    template = env.get_template('readme.md.j2')

    msg = template.render(values)
    return msg

def running_from_root():
    dir_content = os.listdir(os.getcwd())
    if ".git" in dir_content and "kfdef" in dir_content:
        return True
    else:
        return False

if __name__ == "__main__":
    if not running_from_root() or len(sys.argv) != 2:
        print("ERROR: Please run from root of odh-manifests as \n\t%s <component-dir>" % sys.argv[0])
        sys.exit(1)
 
    template_config = analyze_component(sys.argv[1])
    #pprint.pprint(template_config)
    if template_config:
        print(template(template_config))

