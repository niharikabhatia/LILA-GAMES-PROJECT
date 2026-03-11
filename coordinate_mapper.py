from config import MINIMAP_SIZE

def world_to_minimap(x, z, scale, origin_x, origin_z):

    u = (x - origin_x) / scale
    v = (z - origin_z) / scale

    px = u * MINIMAP_SIZE
    py = (1 - v) * MINIMAP_SIZE

    return px, py