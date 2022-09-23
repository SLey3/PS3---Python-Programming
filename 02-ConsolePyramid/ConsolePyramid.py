# File: ConsolePyramid.py
# Name: Sergio Ley Languren

"""Constructs an astrik pyramid."""

def draw_console_pyramid(height):
    """draws an pyramid on the console."""
    astrik = "*"
    line = ""

    width = (height+1) * 2 # multiple by 2 to prevent pyramid going off into the left margin
    
    for i in range(height):
        line += f"{astrik.center(width)}\n"
        astrik += "**"
    print(line)


def test_console_pyramid():
    """Test program for the draw_console_pyramid function."""
    draw_console_pyramid(8) 
    print("\n") # spacing out the pyramids
    draw_console_pyramid(18)
    print("\n")
    draw_console_pyramid(40)

# Startup code

if __name__ == "__main__":
    test_console_pyramid()
