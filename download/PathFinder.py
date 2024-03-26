# MIT License
#
# Copyright (c) 2024 Wanets
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import time
#╔═══╗      ╔╗ ╔╗   ╔═══╗        ╔╗       
#║╔═╗║     ╔╝╚╗║║   ║╔══╝        ║║       
#║╚═╝║╔══╗ ╚╗╔╝║╚═╗ ║╚══╗╔╗╔═╗ ╔═╝║╔══╗╔═╗
#║╔══╝╚ ╗║  ║║ ║╔╗║ ║╔══╝╠╣║╔╗╗║╔╗║║╔╗║║╔╝
#║║   ║╚╝╚╗ ║╚╗║║║║╔╝╚╗  ║║║║║║║╚╝║║║═╣║║ 
#╚╝   ╚═══╝ ╚═╝╚╝╚╝╚══╝  ╚╝╚╝╚╝╚══╝╚══╝╚╝
def newline():
    print("------------------------------------")

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end='')
        print()

def find_path(board, start, end):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = [(start, [])]
    visited = set()

    while queue:
        (x, y), path = queue.pop(0)
        if (x, y) == end:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != '🔲' and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None

def main():
    input_board = [
        ['🚩', '🔲', '🔲', '🏁', '🔲', '💠', '💠', '💠', '💠', '💠'],
        ['💠', '🔲', '🔲', '💠', '🔲', '💠', '💠', '💠', '💠', '💠'],
        ['💠', '🔲', '🔲', '💠', '🔲', '🔲', '🔲', '💠', '💠', '💠'],
        ['💠', '💠', '💠', '💠', '🔲', '💠', '🔲', '💠', '💠', '💠'],
        ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲']
    ]

    end_pos = None
    for i in range(len(input_board)):
        for j in range(len(input_board[0])):
            if input_board[i][j] == '🏁':
                end_pos = (i, j)
                break

    if end_pos is None:
        print("You need to place atleast 1 end position")
        return

    start_pos = None
    for i in range(len(input_board)):
        for j in range(len(input_board[0])):
            if input_board[i][j] == '🚩':
                start_pos = (i, j)
                break

    if start_pos is None:
        print("You need to place a start position")
        return

    path = find_path(input_board, start_pos, end_pos)

    if path is None:
        print("Error! This map is unbeatable, or you have placed too much elements")
    else:
        print("Path calculated")
        for step in path:
            board_copy = [row[:] for row in input_board]
            board_copy[step[0]][step[1]] = '🤖'
            newline()
            print_board(board_copy)
            time.sleep(0.5)  # Adjust the delay time as needed
            

if __name__ == "__main__":
    main()
