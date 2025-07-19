from .main import Node

NODE_CLASS_MAPPINGS = {
    "nokota_mustang.sampler_config": Node
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "nokota_mustang.sampler_config": "Sampler config"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
