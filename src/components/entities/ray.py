import math, pygame
from ..consts import *
from .player import Player

def normalize_angle( angle ):
    angle = angle % (2 * math.pi)
    if (angle <= 0):
        angle = (2 * math.pi) + angle
    return angle

class Ray():
    def __init__(self, angle, player, mapGrid) -> None:
        self.angle = normalize_angle(angle)
        self.player = player
        self.mapGrid = mapGrid

        self.isdown = self.angle > 0 and self.angle < math.pi
        self.isup = not self.isdown
        self.isright = self.angle < 0.5 * math.pi or self.angle > 1.5 * math.pi
        self.isleft = not self.isright

        self.wall_hit_x = 0
        self.wall_hit_y = 0

        self.color = (50, 50, 50)

    def cast(self):
        # HORIZONTAL CHECKING
        found_horizontal_wall = False
        horizontal_hit_x = 0
        horizontal_hit_y = 0

        # The first intersection is the intersection where we need to offset by the player's position
        first_intersection_x = None
        first_intersection_y = None

        # finding y first
        if self.isup:
            first_intersection_y = ((self.player.y // TILESIZE) * TILESIZE) - .001
        elif self.isdown:
            first_intersection_y = ((self.player.y // TILESIZE) * TILESIZE) + TILESIZE
        
        # self.finding x
        first_intersection_x = self.player.x + (first_intersection_y - self.player.y) / math.tan(self.angle)

        # These variables will be used later
        next_intersection_x = first_intersection_x
        next_intersection_y = first_intersection_y

        xa = 0
        ya = 0

        if self.isup:
            ya = -TILESIZE
        elif self.isdown:
            ya = TILESIZE
        
        xa = ya / math.tan(self.angle)

        while (next_intersection_x <= WIDTH and next_intersection_x >= 0 and next_intersection_y <= HEIGHT and next_intersection_y >= 0):

            if self.mapGrid[ int(next_intersection_y // TILESIZE) ][ int(next_intersection_x // TILESIZE) ]:
                found_horizontal_wall = True
                horizontal_hit_x = next_intersection_x
                horizontal_hit_y = next_intersection_y
                break
            else:
                next_intersection_x += xa
                next_intersection_y += ya

        # VERTICAL CHECKING
        found_vertical_wall = False
        vertical_hit_x = 0
        vertical_hit_y = 0

        # The first intersection is the intersection where we need to offset by the player's position
        first_intersection_x = None
        first_intersection_y = None

        # finding x first
        if self.isleft:
            first_intersection_x = ((self.player.x // TILESIZE) * TILESIZE) - .001
        elif self.isright:
            first_intersection_x = ((self.player.x // TILESIZE) * TILESIZE) + TILESIZE
        
        # self.finding y
        first_intersection_y = (first_intersection_x - self.player.x) * math.tan(self.angle) + self.player.y

        # These variables will be used later
        next_intersection_x = first_intersection_x
        next_intersection_y = first_intersection_y

        xa = 0
        ya = 0

        if self.isleft:
            xa = -TILESIZE
        elif self.isright:
            xa = TILESIZE
        
        ya = xa * math.tan(self.angle)

        while (next_intersection_x <= WIDTH and next_intersection_x >= 0 and next_intersection_y <= HEIGHT and next_intersection_y >= 0):

            if self.mapGrid[ int(next_intersection_y // TILESIZE) ][ int(next_intersection_x // TILESIZE) ]:
                found_vertical_wall = True
                vertical_hit_x = next_intersection_x
                vertical_hit_y = next_intersection_y
                break
            else:
                next_intersection_x += xa
                next_intersection_y += ya

        horizontal_distance = math.sqrt( (self.player.x - horizontal_hit_x)**2 + (self.player.y - horizontal_hit_y)**2 )
        vertical_distance = math.sqrt( (self.player.x - vertical_hit_x)**2 + (self.player.y - vertical_hit_y)**2 )

        if horizontal_distance <= vertical_distance:
            self.wall_hit_x, self.wall_hit_y = horizontal_hit_x, horizontal_hit_y 
            self.distance = horizontal_distance

            # color and visibility
            visibility = 100/self.distance
            self.color = [ visibility * 30 for i in range(3) ] if visibility < 1 else (30, 30,30)
        else:
            self.wall_hit_x, self.wall_hit_y = vertical_hit_x, vertical_hit_y 
            self.distance = vertical_distance

            # color and visibility
            visibility = 20/self.distance
            self.color = [ visibility * 50 for i in range(3) ] if visibility < 1 else (50, 50,50)

        # this will fix the fish eye effect
        self.distance *= math.cos( self.player.angle - self.angle )

    def render(self, screen):
        pygame.draw.line( screen, (255, 0, 0),(self.player.x, self.player.y),(self.wall_hit_x, self.wall_hit_y) )
