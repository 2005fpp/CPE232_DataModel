from nbconvert import HTMLExporter
import nbformat

NOTEBOOK_PATH = 'WEEK4/Lab3_Data_Preparation.ipynb'
HTML_PATH = 'WEEK4/report/Lab3_Data_Preparation.html'

# Load your notebook file with UTF-8 encoding
with open(NOTEBOOK_PATH, encoding="utf-8") as f:
    notebook_content = nbformat.read(f, as_version=4)

# Initialize the HTML Exporter
html_exporter = HTMLExporter()

# Convert the notebook to HTML
(body, resources) = html_exporter.from_notebook_node(notebook_content)

# Save the output HTML file
with open(HTML_PATH, 'w', encoding="utf-8") as output_file:
    output_file.write(body)