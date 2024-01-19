#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class represents a geometric square and inherits from the Rectangle class.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
        id (int): The identifier of the square.
    """
    def __init__(self, size, x = 0, y = 0, id = None):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square.
            x (int): The x-coordinate of the top-left corner of the square.
            y (int): The y-coordinate of the top-left corner of the square.
            id (int): The identifier of the square.
        """
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """
        Getter method for the size property.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size property.

        Parameters:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
         """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square using either positional arguments or keyword arguments.
        """
        if args and len(args) != 0:
           a = 0 
           for arg in args:
               if a == 0:
                  if arg is None:
                     self.__init__(self.size, self.x, self.y)
                  else:
                     self.id = arg
               elif a == 1:
                   self.size = arg
               elif a == 2:
                   self.x = arg
               elif a == 3:
                   self.y = arg
               a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                   if v is None:
                      self.__init__(self.size, self.x, self.y)
                   else:
                      self.id = v
                elif k == "size":
                     self.size = v
                elif k == "x":
                     self.x = v
                elif k == "y":
                     self.y = v

    def to_dictionary(self):
        """
        Converts the square object to a dictionary.

        Returns:
            dict: A dictionary representation of the square.
        """
        return({"id": self.id, "size": self.width, "x": self.x, "y": self.y})
