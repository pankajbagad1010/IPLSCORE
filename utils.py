import pickle
import json
import numpy as np
import config
class iplscore():
    def __init__(self, batting_team, bowling_team, overs, runs,wickets, runs_in_prev_5,wickets_in_prev_5):
        print("****** INIT Function *********")
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.overs = overs
        self.runs = runs
        self.wickets = wickets
        self.runs_in_prev_5 = runs_in_prev_5
        self.wickets_in_prev_5 = wickets_in_prev_5

def __load_saved_data(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        # with open(config.JSON_FILE_PATH,'r') as f:
        #     self.json_data = json.load(f)

def get_predicted_score(self):
    self.__load_saved_data()
    test_array = np.zeros([1,self.model.n_features_in_])
    test_array[0,0] = self.batting_team
    test_array[0,1] = self.bowling_team
    test_array[0,2] = self.overs
    test_array[0,3] = self.runs
    test_array[0,4] = self.wickets
    test_array[0,5] = self.runs_in_prev_5
    test_array[0,6] = self.wickets_in_prev_5

    predicted_score = np.around(self.model.predict(test_array)[0],3)
    return predicted_score