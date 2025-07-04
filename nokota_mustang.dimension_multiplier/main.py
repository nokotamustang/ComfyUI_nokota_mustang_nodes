
class Node:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "w": ("INT,FLOAT", {"default": 1.0, "step": 0.05}),
                "h": ("INT,FLOAT", {"default": 1.0, "step": 0.05}),
                "multiplier": ("FLOAT", {"default": 2.0, "step": 0.05})
            }
        }
    RETURN_TYPES = ("INT,FLOAT", "INT,FLOAT",)
    RETURN_NAMES = ("result_w", "result_h",)
    FUNCTION = "run_node"
    CATEGORY = "NokotaMustang"
    OUTPUT_NODE = True

    def run_node(self, w, h, multiplier):
        if isinstance(w, int):
            result_w = float(w) * multiplier
        elif isinstance(w, float):
            result_w = w * multiplier
        if isinstance(h, int):
            result_h = float(h) * multiplier
        elif isinstance(h, float):
            result_h = h * multiplier
        result_w = int(result_w - (result_w % 8))
        result_h = int(result_h - (result_h % 8))
        return {"ui": {"result": (f"{result_w} by {result_h}",)}, "result": (result_w, result_h,)}
