"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730555430"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
       return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)



class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        self.location = self.location.add(self.direction)
        if (self.is_infected()):
            self.sickness += 1
        
        if self.sickness >= constants.RECOVERY_PERIOD:
            self.immunize()
        

    def color(self) -> str:
        """Return the color representation of a cell."""
        return "black"


    def contract_disease(self) -> None:
        """Assigns a cell to be sick."""
        self.sickness = constants.INFECTED


    def is_vulnerable(self) -> bool:
        """Assigns a cell to be vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False


    def is_infected(self) -> bool:
        """Assigns a cell to be infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False


    def color(self) -> str:
        """Assigns color based on health."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_immune():
            return "blue"
        else:
            return "misty rose"


    def contact_with(self, other: Cell) -> None:
        """Cells in contact contract diseases."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        if other.is_infected() and self.is_vulnerable():
            self.contract_disease()


    def immunize(self) -> None:
        """Function for immunity."""
        self.sickness = constants.IMMUNE
    

    def is_immune(self) -> bool:
        """Assigns a cell to be immune."""
        return self.sickness == constants.IMMUNE

class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0


    def __init__(self, cells: int, speed: float, infect: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if infect <= 0  or infect >= cells:
            raise ValueError("Some amount of cells must begin infected and less than the number of cells.")
        
        if immune < 0 or immune >= cells:
            raise ValueError("Some amount of immune cells cannot be less than 0 and must be less than the number of cells.")

        self.population = []
        infected_num: int = 0
        immune_num: int = 0 

        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if infected_num < infect:
                cell.contract_disease()
                infected_num += 1
            
            if immune_num < immune: 
                cell.immunize()
                immune_num += 1

            self.population.append(cell)
            

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        print(self.time)
        for cell in self.population:
            self.enforce_bounds(cell)
            cell.tick()
            if cell.is_infected():
                cell.sickness += 1
                if cell.sickness > constants.RECOVERY_PERIOD:
                    cell.immunize()

        self.check_contacts()


    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)


    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)


    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0

        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0

        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0

        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0


    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        
        return True


    def check_contacts(self) -> None:
        """If two cells are touching."""
        for i in range(len(self.population)-1):
            for a in range(i+1, len(self.population)):
                if self.population[i].location.distance(self.population[a].location) <= constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[a])