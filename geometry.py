from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    This is a abstract class representing geometrical shape.
    """

    def __init__(self, *args):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        for arg in args:
            if arg < 0:
                raise ValueError('Number below 0!!')

    @abstractmethod
    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        return self.area

    @abstractmethod
    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        return self.perimeter

    @abstractmethod
    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information about shape
        """
        return self.text

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the shape as a string.

        Returns:
            str: area formula
        """
        return self.area_formula

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the shape as a string.

        Returns:
            str: perimeter formula
        """
        return self.perimeter_formula


class Circle(Shape):
    '''This is class representing geometric figure: circle'''

    def __init__(self, r):
        '''
        Constructs Circle object
        '''

        super().__init__(r)
        self.r = r

    def get_area(self):
        """
        Calculates circle area.

        Returns:
            float: area of the circle
        """

        self.area = float("{0:.2f}".format(math.pi * self.r * self.r))
        return self.area

    def get_perimeter(self):
        """
        Calculates circle perimeter.

        Returns:
            float: perimeter of the circle
        """

        self.perimeter = float("{0:.2f}".format(2 * math.pi * self.r))
        return self.perimeter

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the circle as a string.

        Returns:
            str: area formula
        """

        return '{0:.2f}x r^2'.format(math.pi)

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the circle as a string.

        Returns:
            str: perimeter formula
        """

        return '2 x {0:.2f} x r'.format(math.pi)

    def __str__(self):
        """
        Returns information about the circle as string.

        Returns:
            str: information about circle
        """

        self.text = '{}, r = {}'.format(self.__class__.__name__, self.r)
        return self.text


class Triangle(Shape):
    '''
    This is class representing geometric figure: triangle.
    To inherit from Shape.
    '''

    def __init__(self, a, b, c):
        '''
        Constructs Triangle object
        '''

        super().__init__(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        """
        Calculates triangle area.

        Returns:
            float: area of the triangle
        """

        s = (self.a + self.b + self.c) / 2
        self.get_area = float("{0:.2f}".format(math.sqrt(s*(s - self.a)*(s - self.b)*(s - self.c))))
        return self.get_area

    def get_perimeter(self):
        """
        Calculates triangle perimeter.

        Returns:
            float: perimeter of the triangle
        """

        self.get_perimeter = float("{0:.2f}".format(self.a + self.b + self.c))
        return self.get_perimeter

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the triangle as a string.

        Returns:
            str: area formula
        """

        return 'sqrt(s x (s-a)x(s-b)x(s-c)) \ns = (a+b+c)/2'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the triangle as a string.

        Returns:
            str: perimeter formula
        """

        return 'a + b + c'

    def __str__(self):
        """
        Returns information about the triangle as string.

        Returns:
            str: information about triangle
        """

        return '{}, a = {}, b = {}, c = {}'.format(self.__class__.__name__, self.a, self.b, self.c)


class EquilateralTriangle(Triangle):
    '''This is class representing geometric figure: equilateral triangle
    To inherit from Triangle.'''

    def __init__(self, a):
        '''
        Constructs EquilateralTriangle object
        '''

        super().__init__(a, a, a)
        self.a = a
        self.b = a
        self.c = a

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the equilateral triangle as a string.

        Returns:
            str: area formula
        """

        return '(a^2 * sqrt(3)) / 4'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the equilateral triangle as a string.

        Returns:
            str: perimeter formula
        """

        return '3*a'

    def __str__(self):
        """
        Returns information about the equilateral triangle as string.

        Returns:
            str: information about equilateral triangle
        """

        return '{}, a = {}'.format(self.__class__.__name__, self.type, self.a)


class Rectangle(Shape):
    '''This is class representing geometric figure: rectangle
    To inherit from Shape.'''

    def __init__(self, a, b):
        '''
        Constructs Rectangle object
        '''

        super().__init__(a, b)
        self.a = a
        self.b = b

    def get_area(self):
        """
        Calculates rectangle area.

        Returns:
            float: area of the rectangle
        """

        self.get_area = float("{0:.2f}".format(self.a * self.b))
        return self.get_area

    def get_perimeter(self):
        """
        Calculates rectangle perimeter.

        Returns:
            float: perimeter of the rectangle
        """

        self.get_perimeter = float("{0:.2f}".format(2*self.a + 2*self.b))
        return self.get_perimeter

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the rectangle as a string.

        Returns:
            str: area formula
        """

        return 'a*b'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the rectangle as a string.

        Returns:
            str: perimeter formula
        """

        return '2a + 2b'

    def __str__(self):
        """
        Returns information about the rectangle as string.

        Returns:
            str: information about rectangle
        """

        return '{}, a = {}, b = {}'.format(self.__class__.__name__, self.a, self.b)


class Square(Rectangle):
    '''This is class representing geometric figure: square
    To inherit from Rectangle.'''

    def __init__(self, a):
        '''
        Constructs Square object
        '''

        super().__init__(a, a)

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the square as a string.

        Returns:
            str: area formula
        """

        return 'a^2'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the square as a string.

        Returns:
            str: perimeter formula
        """

        return '2*a'

    def __str__(self):
        """
        Returns information about the square as string.

        Returns:
            str: information about square
        """

        return '{}, a = {}'.format(self.__class__.__name__, self.type, self.a)


class RegularPentagon(Shape):
    '''This is class representing geometric figure: regular pentagon
    To inherit from Shape.'''

    def __init__(self, a):
        '''
        Constructs RegularPentagon object
        '''

        super().__init__(a)
        self.a = a

    def get_area(self):
        """
        Calculates regular pentagon area.

        Returns:
            float: area of the regular pentagon
        """

        self.get_area = float("{0:.2f}".format((self.a**2 * math.sqrt(5*(5 + 2*math.sqrt(5))))/4))
        return self.get_area

    def get_perimeter(self):
        """
        Calculates regular pentagon perimeter.

        Returns:
            float: perimeter of the regular pentagon
        """

        self.get_perimeter = float("{0:.2f}".format(5*self.a))
        return self.get_perimeter

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the regular pentagon as a string.

        Returns:
            str: area formula
        """

        return '(a^2 * sqrt(5(5 + 2*sqrt(5)))) / 4'

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the regular pentagon as a string.

        Returns:
            str: perimeter formula
        """

        return '5*a'

    def __str__(self):
        """
        Returns information about the regular pentagon as string.

        Returns:
            str: information about regular pentagon
        """

        return '{}, a = {}'.format(self.__class__.__name__, self.a)


class ShapeList:
    '''This is class representing list of shapes'''

    def __init__(self):
        '''
        Constructs ShapeList object
        '''

        self.shapes = []

    def add_shape(self, shape):
        '''
        Add new shape to list shapes.
        Raise TypeError if shape is not ancestor of Shape class.ABC

        Args:
            shape - object
        '''

        if not isinstance(shape, Shape):
            raise TypeError('Shape is not ancestor!')
        else:
            self.shapes.append(shape)

    def create_circle(self):
        '''
        Take radius from user, check correct format (int) and create new object of Circle class.

        Returns:
            shape - object
        '''

        r = input('Write radius r: ')
        self.is_digit(r)
        shape = Circle(int(r))

        return shape

    def create_triangle(self):
        '''
        Take side a, b and from user, check correct format (int) and create new object of Triangle class.

        Returns:
            shape - object
        '''

        a = input('Write length side a: ')
        b = input('Write length side b: ')
        c = input('Write length side c: ')
        self.is_digit(a, b, c)
        shape = Triangle(int(a), int(b), int(c))

        return shape

    def create_equalateral_triangle(self):
        '''
        Take side a from user, check correct format (int) and create new object of EquilateralTriangle class.

        Returns:
            shape - object
        '''

        a = input('Write length side a: ')
        self.is_digit(a)
        shape = EquilateralTriangle(int(a))

        return shape

    def create_rectangle(self):
        '''
        Take side a and b from user, check correct format (int) and create new object of Rectangle class.

        Returns:
            shape - object
        '''

        a = input('Write length side a: ')
        b = input('Write length side b: ')
        self.is_digit(a, b)
        shape = Rectangle(int(a), int(b))

        return shape

    def create_square(self):
        '''
        Take side a from user, check correct format (int) and create new object of Square class.

        Returns:
            shape - object
        '''

        a = input('Write length side a: ')
        self.is_digit(a)
        shape = Square(int(a))

        return shape

    def create_regular_pentagon(self):
        '''
        Take side a from user, check correct format (int) and create new object of RegularPentagon class.

        Returns:
            shape - object
        '''

        a = input('Write length side a: ')
        self.is_digit(a)
        shape = RegularPentagon(int(a))

        return shape

    def is_digit(self, *args):
        '''
        Raise Value Error if some argument is not digit.
        '''

        for arg in args:
            if not arg.isdigit():
                raise ValueError('Parametr must be number!')

    def choose_shape(self):
        '''
        Show options. User choose shape.ABC

        Returns:
            user_choice - string
        '''

        print('''
        1. Circle
        2. Triangle
        3. Equalateral Triangle
        4. Rectangle
        5. Square
        6. Regular pentagon
        ''')

        user_choice = input('Choose shape: ')

        return user_choice

    def create_shape(self, user_choice):
        '''
        Depending on the user_choice, create proper geometrical figure.

        Returns:
            shape - object
        '''

        if user_choice == '1':
            shape = self.create_circle()

        elif user_choice == '2':
            shape = self.create_triangle()

        elif user_choice == '3':
            shape = self.create_equalateral_triangle()

        elif user_choice == '4':
            shape = self.create_rectangle()

        elif user_choice == '5':
            shape = self.create_square()

        elif user_choice == '6':
            shape = self.create_regular_pentagon()

        else:
            print('Bad choice')
            shape = None

        return shape

    def get_largest_shape_by_perimeter(self):
        '''
        Find the largest value of perimeter for figure in shapes list.

        Returns:
            shape - object
        '''

        largest_perimeter = 0
        for figure in self.shapes:
            if float(figure.get_perimeter()) > largest_perimeter:
                largest_perimeter = figure.get_perimeter
                max_shape_by_perimeter = figure

        return max_shape_by_perimeter

    def get_largest_shape_by_area(self):
        '''
        Find the largest value of area for figure in shapes list.

        Returns:
            shape - object
        '''

        largest_area = 0
        for figure in self.shapes:
            if float(figure.get_area()) > largest_area:
                largest_area = figure.get_area
                max_shape_by_area = figure

        return max_shape_by_area

    def get_data_to_table(self):
        '''
        Create table row: insert data to list in proper order (according to the tittle).
        Add row list to bigger list with all rows.

        Returns:
            rows_list - list of lists
        '''
        rows_list = []
        index = 0
        title = ['idx', 'Class', '__str__', 'Perimeter', 'Formula', 'Area', 'Formula']
        rows_list.append(title)
        for figure in self.shapes:
            row = [index,
                   figure.__class__.__name__,
                   figure.__str__(),
                   figure.get_perimeter(),
                   figure.get_perimeter_formula(),
                   figure.get_area(),
                   figure.get_area_formula()
                   ]

            rows_list.append(row)
            index += 1

        return rows_list

    def find_max_string(self, data, index):
        '''
        Find max length of data in column.

        Args:
            data - list of lists
            index - int

        Returns:
            length longest string - int
        '''

        longest_string = ''
        for row in data:
            if len(str(row[index])) > len(longest_string):
                longest_string = str(row[index])

        return len(longest_string)

    def draw_data_row(self, data, row):
        '''
        Draw row with data (with proper width and format).

        Args:
            data - list of lists
            row - list

        Returns:
            row_data - string
        '''

        row_data = '|'
        addit = 2
        index = 0
        for item in row:
            max_string = self.find_max_string(data, index)
            cell_width = max_string + addit
            row_data = row_data + (str(item).center(cell_width, ' ')) + '|'
            index += 1

        return row_data

    def draw_out_row(self, data, row):
        '''
        Draw out row (with proper width and format).

        Args:
            data - list of lists
            row - list

        Returns:
            out_row - string
        '''

        index = 0
        addit = 3
        out_row = ''
        for item in row:
            max_string = self.find_max_string(data, index)
            cell_width = max_string + addit
            out_row += '-' * cell_width
            index += 1

        return out_row

    def get_shapes_table(self):
        '''
        Connection out row with data row and create proper table.

        Returns:
            out_row - string
        '''

        data = self.get_data_to_table()
        for row in data:
            out_row = self.draw_out_row(data, row)
            print(out_row)
            middle_row = self.draw_data_row(data, row)
            print(middle_row)
        print(out_row)

        return out_row

    def display_formula(self, user_choice):
        '''
        Display area and peremiter formula depending on user_choice.ABC

        Args:
            user_choice - string
        '''

        if user_choice == '1':
            print("area: {}, \nperimeter: {}".format(Circle.get_area_formula(), Circle.get_perimeter_formula()))

        elif user_choice == '2':
            print("area: {}, \nperimeter: {}".format(Triangle.get_area_formula(), Triangle.get_perimeter_formula()))

        elif user_choice == '3':
            print("area: {}, \nperimeter: {}".format(EquilateralTriangle.get_area_formula(), EquilateralTriangle.get_perimeter_formula()))

        elif user_choice == '4':
            print("area: {}, \nperimeter: {}".format(Rectangle.get_area_formula(), Rectangle.get_perimeter_formula()))

        elif user_choice == '5':
            print("area: {}, \nperimeter: {}".format(Square.get_area_formula(), Square.get_perimeter_formula()))

        elif user_choice == '6':
            print("area: {}, \nperimeter: {}".format(RegularPentagon.get_area_formula(), RegularPentagon.get_perimeter_formula()))

        else:
            print('Bad choice')



