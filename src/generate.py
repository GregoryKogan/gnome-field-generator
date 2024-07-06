from PIL import Image


TILE_SIZE = 64

TEXTURES = {
    0: 'water.jpeg',
    1: 'dirt.jpg',
    2: 'dirt.jpg',
    3: 'stone.jpg',
    4: 'tnt.jpg',
    5: 'sand.png',
    6: 'mole.png',
    7: 'portal.jpg',
    8: 'skeleton.jpeg',
}


def read_map(filename: str) -> list[list[int]]:
    with open(filename, "r", encoding='utf-8-sig') as f:
        return [[int(x) for x in line.split(';')] for line in f]


def main():
    map2d = read_map("src/assets/map.csv")

    img = Image.new("RGB", (len(map2d[0]) * TILE_SIZE, len(map2d) * TILE_SIZE), "white")

    for i in range(len(map2d)):
        for j in range(len(map2d[i])):
            tile = map2d[i][j]
            texture = Image.open(f"src/assets/textures/{TEXTURES[tile]}")
            texture = texture.resize((TILE_SIZE, TILE_SIZE))
            img.paste(texture, (j * TILE_SIZE, i * TILE_SIZE))

    with open("out/map.png", "wb") as out:
        img.save(out, "PNG")

if __name__ == "__main__":
    main()
