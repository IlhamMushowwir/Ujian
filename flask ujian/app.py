from flask import Flask,render_template
from plots import dist_mpg,dist_horse
from cleaning_data import data_mpg
app = Flask(__name__)

# ROUTE
# RENDER TEMPLATE
# RENDER TEMPLATE WITH VARIABLE

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')
def data():
    data = data_mpg().head()
    return render_template('table_data.html' , data=data)


@app.route('/plots')
def plots():
    plot1 = dist_mpg()
    plot2 = dist_horse()
    return render_template('plots.html' , data=[plot1,plot2])

if __name__ == '__main__':
    app.run(debug=True, port=2000)