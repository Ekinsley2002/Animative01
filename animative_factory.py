from animative import Animative
import utilities
import configanimative

class AnimativeFactory:
    def __init__(self):
        self.count = 0

    def create_animative_index(self, index):
        animative = Animative(configanimative.ANIMATIVES[index]['animative_type'], index)
        self.count = self.count + 1
        return animative

    def create_animative(self, animative_type):
        random_number = -1
        if animative_type == "g":
            random_number = utilities.generate_random_number(configanimative.GRASS_TYPE_START, configanimative.GRASS_TYPE_END)
        animative = Animative(animative_type, random_number)
        return animative


