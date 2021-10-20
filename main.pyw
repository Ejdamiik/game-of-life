import json
import visualize
import matrix_handle


# Parse json
with open("config.json", "r") as f:
    config = json.load(f)

cell_color = tuple(config["color_cells"])
bg_color = tuple(config["color_bg"])
m, n = config["dimensions"]
width, height = config["screen_size"]
mode = config["mode"]
delay = config["delay"]	# ms


m = matrix_handle.get_random_matrix(m, n)

if mode == 1:
	mv = visualize.MatrixVizualizer(m, 1, delay, bg_color, cell_color, width, height)
	mv.run_winteract()
elif mode == 2:
	mv = visualize.MatrixVizualizer(m, 2, delay, bg_color, cell_color, width, height)
	mv.run_interact()
else:
	mv = visualize.MatrixVizualizer(m, 3, delay, bg_color, cell_color, width, height)
	mv.run_interact()