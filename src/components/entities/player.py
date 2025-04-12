class Player():
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y
#        self.radius = 8
        self.range = 120
        self.angle = 0
        self.walkDir = 0
        self.turnDir = 0
        self.rotationSpeed = 2 * ( math.pi / 180 )

    def draw(self) -> None:
        pass

    def update(self) -> None:
    
        self.turnDir = 0
        self.walkDir = 0

        if keys[pg.K_w]:
            self.walkDir = 1
        if keys[pg.K_s]:
            self.walkDir = -1
        if keys[pg.K_d]:
            self.turnDir = 1
        if keys[pg.K_a]:
            self.turnDir = -1

        self.angle += self.turnDir * self.rotationSpeed

        self.x += self.walkDir * math.cos( self.angle )
        self.y += self.walkDir * math.sin( self.angle )
