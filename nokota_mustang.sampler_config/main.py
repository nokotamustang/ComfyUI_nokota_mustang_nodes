
class Node:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "cfg": ("FLOAT", {"default": 6.0, "min": 0.05, "max": 20.0, "step": 0.05}),
                "steps": ("INT", {"default": 32, "min": 1, "max": 200, "step": 1}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.05, "max": 2.0, "step": 0.05}),
                "upscale_cfg": ("FLOAT", {"default": 6.0, "min": 0.05, "max": 20.0, "step": 0.05}),
                "upscale_steps": ("INT", {"default": 23, "min": 1, "max": 200, "step": 1}),
                "upscale_denoise": ("FLOAT", {"default": 0.5, "min": 0.05, "max": 2.0, "step": 0.05}),
            }
        }
    RETURN_TYPES = ("FLOAT", "INT", "FLOAT", "FLOAT", "INT", "FLOAT",)
    RETURN_NAMES = ("cfg", "steps", "denoise", "upscale_cfg", "upscale_steps", "upscale_denoise",)
    FUNCTION = "run_node"
    CATEGORY = "NokotaMustang"
    OUTPUT_NODE = True

    def run_node(self, cfg, steps, denoise, upscale_cfg, upscale_steps, upscale_denoise):
        return (cfg, steps, denoise, upscale_cfg, upscale_steps, upscale_denoise,)
