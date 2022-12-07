from flask import Flask, render_template

app = Flask(__name__)

@app.route('/building_2')
def b_2():
    return render_template('index_b2_new.html')

@app.route('/building_3')
def b_3():
    return render_template('index_b3_new.html')

@app.route('/building_4')
def b_4():
    return render_template('index_b4_new.html')

@app.route('/building_5')
def b_5():
    return render_template('index_b5_new.html')

@app.route('/building_6')
def b_6():
    return render_template('index_b6_new.html')

@app.route('/building_7')
def b_7():
    return render_template('index_b7_new.html')

@app.route('/building_8')
def b_8():
    return render_template('index_b8_new.html')

@app.route('/building_9')
def b_9():
    return render_template('index_b9_new.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')