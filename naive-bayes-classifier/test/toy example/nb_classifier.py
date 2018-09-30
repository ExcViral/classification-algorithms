# Implementation of naive bayes algorithm

# Import necessary libraries
import pandas as pd
import itertools

# ======================================================================================================================
# ===== Helper Functions ===============================================================================================
# ======================================================================================================================

def genCombinations(a, b):
    t = []
    for i in a:
        for j in b:
            t.append([i,j])
    return t

def genPM(feature, resp_vec):
    # f_r = list(zip(feature, resp_vec))
    # set_f_r = list(set(f_r))
    # count = [f_r.count(i) for i in set_f_r]
    # return list(zip(set_f_r, count))
    set_feature = list(set(feature))
    # print(set_feature)
    set_resp_vec = list(set(resp_vec))
    # print(set_resp_vec)
    # combinations = genCombinations(set_feature, set_resp_vec)
    # print(combinations)
    zipped_f_r = [[i,j] for i,j in zip(feature, resp_vec)]
    # print(zipped_f_r)
    # for i in combinations:
    #     count = zipped_f_r.count(i)
    #     i.append(count)
    # print(combinations)
    dict_pm = {}
    for i in set_feature:
        dict_pm[i] = {}
        for j in set_resp_vec:
            count_of_j = zipped_f_r.count([i,j])
            total_j = resp_vec.count(j)
            dict_pm[i][j] = count_of_j
            s = 'P(' + j +')'
            dict_pm[i][s] = count_of_j / total_j

    # print(dict_pm)
    return dict_pm

def genRV_PM(response_vector):
    dict_pm = {}
    for i in response_vec:
        c = response_vector.count(i)
        dict_pm[i] = {}
        dict_pm[i]['count'] = c
        dict_pm[i]['P('+i+')'] = c/len(response_vector)
    return dict_pm

# def predict(today):
#     # print(today)
#
#     # Predict for yes
#
#
#     # Predict for no

# ======================================================================================================================
# ===== Naive Bayes Classifier =========================================================================================
# ======================================================================================================================

# load dataset
data = pd.read_csv("dataset/toy_data.csv")
# print(data)

# seperate data into feature matrix and response vector
outlook = data['OUTLOOK'].values.tolist()
temperature = data['TEMPERATURE'].values.tolist()
humidity = data['HUMIDITY'].values.tolist()
windy = data['WINDY'].values.tolist()

features = [outlook, temperature, humidity, windy]
response_vec = data['PLAY GOLF'].values.tolist()

# calculating P(X_i|Y_i) for all features
outlook_pm = genPM(outlook, response_vec)
print(outlook_pm)
temperature_pm = genPM(temperature, response_vec)
print(temperature_pm)
humidity_pm = genPM(humidity, response_vec)
print(humidity_pm)
windy_pm = genPM(windy, response_vec)
print(windy_pm)

resp_pm = genRV_PM(response_vec)
print(resp_pm)

today = ['Sunny', 'Hot', 'Normal', 'F']
# predict(today)

# print(windy_pm['F']['P(Yes)'])

p_yes_today = outlook_pm[today[0]]['P(Yes)']*temperature_pm[today[1]]['P(Yes)']*humidity_pm[today[2]]['P(Yes)']*windy_pm[today[3]]['P(Yes)']*resp_pm['Yes']['P(Yes)']
print(p_yes_today)