import os
import random
import sys
from flask import Flask, render_template
import openai



app = Flask(__name__)
app.template_folder = './'  # Set the template folder to the current directory

def calculate_text_color(background_color):
    # Calculate the perceived brightness of the background color
    r, g, b = tuple(int(background_color[i:i+2], 16) for i in (1, 3, 5))
    brightness = (r * 299 + g * 587 + b * 114) / 1000

    # Choose the text color based on the background brightness
    if brightness > 128:
        return 'black'
    else:
        return 'white'

@app.route('/')
def home():
    color_code = os.environ.get('BACKGROUND_COLOR', '#0000FF')  # Default color is blue

    facts = [
        "Artificial Intelligence (AI) is a branch of computer science that deals with the creation and development of intelligent machines.",
        "Machine Learning is a subset of AI that focuses on giving machines the ability to learn and improve from data without being explicitly programmed.",
        "Deep Learning is a subfield of machine learning that uses neural networks with multiple layers to learn and make predictions.",
        "AI has applications in various fields such as healthcare, finance, transportation, and entertainment.",
        "Ethical considerations are important in the development and deployment of AI systems to ensure fairness, transparency, and accountability."
    ]
    random_fact = random.choice(facts)

    text_color = calculate_text_color(color_code)

    return render_template('index.html', background_color=color_code, text_color=text_color, fact=random_fact)

if __name__ == '__main__':
    # Set the BACKGROUND_COLOR environment variable from the command line argument
    if len(sys.argv) > 1:
        os.environ['BACKGROUND_COLOR'] = sys.argv[1]
    app.run()
