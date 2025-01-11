#public modifier
class ABC :
    def __init__ (self):
        self.public_attribute = None #this is a public attribute

    def public_function(): #this is a public function
        pass 

obj1 = ABC()
obj1.public_attribute
obj1.public_function() 

#private modifier
class ABCD :
    def __init__ (self):
        self.__private_attribute = None #this is a private attribute (use two underscores after .)

    def __private_function(): #this is a private function
        pass 

#protected modifier
class ABCDE :
    def __init__ (self):
        self._protected_attribute = None #this is a protected attribute (use one underscores after .)

    def _protected_function(): #this is a protected function
        pass 