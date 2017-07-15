import csv

import numpy as np
from matplotlib import patches
from scipy import stats
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


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
    print len(heap_map)
    heap_map_np = np.asarray(heap_map)
    return np.flipud(np.transpose(heap_map_np)), x_edeges, y_edges


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


def gauss(x, *p):
    A, mu, sigma = p
    return A * np.exp(-(x - mu) ** 2 / (2. * sigma ** 2))


def draw_y():
    x_np_data, y_np_data = get_x_y_data()
    # for i in range(x_np_data.shape[0]):
    y_i = y_np_data[704,]
    print y_i
    plt.plot(y_i)
    # plt.plot(y_i)
    plt.hist(y_i)
    plt.title("Gaussian Histogram")
    plt.show()


def gaussian_fitting(x_np_data, y_np_data):
    # It seems that it doesn't conform to Normal Distribution.
    print 'gaussian_fitting'
    print x_np_data.shape
    print y_np_data.shape
    print x_np_data.shape[0]
    print y_np_data[0,]

    for i in range(x_np_data.shape[0]):
        y_i = y_np_data[i,]
        p0 = (1., 0., 1.)
        hist, bin_edges = np.histogram(y_i, density=True)
        bin_centres = (bin_edges[:-1] + bin_edges[1:]) / 2
        try:
            coeff, var_matrix = curve_fit(gauss, bin_centres, hist, p0=p0, maxfev=1000)
        except Exception:
            continue
        print str(i) + ' Su' * 100


def solution_a():
    x_np_data, y_np_data = get_x_y_data()
    gaussian_fitting(x_np_data, y_np_data)
    heatmap, xedges, yedges = get_heap_data(x_np_data, y_np_data)
    print  heatmap
    print  xedges
    print yedges
    xedges = xedges
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.imshow(heatmap, extent=extent, aspect='auto')
    plt.colorbar()
    plt.title('Draft: Need refine.')
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()


def solution_b():
    x_np_data, y_np_data = get_x_y_data()
    heatmap, xedges, yedges = get_heap_data(x_np_data, y_np_data)
    print  heatmap
    print  xedges
    print yedges
    xedges = xedges
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    # Create figure and axes
    fig, ax = plt.subplots(1)

    print type(ax)
    # Display the image
    ax.imshow(heatmap, extent=extent, aspect='auto')

    # Create a Rectangle patch
    rect = patches.Rectangle((50, 100), 40, 30, linewidth=10, edgecolor='r', facecolor='none')

    someX, someY = 0.5, 0.5
    ax.add_patch(patches.Rectangle((someX - 0.1, someY - 0.1), 0.2, 20,
                                   alpha=1, facecolor='white'))

    # print ax.plot([-0.5,0.5],[0,20])
    # Add the patch to the Axes
    # ax.add_patch(rect)

    plt.show()


def solution_c():
    x_np_data, y_np_data = get_x_y_data()
    heatmap, xedges, yedges = get_heap_data(x_np_data, y_np_data)
    for line in heatmap:
        print list(line)
    print xedges
    print yedges
    xedges = xedges
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.imshow(heatmap, extent=extent, aspect='auto')
    plt.colorbar()
    plt.title('Version 1.0')
    axes = plt.gca()
    print axes
    # axes.plot([-0.5, 0.5], [0, 20], 'r')
    axes.set_ylim(top=yedges[-1], bottom=yedges[0])
    # axes.
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


if __name__ == '__main__':
    solution_c()
