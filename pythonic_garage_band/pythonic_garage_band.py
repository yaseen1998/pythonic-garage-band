from abc import ABC, abstractmethod
class Band():
    """
    in this class we collect the team member and name of Band 

    """
    instances=[]
    def __init__(self,name,members):
        self.name = name # name of band
        self.members = members # member of band
        Band.instances.append(self) # create list for previous member


    def play_solos(self):
        """
        print poly_solo for every member in team 
        """
        result=[]
        for i in self.members:
            result.append(i.play_solo())
        return result
    
    @classmethod
    def to_list(cls):
        """
        call the previous member and name for Band
        """
        return cls.instances

class Musician():
    """
    in this class store and inhirt the name of musician
    """
    def __init__(self,name):
        self.name =name

class Guitarist(Musician):
    """
    the class for guitarist member and some information about him
    """
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "guitar"
    @staticmethod
    def play_solo():
        return "face melting guitar solo"

class Bassist(Musician):
    """
    the class for Bassist member and some information about him
    """
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "bass"
    @staticmethod
    def play_solo():
        return "bom bom buh bom"


class Drummer(Musician):
    """
    the class for Drummer member and some information about him
    """
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "drums"
    @staticmethod
    def play_solo():
        return "rattle boom crash"

