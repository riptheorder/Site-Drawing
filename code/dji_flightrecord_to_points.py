import utm
import csv
import pandas as pd

# import tracks file
# input_file="~/Documents/anton_rtk/FinalsT5_2 CSV/FinalsT5_2_TRACKPOINTS.csv"
input_file="../data/DJIFlightRecord_2024-07-23_[14-33-43].csv"

# read in csv export of tracks from sw maps
flight_record = pd.read_csv(input_file, header=1)

# with open(input_file,'r') as in_f:
#     flight_record = pd.read_csv(input_file)
#     in_lines = in_f.readlines()[1:]


print(flight_record[["OSD.height [ft]", "OSD.latitude", "OSD.longitude"]])

flight_record["utm"] = flight_record[[ "OSD.latitude", "OSD.longitude"]].apply(lambda x: utm.from_latlon(x[1],x[0]), axis=1)

x = [f[0] for f in flight_record["utm"]]
y = [f[1] for f in flight_record["utm"]]
z = flight_record["OSD.height [ft]"]

flight_record["x"] = x
flight_record["y"] = y
flight_record["z"] = z

flight_record[["x", "y", "z"]].to_csv("drone_track.csv", index=False, header=False)