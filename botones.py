class Button():
    def __init__(self, image=None, pos=(0, 0), text_input=None, font=None, base_color=None, hovering_color=None):
        # Inicializa los atributos de la clase
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input

        self.base_text = None
        self.hover_text = None

        if self.text_input and self.font and self.base_color:
            self.base_text = self.font.render(self.text_input, True, self.base_color)
            self.hover_text = self.font.render(self.text_input, True, self.hovering_color if self.hovering_color else self.base_color)

        if self.image is None and self.base_text:
            self.image = self.base_text

        # Obtiene los rectángulos de la imagen y el texto
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

        # Controla si el botón está siendo "hovered" (mouse sobre el botón)
        self.hovered = False

        # Velocidad de transición suave para el tamaño de fuente
        self.transition_speed = 2

    def update(self, screen):
        # Actualiza la imagen del botón según si está siendo "hovered" o no
        if self.hovered and self.hover_text:
            self.image = self.hover_text
        elif self.base_text:
            self.image = self.base_text

        # Dibuja la imagen en la pantalla
        screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        # Verifica si la posición (generalmente la posición del mouse) está dentro del botón
        if self.rect.collidepoint(position):
            return True
        return False

    def changeColor(self, position):
        # Cambia el estado de "hovered" según si la posición está dentro del botón
        self.hovered = self.rect.collidepoint(position)

    def update_font_size(self, font_size):
        # Actualiza el tamaño de fuente de forma suave
        current_font_size = self.font.get_height()
        target_font_size = font_size

        if current_font_size < target_font_size:
            current_font_size += self.transition_speed
            if current_font_size > target_font_size:
                current_font_size = target_font_size
        elif current_font_size > target_font_size:
            current_font_size -= self.transition_speed
            if current_font_size < target_font_size:
                current_font_size = target_font_size