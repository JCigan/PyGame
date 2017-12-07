#!/usr/bin/env python3

import random
import sys

import pygame
from pygame.locals import *

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

def main():
    x_obj = pygame.image.load('x.png')
    o_obj = pygame.image.load('o.png')
    pygame.init()
    game_surface = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Tic Tac Toe')
    winner = False
    turn_no = 0
    board = [[None, None, None], [None, None, None], [None, None, None]]
    coordinates = [
                   [(0, 0), (200, 0), (400, 0)],
                   [(0, 200), (200, 200), (400, 200)],
                   [(0, 400), (200, 400), (400, 400)]
                  ]
    while not winner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winner = " "
            elif event.type == MOUSEBUTTONDOWN:
                turn_no = handle_click(board, turn_no)
                winner = check_for_winner(board, turn_no)
        draw_board(game_surface, board, coordinates, x_obj, o_obj)
        pygame.display.update()

    print(winner)
    pygame.quit()
    sys.exit()


def handle_click(board, turn_no):
    x_pos, y_pos = pygame.mouse.get_pos()
    column = x_pos // 200
    row = y_pos // 200
    print(row, column)
    if not board[row][column]:
        if turn_no % 2 == 0:
            board[row][column] = "X"
        else:
            board[row][column] = "O"
        turn_no += 1
    return turn_no


def draw_board(game_surface, board, coordinates, x_obj, o_obj):
    game_surface.fill(white)
    pygame.draw.line(game_surface, black, (200, 0), (200, 600), 3)
    pygame.draw.line(game_surface, black, (400, 0), (400, 600), 3)
    pygame.draw.line(game_surface, black, (0, 200), (600, 200), 3)
    pygame.draw.line(game_surface, black, (0, 400), (600, 400), 3)
    for row in range(3):
        for column in range(3):
            if board[row][column] == "X":
                game_surface.blit(x_obj, coordinates[row][column])
            elif board[row][column] == "O":
                game_surface.blit(o_obj, coordinates[row][column])

def check_for_winner(board, turn_no):
    for row in range(3):
        if board[row][0] and board[row][0] == board[row][1] == board[row][2]:
            return "Winner is {0}".format(board[row][0])
    for column in range(3):
        if board[0][column] and board[0][column] == board[1][column] == \
board[2][column]:
            return "Winner is {0}".format(board[0][column])
    if turn_no == 9:
        return "Catsgame"
    else:
        return False


if __name__ == '__main__':
    main()
