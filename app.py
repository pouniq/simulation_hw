from flask import Flask, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    waiting = np.random.randint(1, 6, 30)
    time_served = np.random.randint(1, 6, 30)

    df = pd.DataFrame({'wait': waiting, 'time': time_served})

    # convert to html table
    table_html = df.to_html(classes="table table-striped", index=False)

    return render_template("index.html", table=table_html)

if __name__ == "__main__":
    app.run(debug=True)
