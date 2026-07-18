def clamp(value, low, high):
    """Return low if value < low, high if value > high, otherwise value."""
    if value < low:
        return low
    if value > high:
        return high
    return value
