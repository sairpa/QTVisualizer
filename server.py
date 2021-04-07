from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/plot')
def plot():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]

    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response
    
if __name__ == "__main__":
    app.run(debug=True)