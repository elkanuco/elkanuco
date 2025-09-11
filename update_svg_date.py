import xml.etree.ElementTree as ET
from datetime import datetime

# Define the SVG file path
svg_file = "banner.svg"

# Get the current date in a human-readable format (e.g., September 11, 2025)
current_date = datetime.now().strftime("%B %d, %Y")

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