import ShapeClass as sc

def main():
    shapes = [sc.Circle('Circle',5), 
                  sc.Rectangle('Rectangle',4,5),
                  sc.Triangle('Triangle',6,5)]
    
    for item in shapes:
        print(f'The shape \"{item.get_name()}\" has an area of {item.calculate_area():.2f}')

main()