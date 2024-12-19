# Terraform GCP VM Provisioner

Este proyecto automatiza la creación de máquinas virtuales en Google Cloud Platform (GCP) utilizando Terraform y Python. Permite configurar y desplegar instancias de VM a través de un archivo YAML de configuración.

## Requisitos Previos

- Docker y Docker Compose
- Cuenta de GCP
- Credenciales de GCP (archivo JSON de cuenta de servicio)

## Estructura del Proyecto

    .
    ├── credentials/              # Directorio para credenciales GCP
    │   └── gcp-credentials.json  # Archivo de credenciales (no incluido en git)
    ├── src/
    │   ├── main.py              # Script principal
    │   ├── terraform/           # Configuración de Terraform
    │   │   ├── main.tf          # Definición de recursos
    │   │   └── terraform.tfvars # Variables de Terraform (generado)
    │   └── utils/
    │       └── yaml_parser.py   # Utilidad para parsear YAML
    ├── config.example.yaml      # Ejemplo de configuración
    ├── config.yaml              # Configuración real (no incluido en git)
    ├── docker-compose.yml       # Configuración de Docker Compose
    └── .gitignore              # Archivos ignorados por git

## Configuración Inicial

1. **Configuración de GCP**:
   - Crear una cuenta de servicio en GCP con permisos de Compute Admin
   - Descargar el archivo JSON de credenciales
   - Colocar el archivo en `credentials/gcp-credentials.json`
   ```bash
   mkdir -p credentials
   mv ~/Downloads/[archivo-credenciales].json credentials/gcp-credentials.json
   chmod 600 credentials/gcp-credentials.json
   ```

2. **Configuración del Proyecto**:
   - Copiar el archivo de configuración de ejemplo
   ```bash
   cp config.example.yaml config.yaml
   ```
   - Editar `config.yaml` con tus valores:
   ```yaml
   project_id: "tu-proyecto-gcp"
   region: "us-central1"
   zone: "us-central1-a"
   name: "nombre-de-tu-vm"
   machine_type: "e2-medium"
   ```

## Uso

1. **Iniciar el Contenedor**:
   ```bash
   docker-compose up
   ```

2. **Verificar la Configuración**:
   - Asegurarse de que las credenciales estén montadas correctamente
   - Verificar que config.yaml tenga los valores correctos

## Especificaciones de la VM

- **Sistema Operativo**: Ubuntu 20.04 LTS
- **Red**: Default network con IP efímera pública
- **Disco**: Disco de arranque estándar

## Validaciones

El script valida automáticamente:
- Existencia de campos requeridos en config.yaml
- Presencia del archivo de credenciales
- Ejecución correcta de comandos Terraform

## Seguridad

- Las credenciales y configuraciones sensibles están excluidas de git
- Los archivos de credenciales requieren permisos 600
- Se utiliza la red default de GCP con IP efímera

## Solución de Problemas

1. **Error de Credenciales**:
   - Verificar que el archivo existe en credentials/gcp-credentials.json
   - Comprobar los permisos del archivo
   - Asegurar que el montaje en Docker está correcto

2. **Error de Configuración**:
   - Validar el formato del archivo config.yaml
   - Verificar que todos los campos requeridos estén presentes

3. **Error de Terraform**:
   - Revisar los logs de terraform init/apply
   - Verificar la conectividad con GCP