def rectangle(lenght, width):
    if not isinstance(lenght, int) or not isinstance(width, int):
        return f"Enter valid values!"
    else:
        def area():
            return f"Rectangle area: {lenght * width}"

        def perimeter():
            return f'Rectangle perimeter: {2 * lenght + 2 *width}'

        return area() + '\n' + perimeter()

print(rectangle('2', 10))