import tensorflow as tf
import utils.loading_util as lu
import os
import pandas as pd
import metadata as md
import numpy as np
import matplotlib.pyplot as mp
tf.compat.v1.enable_eager_execution()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def load(file = "2_14.csv"):
    """
    this loads the braking events from a file in the data folder
    """
    #load file
    file_path ="./data/" + file
    data = pd.read_csv(file_path , delimiter=",", index_col=0)
    data = data.reset_index(drop=True)

    #here the formating has to be done; creating the sequences for the state,environmental variables and the inputs
    listaa = []
    cols = [col for col in data.columns if col not in ["LWI_Lenkradwinkel.Angle.°.","EM1_IstMoment.Torque.Nm.","ESP_Bremsdruck.Pressure.bar."]]
    aa = data[cols]
    aa = aa.add_suffix(0)
        #print(aa)
    listaa.append(aa)
    for j in range(md.shift_range, 0, -1):
        cols = [col for col in data.columns if col not in ["LWI_Lenkradwinkel.Angle.°.","EM1_IstMoment.Torque.Nm.","ESP_Bremsdruck.Pressure.bar."]]
        aa = data[cols].shift(periods = j * md.down_sampling_factor)
        aa = aa.add_suffix(j)
        #print(aa)
        listaa.append(aa)
        del aa
    for j in range((md.input_length), 0, -1):
        aa = data[["LWI_Lenkradwinkel.Angle.°.","EM1_IstMoment.Torque.Nm.","ESP_Bremsdruck.Pressure.bar."]].shift(periods = j)
        aa = aa.add_suffix(j)
        #print(aa)
        listaa.append(aa)
        del aa
    data2 = pd.concat(listaa, axis = 1)

    input = data2.iloc[: , md.channels:]
    result = data2.iloc[: , 4:md.channels]
    return input, result

def predict(env, input, result, index_start, index_end):
    """
    needs: gym, environment, the data from a file and the start and end index the prediction is allowed to go through
    """
    total_reward = 0
    series=False
    predict_list=[]
    start = index_start
    end = index_start
    #start to go through file
    for i in range(index_start,index_end,md.down_sampling_factor):
        #checks if a braking event has ended; only possible if series = True / we already had atleast one prediction
        if (result.iloc[i].isna().any() == True or result.iloc[i+1].isna().any() == True) and series== True:
            break
        #starts the braking event if non nan row is found -> braking event has started
        elif input.iloc[i].isna().any() == True:
            start = start + md.down_sampling_factor
            end = end + md.down_sampling_factor
            continue 
        else:
            #preprocess the data into the correct format
            if series == False:
                features = np.reshape(input.iloc[i][:md.channels * (md.shift_range)].to_numpy(), [1,(md.shift_range)* md.channels])
            else:
                features = np.roll(features, (md.shift_range - 1) * md.channels)
                pos = md.channels * (md.shift_range - 1)
                np.put(features, [pos + 0,pos + 1,pos + 2,pos + 3], input.iloc[i][:7].to_numpy())
                np.put(features, [pos + 4,pos + 5,pos + 6,pos + 7,pos + 8,pos + 9,pos + 10], prediction_result)
            inputs = np.reshape(input.iloc[i][md.channels * (md.shift_range):].to_numpy(), [1,md.amount_of_inputs * (md.input_length)])


            #predict
            env.set_features(features)   
            prediction_result, reward, done, info = env.step(inputs)

            total_reward += reward
            #append data to dataframe for plotting
            df = pd.DataFrame([prediction_result.tolist()])
            df["Index"] = end
            predict_list.append(df)
            series=True
            end = end + md.down_sampling_factor

    #if braking event is over return al the relevant info
    predictions = pd.concat(predict_list, axis = 0)
    predictions = predictions.set_index('Index')
    rev = result.iloc[start:end,:]
    rev = rev[::md.down_sampling_factor]
    return predictions, rev, end, total_reward

def scale(predictions,rev):
    """
    rescaling the results
    """
    scaling_min, scaling_max = lu.load_scaling()

    predictions = predictions.mul((scaling_max[7:] - scaling_min[7:]), axis=1)
    predictions = predictions.add(scaling_min[7:], axis=1)

    rev = rev.mul((scaling_max[7:] - scaling_min[7:]), axis=1)
    rev = rev.add(scaling_min[7:], axis=1)

    return predictions,rev
def plot(predictions,rev):
    """
    ploting the prediction and the reference data
    """

    for i in range(0,len(predictions.columns)):
        mp.subplot(2, 4, i+1)
        mp.plot(rev.iloc[:,i] , label='True')
        mp.plot(predictions.iloc[:,i] , label='Prediction')
        mp.legend(loc="upper left")
        mp.title(rev.iloc[:,i].name)

    mp.show()