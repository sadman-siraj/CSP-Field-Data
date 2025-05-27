import math

def get_distance2D(p1, p2):
    d = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return d

def get_distance3D(p1, p2):
    d = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
    return d

def get_PL(p1, p2, f_c):
    PL = 21.8 * math.log10(get_distance3D(p1, p2)) - 70.46 * math.log10(f_c) + 691.66 # [dB]
    return PL

def get_channel_gain(p1, p2, f_c):
    g = 1 / 10**( (get_PL(p1, p2, f_c) / 10) ) # [dB] to linear then inverse
    return g