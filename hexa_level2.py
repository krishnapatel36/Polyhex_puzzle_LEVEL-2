import streamlit as st
from polymino import Grid,generate_polyminoes,generate_polymino_positions,unique_grids
from dlx import DLX
from hexa_rotation_flip import P1,P2,P3,P4,P5,P6,P7,P8,P9
from itertools import product
from svgwrite import Drawing,text
import numpy as np  

st.title("Shatkon Paheli")

# def solutions_svg(solutions, filename, columns=1, size=5, padding=10,
#                   colour=lambda _: "white",stroke_colour="black",
#                   stroke_width=10, empty=' '):
#     """Format polyomino tilings as an SVG image.

#     Args:
#         solutions (list): List of polyomino solution grids.
#         filename (str): Filename for the SVG image.
#         columns (int, optional): Number of columns in the image (Default: 1).
#         size (int, optional): Size of each hexagon (default: 25).
#         padding (int, optional): Padding around the image (default: 5)
#         colour (function, optional): Function taking a piece name and returning its colour (Default: a function returning white for each piece).
#         stroke_colour (str, optional): Stroke colour (default: black).
#         stroke_width (int, optional): Width of strokes between pieces (default: 3).
#         empty (str, optional): String for empty grid point.
#     """
#     solutions = list(solutions)

#     height, width = solutions[0].size

#     rows = (len(solutions) + columns - 1) // columns

#     drawing_size = (2 * padding + (columns * (3/2 * size) - 0.5) * width,
#                     2 * padding + (rows * (np.sqrt(3) * size) - 0.5) * height)

#     drawing = Drawing(debug=False, filename=filename, size=drawing_size)
#     for i, solution in enumerate(solutions):
#         y, x = divmod(i, columns)
#         oj = padding + (x * (3/2 * size) - 0.5) * width
#         oi = padding + (y * (np.sqrt(3) * size) - 0.5) * height
#         group = drawing.g(stroke=stroke_colour, stroke_linecap="round",
#                           stroke_width=1)
#         drawing.add(group)

#         grid = [[empty] * width for _ in range(height)]
#         for polymino in solution.polyminoes:
#             piece = drawing.g(fill=colour(polymino.name))
#             group.add(piece)
#             for i, j in polymino.coord:
#                 x_coord = j * (1.69 * size) + oj + ((i + (j % 8) / 8) * size)
#                 y_coord = i * (np.sqrt(2) * size) + oi
#                 # Calculate the points for a pointed top hexagon
#                 points = [
#                     (x_coord + size * np.cos(np.radians(angle)),
#                      y_coord + size * np.sin(np.radians(angle)))
#                     for angle in range(30, 360, 60)
#                 ]
#                 piece.add(drawing.polygon(points))

#         # put in "empty" pieces
#         # num=1
#         for i, j in solution.coord:
#             if grid[i][j] == empty:
#                 x_coord = j * (1.69 * size) + oj + ((i + (j % 8) / 8) * size)
#                 y_coord = i * (np.sqrt(2.2) * size) + oi
#                 # if num==17:
#                 #     t1 = text.Text("H", insert=(x_coord-10,y_coord), fill='white', font_size=3)
#                 #     drawing.add(t1)
#                 # if number==num:
#                 #     text_element = text.Text(num+1, insert=(x_coord,y_coord), fill='black', font_size=3)
#                 #     num+=2
#                 # else:
#                 #     text_element = text.Text(num, insert=(x_coord,y_coord), fill='black', font_size=3)
#                 #     num+=1
#                 # drawing.add(text_element)

#         edges = drawing.path(stroke_width=stroke_width)
#         group.add(edges)
#         for i, j in product(range(height + 1), range(width)):
#             if ((empty if i == 0 else grid[i-1][j])
#                 != (empty if i == height else grid[i][j])):
#                 x_coord = j * (3/2 * size) + oj + ((i + (j % 2) / 2) * size)
#                 y_coord = i * (np.sqrt(3) * size) + oi
#                 edges.push(['M', x_coord + size * np.cos(np.radians(30)),
#                             y_coord + size * np.sin(np.radians(30)),
#                             'l', size * np.cos(np.radians(30)),
#                             -size * np.sin(np.radians(30))])
#         for i, j in product(range(height), range(width + 1)):
#             if ((empty if j == 0 else grid[i][j-1])
#                 != (empty if j == width else grid[i][j])):
#                 x_coord = j * (3/2 * size) + oj + ((i + (j % 2) / 2) * size)
#                 y_coord = i * (np.sqrt(3) * size) + oi
#                 edges.push(['M', x_coord, y_coord, 'l', 0, size])

#     drawing.save()

def solutions_svg(solutions, filename, date_number, month_name, date_position, month_position, columns=1, size=5, padding=10,
                  colour=lambda _: "white", stroke_colour="black", stroke_width=10, empty=' '):
    solutions = list(solutions)

    height, width = solutions[0].size

    rows = (len(solutions) + columns - 1) // columns

    drawing_size = (2 * padding + (columns * (3/2 * size) - 0.5) * width,
                    2 * padding + (rows * (np.sqrt(3) * size) - 0.5) * height)

    drawing = Drawing(debug=False, filename=filename, size=drawing_size)
    
    for i, solution in enumerate(solutions):
        y, x = divmod(i, columns)
        oj = padding + (x * (3/2 * size) - 0.5) * width
        oi = padding + (y * (np.sqrt(3) * size) - 0.5) * height
        group = drawing.g(stroke=stroke_colour, stroke_linecap="round", stroke_width=1)
        drawing.add(group)

        grid = [[empty] * width for _ in range(height)]
        for polymino in solution.polyminoes:
            piece = drawing.g(fill=colour(polymino.name))
            group.add(piece)
            for i, j in polymino.coord:
                x_coord = j * (1.69 * size) + oj + ((i + (j % 8) / 8) * size)
                y_coord = i * (np.sqrt(2) * size) + oi
                points = [
                    (x_coord + size * np.cos(np.radians(angle)),
                     y_coord + size * np.sin(np.radians(angle)))
                    for angle in range(30, 360, 60)
                ]
                piece.add(drawing.polygon(points))

        # Add the date text
        date_row, date_col = date_position
        x_coord = date_col * (1.69 * size) + oj + ((date_row + (date_col % 8) / 8) * size)
        y_coord = date_row * (np.sqrt(2) * size) + oi
        drawing.add(drawing.text(str(date_number), insert=(x_coord, y_coord+5), fill='white', font_size=20, text_anchor="middle"))

        # Add the month text
        month_row, month_col = month_position
        x_coord_month = month_col * (1.69 * size) + oj + ((month_row + (month_col % 8) / 8) * size)
        y_coord_month = month_row * (np.sqrt(2) * size) + oi
        drawing.add(drawing.text(month_name, insert=(x_coord_month, y_coord_month+5), fill='white', font_size=20, text_anchor="middle"))

        edges = drawing.path(stroke_width=stroke_width)
        group.add(edges)
        for i, j in product(range(height + 1), range(width)):
            if ((empty if i == 0 else grid[i-1][j]) != (empty if i == height else grid[i][j])):
                x_coord = j * (3/2 * size) + oj + ((i + (j % 2) / 2) * size)
                y_coord = i * (np.sqrt(3) * size) + oi
                edges.push(['M', x_coord + size * np.cos(np.radians(30)),
                            y_coord + size * np.sin(np.radians(30)),
                            'l', size * np.cos(np.radians(30)),
                            -size * np.sin(np.radians(30))])
        for i, j in product(range(height), range(width + 1)):
            if ((empty if j == 0 else grid[i][j-1]) != (empty if j == width else grid[i][j])):
                x_coord = j * (3/2 * size) + oj + ((i + (j % 2) / 2) * size)
                y_coord = i * (np.sqrt(3) * size) + oi
                edges.push(['M', x_coord, y_coord, 'l', 0, size])

    drawing.save()


number = st.selectbox("Select a Date", options=list(range(1, 32)), index=0)
month = st.selectbox("Select a Month", options=["January","February","March","April","May","June","July","August","September","October","November","December"], index=0)

month_map={
    "January":(0,1),
    "February":(0,2),
    "March":(0,3),
    "April":(0,4),
    "May":(0,5),
    "June":(0,6),
    "July":(1,1),   
    "August":(1,2),
    "September":(1,3),
    "October":(1,4),
    "November":(1,5),      
    "December":(1,6)
}
month_row_col=month_map[month]


date_map={
    1:(2,1),
    2:(2,2),
    3:(2,3),
    4:(2,4),
    5:(2,5),
    6:(2,6),
    7:(3,0),
    8:(3,1),
    9:(3,2),
    10:(3,3),
    11:(3,4),
    12:(3,5),
    13:(3,6),
    14:(4,0),
    15:(4,1),
    16:(4,2),
    17:(4,3),
    18:(4,4),
    19:(4,5),
    20:(5,0),
    21:(5,1),
    22:(5,2),
    23:(5,3),
    24:(5,4),
    25:(5,5),
    26:(6,0),
    27:(6,1),
    28:(6,2),
    29:(6,3),
    30:(6,4),
    31:(6,5),
}
date_row_col=date_map[number]

def sortkey(x):
    x = str(x)
    return (len(x), x)

COLOURS = dict(I="#f15bb5", F="#9b5de5", L="#00bbf9",
            P="#c7ffff", N="#7aff60", T="#e8fa42",
            U="#fb8f23", V="#f44a4a", W="#AAAAEE",
            X="#BB99DD", Y="#CC88CC", Z="#DD99BB")
GRID = Grid((7, 7), holes=[(0,0),(1,0),(2,0),(4,6),(5,6),(6,6),date_row_col,month_row_col])
print(GRID)
main_polyminoes=[]

pieces=[P1,P2,P3,P4,P5,P6,P7,P8,P9,P4,P7]
shade=['I','F','L','P','N','T','U','V','W','X','Y','Z']

all_solutions = []  
j=0

for SHAPES in pieces:
    polyminoes=[]
    for piece in generate_polyminoes(SHAPES):
        for position in generate_polymino_positions(piece, GRID):
            if position not in polyminoes:
                polyminoes.append(position)
    polyminoes = [polymino.aslist for polymino in polyminoes]
    polyminoes = [list(reversed(inner_list)) for inner_list in polyminoes]
    for i in polyminoes:
        i.pop()
        i.append(shade[j])
    j+=1
    polyminoes = [list(reversed(inner_list)) for inner_list in polyminoes]
    main_polyminoes+=polyminoes

LABELS = list(set([element for polymino in main_polyminoes for element in polymino]))
LABELS = sorted(LABELS, key=sortkey)

COVER = DLX(LABELS, main_polyminoes)
for i, SOLUTION in enumerate(COVER.generate_solutions()):
    solution_grid = Grid.from_DLX(SOLUTION)
    all_solutions.append(solution_grid)
    break

# solutions_svg([all_solutions[0]], filename='first_solution.svg', columns=5,colour=COLOURS.get)
solutions_svg(
    [all_solutions[0]], 
    filename='first_solution.svg', 
    date_number=number, 
    month_name=month, 
    date_position=date_row_col, 
    month_position=month_row_col,
    columns=5,
    colour=COLOURS.get
)
svg_content = open("first_solution.svg", "r").read()
st.write(f"solution for DATE: {number}")
st.image(svg_content, width=1100)



