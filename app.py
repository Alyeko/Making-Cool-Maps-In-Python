from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (5.6, 26.17)
    folium_map = folium.Map(location=start_coords, zoom_start=3.4)
    folium_map.save('templates/map.html')
    return render_template('index.html')


@app.route('/map')
def map():
    return render_template('the_map.html')

if __name__ == '__main__':
    app.run(debug=True)