import _04_divisors


def width(area, height):
    assert area % height == 0
    return area // height


def perimeter(width, height):
    return width * 2 + height * 2


def minimum_perimeter(area):
    min_peri = None
    for h in _04_divisors.divisors(area):
        now_peri = perimeter(width(area, h), h)
        if (min_peri == None):
            min_peri = now_peri
        elif now_peri < min_peri:
            min_peri = now_peri
    return min_peri
