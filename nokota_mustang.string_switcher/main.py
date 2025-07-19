
class Node:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "select": ("INT", {"default": 1, "min": 1, "max": 5}),
                "text_1": ("STRING", {"default": "", "multiline": True}),
                "text_2": ("STRING", {"default": "", "multiline": True}),
                "text_3": ("STRING", {"default": "", "multiline": True}),
                "text_4": ("STRING", {"default": "", "multiline": True}),
                "text_5": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING",)
    RETURN_NAMES = ("selected_text", "text_1", "text_2", "text_3", "text_4", "text_5",)
    FUNCTION = "run_node"
    CATEGORY = "NokotaMustang"
    OUTPUT_NODE = True

    def run_node(self, select, text_1="", text_2="", text_3="", text_4="", text_5="",):
        if select == 1:
            selected_text = text_1
        elif select == 2:
            selected_text = text_2
        elif select == 3:
            selected_text = text_3
        elif select == 4:
            selected_text = text_4
        elif select == 5:
            selected_text = text_5
        return {
            "ui": {
                "result": (f"{select}: {selected_text}",)
            },
            "result": (selected_text, text_1, text_2, text_3, text_4, text_5,)
        }
