import tkinter as tk
import math

def draw_clockwise_arrow(canvas, center_x, center_y, radius, start_angle, extent):
    # Draw the arc
    canvas.create_arc(center_x - radius, center_y - radius,
                      center_x + radius, center_y + radius,
                      start=start_angle, extent=extent,
                      style=tk.ARC, width=2, outline='black')
    
    # Calculate the end position of the arc
    end_angle = start_angle + extent
    end_x = center_x + radius * math.cos(math.radians(end_angle))
    end_y = center_y - radius * math.sin(math.radians(end_angle))
    
    # Calculate arrowhead points
    arrow_length = 10  # Length of the arrowhead
    arrow_angle1 = math.radians(end_angle + 30)  # Angle for the first line of the arrowhead
    arrow_angle2 = math.radians(end_angle - 30)  # Angle for the second line of the arrowhead
    
    # Points for the lines
    arrow_x1 = end_x + arrow_length * math.cos(arrow_angle1)
    arrow_y1 = end_y - arrow_length * math.sin(arrow_angle1)
    arrow_x2 = end_x + arrow_length * math.cos(arrow_angle2)
    arrow_y2 = end_y - arrow_length * math.sin(arrow_angle2)
    
    # Draw the arrowhead as two lines
    canvas.create_line(end_x, end_y, arrow_x1, arrow_y1, fill='black', width=2)
    canvas.create_line(end_x, end_y, arrow_x2, arrow_y2, fill='black', width=2)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()
    
    # Draw a clockwise circular arrow
    draw_clockwise_arrow(canvas, 200, 200, 100, 45, 270)
    
    root.mainloop()
