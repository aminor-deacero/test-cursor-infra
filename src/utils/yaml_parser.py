import yaml

def parse_yaml_config(config_file):
    """Parse YAML configuration file"""
    try:
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML file: {str(e)}")
    except Exception as e:
        raise Exception(f"Error reading config file: {str(e)}") 