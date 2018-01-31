# Datacamp_RATP_Velib

The aim was to have, for each station, the numBikesAvailable updated every 6 minutes from 25 hours before to 1 hour before the actual time and predict if the station would be near empty (status 0), near full (status 2) or filled correctly (status 1) at the actual time. This would have allowed the company to predict where to take Velibs and where to put them before stations were in fact empty or full.
We would have had a table of size 201 (number of available stations as of 30 january) * 240 (24 * 60 / 6 number of time stamps).
Due to technical issues to extract real-time data for 24 hours, we didn't manage to get a training set and a test set.
