import xml.etree.ElementTree as ET
from datetime import datetime

def get_day_suffix(day):
    if 11 <= day <= 13:
        return "th"
    last_digit = day % 10
    if last_digit == 1:
        return "st"
    elif last_digit == 2:
        return "nd"
    elif last_digit == 3:
        return "rd"
    else:
        return "th"

def update_svg_file(svg_file, current_date):
    try:
        # Parse the SVG file
        tree = ET.parse(svg_file)
        root = tree.getroot()

        # Find the tspan element with id="dateToUpdate"
        tspan = root.find(".//{http://www.w3.org/2000/svg}tspan[@id='dateToUpdate']")

        if tspan is not None:
            # Update the tspan text with the current date
            tspan.text = current_date
            # Save the updated SVG file
            tree.write(svg_file)
            print(f"Successfully updated the SVG date to: {current_date}")
        else:
            print("Error: Could not find tspan element with id='dateToUpdate'")
    except FileNotFoundError:
        print(f"Error: The file {svg_file} was not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

try:
    # Get the current date in a human-readable format 
    now = datetime.now()
    day = now.day
    suffix = get_day_suffix(day)
    current_date = now.strftime("%A, %B {day}{suffix}, %Y")
    # Update both SVG files
    update_svg_file("banner.svg", current_date)
    update_svg_file("banner_light.svg", current_date)
except Exception as e:
    print(f"An error occurred: {str(e)}")





