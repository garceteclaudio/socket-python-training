class Camera:
    def __init__(self, width, height, map_width, map_height):
        self.width = width
        self.height = height
        self.map_width = map_width
        self.map_height = map_height
        self.offset_x = 0
        self.offset_y = 0

    def update(self, target_x, target_y):
        # Centrar cámara en el jugador
        self.offset_x = target_x - self.width // 2
        self.offset_y = target_y - self.height // 2

        # Limitar la cámara al mapa
        self.offset_x = max(0, min(self.offset_x, self.map_width - self.width))
        self.offset_y = max(0, min(self.offset_y, self.map_height - self.height))
