from PIL import Image

def image_to_ansi(image_path, new_width, aspect):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening the image: {e}")
        return ""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * aspect)  # 縦横比を保持

    image = image.resize((new_width, new_height))
    image = image.convert('RGB')

    ansi_chars = '█'  # 埋めるために使用する文字
    ansi_img = []

    pixels = list(image.getdata())
    for i in range(0, len(pixels), new_width):
        for pixel in pixels[i:i+new_width]:
            brightness = sum(pixel) / (255 * 3)
            ansi_index = int(brightness * (len(ansi_chars) - 1))
            r, g, b = pixel
            # RGB値を直接指定して色を設定
            color = f'\x1b[38;2;{r};{g};{b}m'
            ansi_img.append(color + ansi_chars[ansi_index] + '\x1b[0m')
        ansi_img.append('\n')

    return ''.join(ansi_img)

def save_ansi_art(save_to, art):
    try:
        with open(save_to, "w") as file:
            file.write(art)
    except Exception as e:
        print(f"Error saving the file: {e}")

def load_ansi_art(load_by):
    try:
        with open(load_by, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error loading the file: {e}")
        return ""
    
def truecolor_to_256color(ansi_art):
    # True Colorから256色へのマッピング関数
    def rgb_to_ansi256(r, g, b):
        if r == g and g == b:
            if r < 8:
                return 16
            if r > 248:
                return 231
            return round(((r - 8) / 247) * 24) + 232
        return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)
    
    # ANSIエスケープシーケンスを探し、変換する
    import re
    pattern = re.compile(r'\x1b\[38;2;(\d+);(\d+);(\d+)m')
    
    def ansi_replacer(match):
        r, g, b = map(int, match.groups())
        ansi_color = rgb_to_ansi256(r, g, b)
        return f'\x1b[38;5;{ansi_color}m'
    
    return pattern.sub(ansi_replacer, ansi_art)

if __name__ == "__main__": # 画像を指定して実行する場合
    import argparse
    parser = argparse.ArgumentParser(description="Convert image to True Color ANSI art")
    parser.add_argument("image_path", help="Path to the image file") # 画像のパスを指定
    parser.add_argument("--size", type=int, default=150, help="Width of the output image") # 画像の幅を指定
    parser.add_argument("--aspect", type=float, default=0.5, help="Aspect ratio of the output image") # 画像の縦横比を指定
    parser.add_argument("--save", action="store_true", help="Save the output to a file") # ファイルに保存するかどうか
    parser.add_argument("--print", action="store_true", help="Print the output to the console") # コンソールに表示するかどうか
    args = parser.parse_args()
    ansi_result = image_to_ansi(args.image_path,args.size,args.aspect)
    if args.print:
        print(ansi_result) # ANSIアートをコンソールに出力する
    if args.save:
        save_ansi_art(args.image_path.split(".")[0]+".txt", ansi_result) # ANSIアートをファイルに保存する