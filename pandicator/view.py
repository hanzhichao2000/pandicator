'''
TODO: Docs
TODO: check box
TODO: draw button
TODO: balanced picture

'''

import matplotlib.pyplot as plt
from matplotlib import widgets
from pylab import hist

from pandicator import common as com

class Interact:

    def __init__(self, data):
        self.data = data
        self.date = data.index
        self.imin = 0
        self.imax = len(self.date)

        self.col_li = data.columns

        self.selected_up = self.col_li[0]
        self.selected_dn = self.col_li[1]

        fig = plt.figure()

        main_left = 0.25; main_width= 0.7
        side_left = 0.05; side_width = 0.15
        up_top = 0.05; up_height = 0.65
        down_top = 0.75; down_height = 0.2
        side_height = 0.035*len(self.col_li)

        rect0 = [main_left, 1-(up_top+up_height), main_width, up_height]
        rect1 = [main_left, 1-(down_top+down_height), main_width, down_height]
        rect2 = [side_left, 1-(up_top+side_height), side_width, side_height]
        rect3 = [side_left, 1-(down_top+side_height), side_width, side_height]

        self.ax0 = fig.add_axes(rect0)
        self.ax1 = fig.add_axes(rect1, sharex=self.ax0)
        self.ax2 = fig.add_axes(rect2)
        self.ax3 = fig.add_axes(rect3)

        self.set_side_up_radio()
        self.set_side_down_radio()

        self.fig_up = []
        self.fig_dn = []

        self.update()
        plt.show()

    def set_side_up_radio(self):
        def _fn(label):
            self.selected_up = label
            self.update()
        self.radio_up = widgets.RadioButtons(self.ax2, self.col_li, 0)
        self.radio_up.on_clicked(_fn)

    def set_side_down_radio(self):
        def _fn(label):
            self.selected_dn = label
            self.update()
        self.radio_dn = widgets.RadioButtons(self.ax3, self.col_li, 1)
        self.radio_dn.on_clicked(_fn)

    def clear(self):
        for _ in self.fig_up: _.remove()
        self.fig_up = []
        for _ in self.fig_dn: _.remove()
        self.fig_dn = []

    def update(self):
        self.clear()
        self.ax0.set_title(self.selected_up)
        self.ax1.set_title(self.selected_dn)
        y0 = self.data[self.selected_up]
        y1 = self.data[self.selected_dn]
        self.ax0.set_ylim(bottom=y0.min(), top=y0.max())
        self.ax1.set_ylim(bottom=y1.min(), top=y1.max())
        self.fig_up = self.ax0.plot(self.date[self.imin: self.imax+1], y0[self.imin: self.imax+1], 'b')
        self.fig_dn = self.ax1.plot(self.date[self.imin: self.imax+1], y1[self.imin: self.imax+1], 'r')
        plt.draw()


def dist(arg, bins=30):
    arg = com.safe_series(arg)
    hist(arg.dropna(), bins=bins)
    plt.show()
