class Camera:
    def __init__(self, coordinates : tuple):
        
        self.position_x = coordinates[0]
        self.position_y = coordinates[1]
        self.position_z = coordinates[2]

    def zoom(self, param : int):
        if not (self.position_z + param) <= 0:
            self.position_z += param
