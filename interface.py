{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c558ade3",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'utils'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_12828\\1742174161.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mflask\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mFlask\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mjsonify\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrender_template\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mredirect\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl_for\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mutils\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0miplscore\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mconfig\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mapp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mFlask\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m__name__\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'utils'"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify, render_template, redirect, url_for\n",
    "from utils import iplscore\n",
    "import config\n",
    "import traceback\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/ipsscore')\n",
    "def home1():\n",
    "    return render_template('iplscore.html')\n",
    "\n",
    "@app.route('/ipl', methods = ['GET', 'POST'])\n",
    "def predict_score():\n",
    "    try:\n",
    "        if request.method == 'GET':\n",
    "            print(\"+\"*50)\n",
    "            data = request.args.get\n",
    "            print(\"Data :\",data)\n",
    "            batting_team = data('batting_team')\n",
    "            bowling_team = data('bowling_team')\n",
    "            overs = int(data('overs'))\n",
    "            runs = int(data('runs'))\n",
    "            wickets = int(data('wickets'))\n",
    "            runs_in_prev_5 = int(data('runs_in_prev_5'))\n",
    "            wickets_in_prev_5 = int(data('wickets_in_prev_5'))\n",
    "            \n",
    "\n",
    "            Obj = iplscore(batting_team, bowling_team, overs, runs,wickets, runs_in_prev_5,wickets_in_prev_5)\n",
    "            pred_score = Obj.get_predicted_score()\n",
    "            \n",
    "            return render_template('iplscore.html', prediction = pred_score)\n",
    "       \n",
    "        elif request.method == 'POST':\n",
    "            print(\"*\"*40)\n",
    "            data = request.form.get\n",
    "            print(\"Data :\",data)\n",
    "            batting_team = data('batting_team')\n",
    "            bowling_team = data('bowling_team')\n",
    "            overs = int(data('overs'))\n",
    "            runs = int(data('runs'))\n",
    "            wickets = int(data('wickets'))\n",
    "            runs_in_prev_5 = int(data('runs_in_prev_5'))\n",
    "            wickets_in_prev_5 = int(data('wickets_in_prev_5'))\n",
    "            \n",
    "\n",
    "            Obj = iplscore(batting_team, bowling_team, overs, runs,wickets, runs_in_prev_5,wickets_in_prev_5)\n",
    "            pred_score = Obj.get_predicted_score()\n",
    "            \n",
    "            return render_template('iplscore.html', prediction = pred_score)\n",
    "\n",
    "    except:\n",
    "        print(traceback.print_exc())\n",
    "        return redirect(url_for('ipsscore'))\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(host='0.0.0.0', port=config.PORT_NUMBER)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "869d13ba",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
