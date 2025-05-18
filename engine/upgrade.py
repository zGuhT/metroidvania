# engine/upgrade.py
class Upgrade:
    def __init__(self, kind, rect):
        self.kind = kind
        self.rect = rect
        # kind: 'double_jump', 'dash', etc.