

class cell:

    def __init__(self, x, y, content):
        self.x = x
        self.y = y
        # 0..8 — numeric content, also FLAGGED and UNKNOWN constants
        self.content = content