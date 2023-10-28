import random
import pygame

class Obstacle:
    def __init__(self, position, type):
        self.position = position
        self.type = type

    def is_colliding(self, player_position):
        return self.position == player_position

class Bonus:
    def __init__(self, position, type):
        self.position = position
        self.type = type

    def apply_effect(self, player):
        # Effet du bonus
        pass

class Environment:
    def __init__(self, width, height):
        self.obstacles = []
        self.bonuses = []
        self.width = width
        self.height = height

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def add_bonus(self, bonus):
        self.bonuses.append(bonus)

    def is_colliding(self, player_position):
        for obstacle in self.obstacles:
            if obstacle.is_colliding(player_position):
                return True
        return False

    def get_valid_positions(self):
        valid_positions = []
        for x in range(self.width):
            for y in range(self.height):
                if not self.is_colliding((x, y)):
                    valid_positions.append((x, y))
        return valid_positions

class State:
    def __init__(self, player_positions, treasure_positions, active_player):
        self.player_positions = player_positions
        self.treasure_positions = treasure_positions
        self.active_player = active_player

    def is_terminal(self):
        for treasure_position in self.treasure_positions:
            if treasure_position in self.player_positions:
                return True
        return False

    def get_possible_moves(self):
        possible_moves = []
        for player_position in self.player_positions:
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_position = (player_position[0] + direction[0], player_position[1] + direction[1])
                if new_position in self.get_valid_positions():
                    possible_moves.append((player_position, direction))
        return possible_moves

    def apply_move(self, move):
        new_state = State(self.player_positions[:], self.treasure_positions[:], self.active_player)
        new_state.player_positions[self.active_player] = (move[0][0] + move[1][0], move[0][1] + move[1][1])
        return new_state

    def value(self):
        if self.is_terminal():
            if self.active_player == 0:
                return len(self.treasure_positions)
            else:
                return 0
        else:
            return None

def evaluate_state(state):
    distances_to_treasures = [
        abs(state.player_positions[0][0] - state.treasure_positions[0][0]) + abs(state.player_positions[0][1] - state.treasure_positions[0][1]),
        abs(state.player_positions[1][0] - state.treasure_positions[1][0]) + abs(state.player_positions[1][1] - state.treasure_positions[1][1]),
    ]
    return min(distances_to_treasures)

def alpha_beta_min_max(state, alpha, beta):
    if state.is_terminal():
        return state.value()

    best_move = None
    best_value = float("-inf")
    for move in state.get_possible_moves():
        new_state = state.apply_move(move)
        value = -alpha_beta_min_max(new_state, -beta, -alpha)
        if value > best_value:
            best_value = value
            best_move = move
        alpha = max(alpha, value)
        if alpha >= beta:
            break

    if state.active_player == 0:
        return best_move, best_value
    else:
        return best_move, -best_value
