import sys
from geometry import *


def main():
    '''
    Logic program
    '''

    shapes = ShapeList()  # object containing all shapes added by the user
    while True:

        try:
            print('''
            1. Add shape
            2. Show all shapes
            3. Show shape with the largest perimeter
            4. Show shape with the largest area
            5. Show formula (area and perimeter)
            0. Exit
            ''')

            option = input("Select an option: ")
            if option == "1":
                # Add new shape
                user_choice = shapes.choose_shape()
                shape = shapes.create_shape(user_choice)
                shapes.add_shape(shape)

            elif option == "2":
                # Show all shapes
                shapes.get_shapes_table()

            elif option == "3":
                # Show shape with the largest perimeter
                shapes.get_largest_shape_by_perimeter()

            elif option == "4":
                # Show shape with the largest area
                shapes.get_largest_shape_by_area

            elif option == "5":
                # Show formulas
                user_choice = shapes.choose_shape()
                shapes.display_formula(user_choice)

            elif option == "0":
                # Exit
                sys.exit()

            else:
                # Incorrect answer
                print('Bad choice')

        except ValueError as err:
            print(''.join(err.args))

        except TypeError as err:
            print(''.join(err.args))


if __name__ == "__main__":
    main()
