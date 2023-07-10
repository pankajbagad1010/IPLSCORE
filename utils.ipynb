{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "65560963",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'config'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_13776\\1439589444.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mjson\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mconfig\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0miplscore\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'config'"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "import json\n",
    "import numpy as np\n",
    "import config\n",
    "\n",
    "class iplscore():\n",
    "    def __init__(self, batting_team, bowling_team, overs, runs,wickets, runs_in_prev_5,wickets_in_prev_5):\n",
    "        print(\"****** INIT Function *********\")\n",
    "        self.batting_team = batting_team\n",
    "        self.bowling_team = bowling_team\n",
    "        self.overs = overs\n",
    "        self.runs = runs\n",
    "        self.wickets = wickets\n",
    "        self.runs_in_prev_5 = runs_in_prev_5\n",
    "        self.wickets_in_prev_5 = wickets_in_prev_5\n",
    "        \n",
    "    def __load_saved_data(self):\n",
    "        with open(config.MODEL_FILE_PATH,'rb') as f:\n",
    "            self.model = pickle.load(f)\n",
    "            \n",
    "        with open(config.JSON_FILE_PATH,'r') as f:\n",
    "            self.json_data = json.load(f)\n",
    "    \n",
    "    def get_predicted_score(self):\n",
    "        self.__load_saved_data()\n",
    "        \n",
    "        test_array = np.zeros([1,self.model.n_features_in_])\n",
    "        test_array[0,0] = self.batting_team\n",
    "        test_array[0,1] = self.bowling_team\n",
    "        test_array[0,2] = self.overs\n",
    "        test_array[0,3] = self.runs\n",
    "        test_array[0,4] = self.wickets\n",
    "        test_array[0,5] = self.runs_in_prev_5\n",
    "        test_array[0,6] = self.wickets_in_prev_5\n",
    "\n",
    "\n",
    "        predicted_score = np.around(self.model.predict(test_array)[0],3)\n",
    "        return predicted_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf170fd3",
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
