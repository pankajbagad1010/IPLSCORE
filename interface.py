from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import iplscore
import config
import traceback
app = Flask(__name__)

@app.route('/')
def home1():
  return render_template('iplscore.html')

@app.route('/ipl', methods = ['GET', 'POST'])
def predict_score():
    try:
        if request.method == 'GET':
            print("+"*50)
            data = request.args.get
            print("Data :",data)
            batting_team = data('batting_team')
            bowling_team = data('bowling_team')
            overs = int(data('overs'))
            runs = int(data('runs'))
            wickets = int(data('wickets'))
            runs_in_prev_5 = int(data('runs_in_prev_5'))
            wickets_in_prev_5 = int(data('wickets_in_prev_5'))

            Obj = iplscore(batting_team, bowling_team, overs, runs,wickets, runs_in_prev_5,wickets_in_prev_5)
            pred_score = Obj.get_predicted_score()
            return render_template('iplscore.html', prediction = pred_score)

        elif request.method == 'POST':
                print("*"*40)
                data = request.form.get
                print("Data :",data)
                batting_team = data('batting_team')
                bowling_team = data('bowling_team')
                overs = int(data('overs'))
                runs = int(data('runs'))
                wickets = int(data('wickets'))
                runs_in_prev_5 = int(data('runs_in_prev_5'))
                wickets_in_prev_5 = int(data('wickets_in_prev_5'))


                Obj = iplscore(batting_team, bowling_team, overs, runs,wickets, runs_in_prev_5,wickets_in_prev_5)
                pred_score = Obj.get_predicted_score()
                return render_template('iplscore.html', prediction = pred_score)

    except:
    
            print(traceback.print_exc())
            return redirect(url_for('home1'))

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=config.PORT_NUMBER)