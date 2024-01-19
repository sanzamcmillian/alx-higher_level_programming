#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class represents a geometric rectangle and inherits from the Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The identifier of the rectangle.
    """

    def __init__(self, width, height, x = 0, y = 0, id = None):
        """
        Initializes a new Rectangle instance.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the top-left corner of the rectangle.
            y (int): The y-coordinate of the top-left corner of the rectangle.
            id (int): The identifier of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        
    @property
    def width(self):
        """

        Getter method for the width property.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Setter method for the width property.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >0")
        self.__width = value
        
    @property
    def height(self):
        """

        Getter method for height property.

        Returns: 
           int: The height of the rectangle.
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """

        Setter method for the height property

        Raises:
           TypeError: If the provided value is not an integer.
           ValueError: If the provided value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >0")
        self.__height = value
        
    @property
    def x(self):
        """

        Getter method for the x property.

        Returns:
           int: The x of the rectangle.
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """
        Setter method fo the x property.

        Raises:
           TypeError:  If the provided value is not an integer.
           ValueError: If the provided value is less than 0.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >=0")
        self.__x = value
        
    @property
    def y(self):
        """

        Getter method for the y property.

        Returns:
           int: The y of the rectangle.
        """
        return self.__y 
    
    @y.setter
    def y(self, value):
        """

        Setter method for the y property.

        Raises:
           TypeError: If the provided value is not an integer.
           ValueError: If the provided value is less than 0.
        """
        if type(value) != int:
            raise TypeError("y musst be ab integer")
        if value < 0:
            raise ValueError("y must be >=0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Displays the rectangle by printing its visual representation with '#' characters.
        """
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end = "") for x in range(self.x)]
            [print("#", end = "") for w in range(self.width)]
            print("")
    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle using either positional arguments or keyword arguments.
        """
        if args and len(args) != 0:
           a = 0
           for arg in args:
               if a == 0:
                  if arg is None:
                     self.__init__(self.width, self.height, self.x, self.y)
                  else:
                     self.id = arg
               elif a == 1:
                  self.width = arg
               elif a == 2:
                  self.height = arg
               elif a == 3:
                  self.x = arg
               elif a == 4:
                  self.y = arg
               a += 1
        elif kwargs and len(kwargs) != 0:
           for k, v in kwargs.items():
               if k == "id":
                  if v is None:
                     self.__init__(self.width, self.height, self.x, self.y)
                  else:
                     self.id = v
               elif k == "width":
                  self.width = v
               elif k == "height":
                  self.height = v
               elif k == "x":
                  self.x = v
               elif k == "y":
                  self.y = v
    def to_dictionary(self):
        """
        Converts the rectangle object to a dictionary.

        Returns:
            dict: A dictionary representation of the rectangle.
        """
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}  
