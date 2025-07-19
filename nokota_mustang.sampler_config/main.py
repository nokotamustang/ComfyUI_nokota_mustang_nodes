
class Node:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "cfg": ("FLOAT", {"default": 5.0, "step": 0.05}),
                "steps": ("INT", {"default": 32}),
                "denoise": ("FLOAT", {"default": 1.0, "step": 0.05}),
                "upscale_cfg": ("FLOAT", {"default": 5.0, "step": 0.05}),
                "upscale_steps": ("INT", {"default": 23}),
                "upscale_denoise": ("FLOAT", {"default": 0.5, "step": 0.05}),
            }
        }
    RETURN_TYPES = ("FLOAT", "INT", "FLOAT", "FLOAT", "INT", "FLOAT",)
    RETURN_NAMES = ("cfg", "steps", "denoise", "upscale_cfg", "upscale_steps", "upscale_denoise",)
    FUNCTION = "run_node"
    CATEGORY = "NokotaMustang"
    OUTPUT_NODE = True

    def run_node(self, cfg, steps, denoise, upscale_cfg, upscale_steps, upscale_denoise):
        return (cfg, steps, denoise, upscale_cfg, upscale_steps, upscale_denoise,)
