
class Model:
    mouse_callback = None
    key_callback = None
    path = None
    is_clicked = False
    is_focused = False

    def __init__(self):
        raise NotImplementedError
    def render(self):
        raise NotImplementedError
    def update(self, dt):
        raise NotImplementedError
    def clicked(self, xc, yc):
        raise NotImplementedError
    def focused(self, xc, yc):
        raise NotImplementedError