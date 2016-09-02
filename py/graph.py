import pygal
from flask import Flask
from pygal.style import DarkSolarizedStyle
import math
import random

#getting started with pygal
# http://www.blog.pythonlibrary.org/2015/04/16/using-pygal-graphs-in-flask/

app = Flask(__name__)

@app.route('/')
def getGraphed():
	title="testing Graph"
	bar_chart = pygal.Bar(width=1200, height=600, explicit_size=True, title=title, style=DarkSolarizedStyle)
	r = random.randint(1,1000)
	bar_chart.x_labels = "cos/tan/sin of random {:d}".format(r)
	bar_chart.add("Cos of r", math.cos(r))
	bar_chart.add("sin of r", math.sin(r))
	bar_chart.add("tan of r", math.tan(r))

	title="cos of random"
	cos_chart = pygal.Bar(width=1200, height=600, explicit_size=True, title=title, style=DarkSolarizedStyle)
	r = random.randint(1,1000)
	cos_chart.x_labels = "cos of random {:d}".format(r)
	cos_chart.add("Cos of r", math.cos(r))

	title="sin of random"
	sin_chart = pygal.Bar(width=1200, height=600, explicit_size=True, title=title, style=DarkSolarizedStyle)
	r = random.randint(1,1000)
	sin_chart.x_labels = "sin of random {:d}".format(r)
	sin_chart.add("sin of r", math.sin(r))

	title="tan of random"
	tan_chart = pygal.Bar(width=1200, height=600, explicit_size=True, title=title, style=DarkSolarizedStyle)
	r = random.randint(1,1000)
	tan_chart.x_labels = "tan of random {:d}".format(r)
	tan_chart.add("tan of r", math.tan(r))

	html="""<html><head><title>{:s}</title></head><body><br></br>{:s}<br></br>{:s}<br></br>{:s}<br></br>{:s}<br></br></body></html>""".format(title, bar_chart.render(), cos_chart.render(), sin_chart.render(), tan_chart.render())
	return html

if __name__ == '__main__':    
    app.run(host="0.0.0.0", port=1234, debug=False, use_reloader=True)
