# ──────────────────────────────────────────────
#              TURTLE GRAPHICS: RED MASK ART
#        Drawing a stylized face using shapes
# ──────────────────────────────────────────────

import turtle  # Import the turtle graphics module for drawing

# ──────────────────────────────────────────────
# Define facial shape segments as coordinate sets
# Each face part is built using two connected paths
# ──────────────────────────────────────────────

face_one = [  # Upper face / Forehead and upper contour
    [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40),
     (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],
    [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40),
     (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]
]

face_two = [  # Middle face / Cheeks and jaw
    [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30),
     (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210)],
    [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40),
     (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]
]

face_three = [  # Chin or facial base
    [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280),
     (-60, -260), (-30, -260), (-20, -250), (0, -250)],
    [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280),
     (120, -250), (110, -220), (80, -240), (60, -220), (0, -220)]
]

# ──────────────────────────────────────────────
# Initialize turtle screen settings
# ──────────────────────────────────────────────

turtle.hideturtle()                 # Hide the turtle cursor for cleaner visuals
turtle.bgcolor("black")            # Set the background to black for dramatic contrast
turtle.setup(width=500, height=600) # Define the window size
turtle.speed(3)                    # Set moderate drawing speed

# Define starting points for each shape
face_one_start = (0, 120)
face_two_start = (0, -30)
face_therr_start = (0, -220)  # (typo: "therr" should be "three")

# ──────────────────────────────────────────────
# Reusable function to draw any facial segment
# Each segment consists of two connected coordinate paths
# ──────────────────────────────────────────────

def draw_face(face_coordinates, start_point):
    turtle.penup()
    turtle.goto(start_point)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()

    # Draw the first contour
    for x, y in face_coordinates[0]:
        turtle.goto(x, y)

    # Then draw the second contour to close the shape
    for x, y in face_coordinates[1]:
        turtle.goto(x, y)

    turtle.end_fill()

# ──────────────────────────────────────────────
# Draw each part of the mask
# ──────────────────────────────────────────────

draw_face(face_one, face_one_start)
draw_face(face_two, face_two_start)
draw_face(face_three, face_therr_start)

# Keep the drawing window open until closed by the user
turtle.done()
