from flask import Flask, render_template, jsonify

app = Flask(__name__)


projects = [{'title': 'First Project',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'image_url': '../static/first-img.jpg',
            'project_url': 'https://github.com/Ankit4j/web-scraper'
            },
           {'title': 'Second Project',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'image_url': '../static/second-img.jpg',
            'project_url': 'https://github.com/Ankit4j/chrome-extension'
            },
           {'title': 'Third Project',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
            'image_url': '../static/third-img.jpg',
            'project_url': 'https://github.com/Ankit4j/drum-kit'
    }
]



@app.route("/")
def get_home():
    return render_template("home.html", projects = projects)

@app.route("/projects")
def get_projects():
    return jsonify(projects)

if __name__ == "__main__":
    app.run(debug=True)