
ratios = {
    "Square (1:1)": 1 / 1,
    "Portrait (2:3)": 2 / 3,
    "Landscape (3:2)": 3 / 2,
    "Portrait SD (3:4)": 3 / 4,
    "Landscape SD (4:3)": 1.33 / 1,
    "Portrait Large Format (4:5)": 4 / 5,
    "Landscape Large Format (5:4)": 5 / 4,
    "Portrait HD (9:16)": 9 / 16,
    "Landscape HD (16:9)": 16 / 9,
    "IMAX Portrait (1:1.43)": 1/1.43,
    "IMAX Landscape (1.43:1)": 1.43/1,
    "Landscape European Wide (1.66:1)": 1.66/1,
    "Portrait European Wide (1:1.66)": 1/1.66,
    "Landscape Standard Wide (1.85:1)": 1.85/1,
    "Portrait Standard Wide (1:1.85)": 1/1.85,
    "Landscape Cinemascope (2.35:1)": 2.35/1,
    "Portrait Cinemascope (1:2.35)": 1/2.35,
    "Landscape Anamorphic (2.39:1)": 2.39/1,
    "Portrait Anamorphic (1:2.39)": 1/2.39,
    "Landscape Golden Ratio (1.618:1)": 1.618 / 1,
    "Portrait Golden Ratio (1:1.618)": 1 / 1.618,
}

target_mega_pixels = {
    "0.5 million (SD base 512)":  512,
    "0.9 million (base 960 ~HD)":  960,
    "1 million (SDXL base 1024)":  1024,
    "2 million (base 1440 ~Full HD)":  1440,
    "4 million (SD2XL base 2048)":  2048,
    "8 million (base 2880 ~4k)":  2880,
    "16 million (SD4XL base 4096)":  4096,
    "33 million (base 5760 ~8k)":  5760,
}


def get_resolution(name: str = "Square (1:1)", target_pixels=1048576, center_point=1024) -> tuple:
    if name == None or name == "":
        return (1024, 1024)
    ratio = ratios[name]
    width = int(center_point * (ratio**0.5))
    height = int(target_pixels / width)
    width = width - (width % 8)
    height = height - (height % 8)
    return (width, height)


def get_pixel_count(name: str = "1 million (SDXL base 1024)") -> tuple:
    center_point = target_mega_pixels[name]
    target_pixels = int(center_point * center_point)
    return (target_pixels, center_point)


class Node:

    @classmethod
    def INPUT_TYPES(s):
        names = [k for k in ratios]
        targets = [k for k in target_mega_pixels]
        return {
            "required": {
                "dimension_name": (names, ),
                "target_mega_pixels": (targets, {"default": "1 million (SDXL base 1024)"}),
            }
        }
    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("result_w", "result_h",)
    FUNCTION = "run_node"
    CATEGORY = "NokotaMustang"
    OUTPUT_NODE = True

    def run_node(self, dimension_name, target_mega_pixels):
        if dimension_name not in ratios:
            raise ValueError(f"dimension {dimension_name} not recognized")
        if target_mega_pixels not in target_mega_pixels:
            raise ValueError(f"target pixels: {target_mega_pixels} not recognized")
        pixel_count = get_pixel_count(name=target_mega_pixels)
        dimension = get_resolution(name=dimension_name, target_pixels=pixel_count[0], center_point=pixel_count[1])
        return {"ui": {"result": (f"{dimension[0]} by {dimension[1]}",)}, "result": (dimension[0], dimension[1],)}
