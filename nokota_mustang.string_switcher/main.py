
class Node:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "select": ("INT", {"default": 1, "min": 1, "max": 10}),
                "text_1": ("STRING", {"default": "", "multiline": True}),
                "text_2": ("STRING", {"default": "", "multiline": True}),
                "text_3": ("STRING", {"default": "", "multiline": True}),
                "text_4": ("STRING", {"default": "", "multiline": True}),
                "text_5": ("STRING", {"default": "", "multiline": True}),
                "text_6": ("STRING", {"default": "", "multiline": True}),
                "text_7": ("STRING", {"default": "", "multiline": True}),
                "text_8": ("STRING", {"default": "", "multiline": True}),
                "text_9": ("STRING", {"default": "", "multiline": True}),
                "text_10": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("selected_text",)
    FUNCTION = "run_node"
    CATEGORY = "NokotaMustang"
    OUTPUT_NODE = True

    def run_node(self, select, text_1="", text_2="", text_3="", text_4="", text_5="",
                 text_6="", text_7="", text_8="", text_9="", text_10="",):
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
        elif select == 6:
            selected_text = text_6
        elif select == 7:
            selected_text = text_7
        elif select == 8:
            selected_text = text_8
        elif select == 9:
            selected_text = text_9
        elif select == 10:
            selected_text = text_10
        return {
            "ui": {
                "result": (f"{selected_text}",)
            },
            "result": (selected_text,)
        }
