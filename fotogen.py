import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the image folder path relative to the script's location
image_folder = os.path.join(script_dir, "namefrom")
output_file = os.path.join(script_dir, "generated_images.txt")

# Check if the 'images' folder exists
if not os.path.isdir(image_folder):
    print(f"Error: The folder '{image_folder}' does not exist in {script_dir}.")
    exit()

# Supported image extensions
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

# Path to placeholder image
placeholder_image = "assets/placeholder.png"

# Generate HTML for each image in the folder
html_output = []
for image_name in os.listdir(image_folder):
    if os.path.splitext(image_name)[1].lower() in image_extensions:
        # Remove leading underscores
        clean_image_name = image_name.lstrip('_')
        html_output.append(f'''
        <div class="gallery-item">
            <div class="image-container">
                <img class="placeholder" src="{placeholder_image}" data-src="images/{clean_image_name}" alt="{clean_image_name}">
            </div>
        </div>
        ''')

# Save generated HTML snippets to a text file
with open(output_file, "w") as f:
    f.write("\n".join(html_output))

print(f"HTML snippets for images have been generated in '{output_file}'.")
