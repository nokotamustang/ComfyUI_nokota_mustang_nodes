import random


class Node:

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "min_val": ("INT", {"default": 1, "min": 1, "max": 1125899906842624, "step": 1}),
                "max_val": ("INT", {"default": 1125899906842624, "min": 1, "max": 1125899906842624, "step": 1}),
                "lock": ("BOOLEAN", {"default": False}),
                "lock_val": ("INT", {"default": 0, "min": 0, "max": 1125899906842624, "step": 1}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("random_int",)
    FUNCTION = "run_node"
    CATEGORY = "NokotaMustang"
    OUTPUT_NODE = True

    def run_node(self, min_val, max_val, lock, lock_val):
        if min_val > max_val:
            raise ValueError("min. value must be less than or equal to max. value")

        if lock == True and lock_val != 0:
            locked_value = lock_val
        else:
            locked_value = random.randint(min_val, max_val)

        return {
            "ui": {
                "result": (f"{locked_value}",)
            },
            "result": (locked_value,)
        }

    @classmethod
    def IS_CHANGED(self, min_val, max_val, lock, lock_val):
        return float("NaN")
