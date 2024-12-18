import os
def create_parrain_data(file_path):
    parrain_data = []

    with open(file_path, 'r') as file:
        # Skip the header line
        next(file)

        for line in file:
            name, time, deleg, sprite = line.strip().split(',')
            parrain_dict = {
                "name": name,
                "time": int(time),
                "deleg": deleg.lower(),
                "sprite": sprite
            }
            parrain_data.append(parrain_dict)

    return parrain_data


# File path
file_path = os.path.join("data/parrainfile.txt")

# Create the list of dictionaries
parrain_data = create_parrain_data(file_path)
