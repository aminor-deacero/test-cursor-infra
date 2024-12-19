#!/usr/bin/env python3
import sys
import os
from utils.yaml_parser import parse_yaml_config
import subprocess

def validate_config(config):
    required_fields = ['project_id', 'region', 'zone', 'machine_type', 'name']
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field: {field}")

def generate_terraform_vars(config):
    """Genera el archivo terraform.tfvars basado en la configuración YAML"""
    vars_content = []
    for key, value in config.items():
        if isinstance(value, str):
            vars_content.append(f'{key} = "{value}"')
        else:
            vars_content.append(f'{key} = {value}')
    
    with open('src/terraform/terraform.tfvars', 'w') as f:
        f.write('\n'.join(vars_content))

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <config.yaml>")
        sys.exit(1)

    config_file = sys.argv[1]
    if not os.path.exists(config_file):
        print(f"Error: Config file {config_file} not found")
        sys.exit(1)

    try:
        config = parse_yaml_config(config_file)
        validate_config(config)
        generate_terraform_vars(config)
        
        subprocess.run(['terraform', 'init'], cwd='src/terraform', check=True)
        subprocess.run(['terraform', 'apply', '-auto-approve'], cwd='src/terraform', check=True)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 