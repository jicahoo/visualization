import csv
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def convert_to_float(str_num):
    try:
        ret = float(str_num)
        return True, ret
    except ValueError:
        return False, None


def np_array_summary(np_array):
    return 'shape: %s, min: %s, max: %s, mean: %s' % (np_array.shape, np_array.min(), np_array.max(), np_array.mean())


def get_heap_data(x_np_data, y_np_data):
    x_hist_values, x_edeges = np.histogram(x_np_data, bins=40)
    y_hist_values, y_edges = np.histogram(y_np_data, bins=40)
    heap_map = []
    l = x_np_data
    sorted = all(l[i] <= l[i + 1] for i in xrange(len(l) - 1))

    index_x_np_data = 0
    for i in range(1, len(x_edeges)):
        y_in_range = []
        for j, val in enumerate(x_np_data):
            if val >= x_edeges[i - 1] and val < x_edeges[i]:
                y_in_range.append(y_np_data[j, :])
        y_in_range_flatten = []
        for np_row in y_in_range:
            y_in_range_flatten += np_row.tolist()
        y_local_hist_values, y_edges = np.histogram(np.asarray(y_in_range_flatten), bins=y_edges)
        heap_map.append(y_local_hist_values)
    heap_map_np = np.asarray(heap_map)
    return heap_map_np, x_edeges, y_edges

def get_x_y_data():
    csv_file_path = '2d_histogram.csv'
    rows = []
    with open(csv_file_path, 'rb') as f:
        reader = csv.reader(f)
        rows = [x for x in reader]
    print len(rows)
    # numpy.loadtxt(csv_file_path)
    # numpy.loadtxt(csv_file_path, delimiter=',', skiprows=1)
    print rows[0]
    y_float_rows = []
    x_float_values = []
    for i, row in enumerate(rows[1:-1]):
        float_row = []
        x_float_values.append(float(row[0]))
        for j, cell in enumerate(row[1:]):
            is_float, float_value = convert_to_float(cell)
            if not is_float:
                try:
                    float_value = float_row[j - 1]
                except ValueError:
                    print '(%s,%s)' % (i, j)
            float_row.append(float_value)
        y_float_rows.append(float_row)
    y_np_data = np.asarray(y_float_rows)
    x_np_data = np.asarray(x_float_values)
    return x_np_data, y_np_data


if __name__ == '__main__':
    x_np_data, y_np_data = get_x_y_data()
    heatmap, xedges, yedges = get_heap_data(x_np_data, y_np_data)
    print  heatmap
    print  xedges
    print yedges
    xedges = xedges*100
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.imshow(heatmap, extent=extent)
    plt.colorbar()
    plt.title('Draft: Need refine.')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


