from .main import Node
NODE_CLASS_MAPPINGS = {
    "nokota_mustang.serial_concatenate": Node
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "nokota_mustang.serial_concatenate": "Serial concatenate"
}
WEB_DIRECTORY = "./js"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
