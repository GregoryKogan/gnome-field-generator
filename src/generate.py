from PIL import Image
import json


TILE_SIZE = 64

TEXTURES = {
    0: "water2.png",
    1: "dirt2.png",
    2: "entrance.png",
    3: "stone2.png",
    4: "gas.png",
    5: "sand2.png",
    6: "mole3.png",
    7: "portal2.png",
    8: "vent.jpg",
    9: "portal2.png",
}


class Map:
    def __init__(self, filename: str):
        self.width = 0
        self.height = 0
        self.tiles = []
        self.walls = []
        self.read_map(filename)

    def read_map(self, filename: str):
        with open(filename, "r") as f:
            data = json.load(f)
            self.width = data["width"]
            self.height = data["height"]
            for i, tile in enumerate(data["tiles"]):
                self.tiles.append(tile["type"])
                for wall_i, wall in enumerate(tile["walls"]):
                    if wall:
                        self.walls.append((i, wall_i))


def main():
    map2d = Map("src/assets/map.json")

    img = Image.new(
        "RGBA", (map2d.width * TILE_SIZE, map2d.height * TILE_SIZE), (0, 0, 0, 0)
    )

    for i in range(map2d.height):
        for j in range(map2d.width):
            tile = map2d.tiles[i * map2d.width + j]
            texture = Image.open(f"src/assets/textures/{TEXTURES[tile]}")
            texture = texture.resize((TILE_SIZE, TILE_SIZE))
            img.paste(texture, (j * TILE_SIZE, i * TILE_SIZE))

    for wall in map2d.walls:
        tile_i, wall_i = wall
        i = tile_i // map2d.width
        j = tile_i % map2d.width
        WALL_TEXTURE_LOOKUP = {0: "up", 1: "right", 2: "down", 3: "left"}
        texture = Image.open(
            f"src/assets/textures/wall-{WALL_TEXTURE_LOOKUP[wall_i]}.png"
        ).convert("RGBA")
        texture = texture.resize((TILE_SIZE, TILE_SIZE))
        img.paste(texture, (j * TILE_SIZE, i * TILE_SIZE), texture)

    with open("out/map.png", "wb") as out:
        img.save(out, "PNG")


if __name__ == "__main__":
    main()
