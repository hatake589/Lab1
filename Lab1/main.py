from Board import Board
from Player import Player
from PlayerInput import PlayerInput
from GameRound import GameRound
from WinnerSelection import WinnerSelection

Board1 = Board()
Player1 = Player()
Input = PlayerInput()
Game = GameRound()
GameEnd = WinnerSelection()

Board1.setDifficulty()
print()
Board1.randomizer()
print()
Player1.assignPlayer()
print()
Input.coinToss()
print()
Input.selectTile()
print()
Game.matchTiles()
print()
Game.score()
print()
GameEnd.calculateWinner()
print()
GameEnd.newGame()