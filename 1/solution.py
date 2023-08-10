def main(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        
        if c == 0 or isinstance(c, str):
            return 'err'
        
        return (a + b) / c
    except (TypeError, ValueError):
        return 'err'