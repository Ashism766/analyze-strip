import cv2
import json



mark = ["URO", "BIL", "KET", "BLD", "PRO", "NIT", "LEU", "GLU", "SG", "PH"]


def analyze_urine_strip(image_path):

    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    colors = {}
    height, width, _ = image_rgb.shape
    strip_width = width // 10

    for i in range(10):
        color_start = i * strip_width
        color_end = (i + 1) * strip_width
        color_strip = image_rgb[:, color_start:color_end, :]
        average_color = color_strip.mean(axis=(0, 1)).astype(int)
        colors[mark[i]] = average_color.tolist()

    color_json = json.dumps(colors)

    return color_json
