import utm
import csv

input_file="FinalsT5_2 CSV/FinalsT5_2_TRACKPOINTS.csv"

# read in csv export of tracks from sw maps
with open(input_file,'r') as in_f:
    in_lines = in_f.readlines()[1:]


tracks = {}
shared_origin = []
# origin in [lat, long, altitude]
# points are defined relative to the shared origin at 0, 0, 0

for i, line in enumerate(in_lines):
    line_array = line.split(",")
    t_name = line_array[0]
    

    # for the first line of each track name
    if t_name not in tracks.keys():
        tracks[t_name] = {"origin" :[], "points" :[]}
        
        # convert origin to utm and svae
        origin_utm = utm.from_latlon(float(line_array[3]), float(line_array[4]))
        
        # save shared_origin for the first processed track
        if i==0:
            shared_origin = [origin_utm[0], origin_utm[1], float(line_array[5])]
        
        # save origin with offsets relative to the shared_origin
        tracks[t_name]["origin"] = [origin_utm[0] - shared_origin[0], origin_utm[1] - shared_origin[1], float(line_array[5]) - shared_origin[2]]

        # create first point as origin
        tracks[t_name]["points"].append(tracks[t_name]["origin"])

    else:
        # convert our lat_lon point to utm
        point_utm = utm.from_latlon(float(line_array[3]), float(line_array[4]))
        
        # grab origin point
        # origin_utm = tracks[t_name]["origin"]
        origin_utm = shared_origin

        # save the relative position
        tracks[t_name]["points"].append([point_utm[0]-origin_utm[0], 
                                        point_utm[1]-origin_utm[1], 
                                        float(line_array[5])-origin_utm[2]])
    

# write pointfiles for each track name
for track in tracks.keys():
    with open(f"{input_file.split('/')[0]}/track_{track}.csv", 'w') as out_f:
        csvwriter = csv.writer(out_f)
        for point in tracks[track]["points"]:
            csvwriter.writerow(point)