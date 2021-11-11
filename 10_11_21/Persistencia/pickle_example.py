"""Pickle example"""
import pickle

sens_1 = ["pos_1", "photo_1", "io_1"]
sens_2 = ["pos_2", "photo_2"]
cells = [
        {"robot": "IRB", "sensor": sens_1}
        {"robot": "UR3", "sensor": sens_2}
        ]
    for cell in cells
        print("\nCell; ","Robot: ", cell["robot"])
        for sensor in cell ["sensor"]
            print("  ", "sensor: ", sensor)

pickle.dump(cells, open("cells.data", "wb"))
cells = []
print("\ncells:\n", cells)
cells = pickle.load(open("cells.data", "rb"))
print("\ncells:\n", cells)

