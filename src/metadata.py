# Channel 1:': 'LWI_Lenkradwinkel.Angle.°.', 'Channel 2:': 'LWI_VZ_Lenkradwinkel.Index..', 'Channel 3:': 'MO_Mom_Ist_Summe.Torque.Nm.', 
# 'Channel 4:': 'EM1_IstMoment.Torque.Nm.', 'Channel 5:': 'EM1_IstDrehzahl.Index..', 'Channel 6:': 'EM1_IstSpannung.Voltage.V.', 
# 'Channel 7:': 'EM2_IstMoment.Torque.Nm.', 'Channel 8:': 'EM2_IstDrehzahl.Index..', 'Channel 9:': 'EM2_IstSpannung.Voltage.V.', 
# 'Channel 10:': 'TS_Faktor_Radmomente.Index..', 'Channel 11:': 'TS_MomRad_Ist.Torque.Nm.', 'Channel 12:': 'TS_MomRad_Wunsch.Torque.Nm.', 
# 'Channel 13:': 'ESC_Bremsdruck_Modell.Pressure.bar.', 'Channel 14:': 'ESP_v_Signal.Speed.km/h.', 
# 'Channel 15:': 'ESP_Querbeschleunigung.Virtual Quantity (m/s2).m/s2.', 
# 'Channel 16:': 'ESP_Laengsbeschl.Virtual Quantity (m/s2).m/s2.', 'Channel 17:': 'ESP_Gierrate.Speed of Rotation.°/s.', 
# 'Channel 18:': 'ESP_VZ_Gierrate.Index..', 'Channel 19:': 'ESP_Bremsdruck.Pressure.bar.', 'Channel 20:': 'ESP_Fahrer_bremst.Index..', 
# 'Channel 21:': 'ESP_VL_Fahrtrichtung.Index..', 'Channel 22:': 'EBKV_Bremspedalweg.Relative Proportion.%.', 'Channel 23:': 'MO_Anzeige_Rekuperation.Index..', 
# 'Channel 24:': 'MO_Rekuperationsstufe.Index..', 'Channel 25:': 'BCM1_Rueckfahrlicht_Schalter.Index..', 'Channel 26:': 'BCM1_Aussen_Temp_ungef.Temperature.°C.', 
# 'Channel 27:': 'ESP_Gierrate_Offset.Speed of Rotation.°/s.', 'Channel 28:': 'ESP_Querbeschleunigung_Offset.Virtual Quantity (m/s2).m/s2.', 
# 'Channel 29:': 'ESP_Laengsbeschleunigung_Offset.Virtual Quantity (m/s2).m/s2.', 'Channel 30:': 'KBI_Kilometerstand.Length.km.', 
# 'Channel 31:': 'TSK_Fahrzeugmasse_02.Dynamic Mass.kg.', 'Channel 32:': 'TSK_Steigung_02.Angle.°.', 
# 'Channel 33:': 'MO_Rekuperation_Ges_EM.Virtual Quantity (Ws).Ws.', 'Channel 34:': 'MO_Drehzahl_EM.Index..', 
# 'Channel 35:': 'EM2_Rekuperation.Virtual Quantity (Ws).Ws.', 'Channel 36:': 'T_VL_1.Temperature.°C.', 'Channel 37:': 'T_VR_1.Temperature.°C.', 
# 'Channel 38:': 'T_HL_1.Temperature.°C.', 'Channel 39:': 'T_HR_1.Temperature.°C.', 'Channel 40:': 'Status_VL_Batterie.Index..', 
# 'Channel 41:': 'Status_VL_Fehler.Index..', 'Channel 42:': 'Status_VR_Batterie.Index..', 'Channel 43:': 'Status_VR_Fehler.Index..', 
# 'Channel 44:': 'Status_HL_Batterie.Index..', 'Channel 45:': 'Status_HL_Fehler.Index..', 'Channel 46:': 'Status_HR_Batterie.Index..', 
# 'Channel 47:': 'Status_HR_Fehler.Index..', 'Channel 48:': 'L_05969_Luftfeuchte.Relative Proportion.%.', 'Channel 49:': 'DruckVL.Pressure.bar.', 
# 'Channel 50:': 'DruckVR.Pressure.bar.', 'Channel 51:': 'DruckHL.Pressure.bar.', 'Channel 52:': 'DruckHR.Pressure.bar.', 
# 'Channel 53:': 'LWI_berechnet.Angle.°.', 'Channel 54:': 'Geschwindigkeit_berechnet.Speed.km/h.', 'Comment:': '', '': ''


selected_channels = [1,2,4,19,48,26,13,32,11,15,17,18,36,38,54]
shift_range = 6
down_sampling_factor = 4
frequency = 100 / down_sampling_factor
amount_of_inputs = 3
car=14
extra_channels = 1
delay = 10
input_length = down_sampling_factor + delay
#selected channels + acceleration
channels = extra_channels + len(selected_channels) - 2 - 3 #-zwei weil zwei inputs nur vorzeichen sind und die nachher wieder rausgenommen werden, minus drei für die inputs
