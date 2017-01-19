from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size):
        super(Square, self).__init__(size,size)
    def set_length(self, new_length):
        if new_length>=0:
            self.length=new_length
            self.height=new_length
            if self.has_been_drawn:
                self.draw_shape()
    def set_height(self, new_height):
        if new_height>=0:
            self.height=new_height
            self.length=new_height
            if self.has_been_drawn:
                self.draw_shape()

        
    
        
