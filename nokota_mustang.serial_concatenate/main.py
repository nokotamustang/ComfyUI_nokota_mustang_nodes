
delimiters = ["new line", "space", "period and space", "none"]


def concat(a: str, b: str, mode: str) -> str:
    if mode == "new line":
        return a + "\n" + b
    if mode == "period and space":
        return a + ". " + b
    if mode == "space":
        return a + " " + b
    return a + "" + b


class Node:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_a": ("STRING", {"default": ""}),
                "input_b": ("STRING", {"default": ""}),
                "input_c": ("STRING", {"default": ""}),
                "input_d": ("STRING", {"default": ""}),
                "input_e": ("STRING", {"default": ""}),
                "delim": (delimiters, {"default": "new line"}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "run_node"
    CATEGORY = "NokotaMustang"
    OUTPUT_NODE = True

    def run_node(self, input_a="", input_b="", input_c="", input_d="", input_e="", delim="new line"):
        result = ""
        if input_a is not "":
            result = input_a
        if input_b is not "":
            result = concat(result, input_b, delim)
        if input_c is not "":
            result = concat(result, input_c, delim)
        if input_d is not "":
            result = concat(result, input_d, delim)
        if input_e is not "":
            result = concat(result, input_e, delim)
        return {
            "ui": {
                "result": (f"{result}",)
            },
            "result": (result,)
        }
