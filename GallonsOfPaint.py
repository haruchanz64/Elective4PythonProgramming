def get_gallons_needed():
    length = 12  # feet
    width = 8  # feet
    paint_coverage = 350  # paint coverage per gallon

    # Calculate area
    area = length * width

    # Calculate gallons needed
    gallons_needed = area / paint_coverage

    return print(f"You need approximately {gallons_needed:.2f} gallons of paint.")


def main():
    get_gallons_needed()


main()
