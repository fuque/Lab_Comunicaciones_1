#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: PruebaPAM L1A
# Author: labcom
# GNU Radio version: v3.8.2.0-57-gd71cd177

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from ModuladorPAM import ModuladorPAM  # grc-generated hier_block
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class PruebaPAM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "PruebaPAM L1A")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("PruebaPAM L1A")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "PruebaPAM")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
        self.fs = fs = samp_rate/100
        self.fm = fm = fs/10
        self.W = W = 25
        self.D3 = D3 = 75
        self.D2 = D2 = 50
        self.D1 = D1 = 25

        ##################################################
        # Blocks
        ##################################################
        self._W_range = Range(0, 50, 1, 25, 200)
        self._W_win = RangeWidget(self._W_range, self.set_W, 'Ancho del pulso', "counter_slider", int)
        self.top_grid_layout.addWidget(self._W_win)
        self._D3_range = Range(0, 100, 1, 75, 200)
        self._D3_win = RangeWidget(self._D3_range, self.set_D3, 'D3', "counter_slider", int)
        self.top_grid_layout.addWidget(self._D3_win)
        self._D2_range = Range(0, 100, 1, 50, 200)
        self._D2_win = RangeWidget(self._D2_range, self.set_D2, 'D2', "counter_slider", int)
        self.top_grid_layout.addWidget(self._D2_win)
        self._D1_range = Range(0, 100, 1, 25, 200)
        self._D1_win = RangeWidget(self._D1_range, self.set_D1, 'D1', "counter_slider", int)
        self.top_grid_layout.addWidget(self._D1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024*4, #size
            samp_rate, #samp_rate
            "", #name
            4 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_delay_0_0_0_0 = blocks.delay(gr.sizeof_float*1, D3)
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_float*1, D2)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, D1)
        self.analog_sig_source_x_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, fm, 1, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fm, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, fm, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fm, 1, 0, 0)
        self.ModuladorPAM_0_2_0_0 = ModuladorPAM(
            D=W,
            Fs=fs,
            Samp_rate=samp_rate,
        )
        self.ModuladorPAM_0_2_0 = ModuladorPAM(
            D=W,
            Fs=fs,
            Samp_rate=samp_rate,
        )
        self.ModuladorPAM_0_2 = ModuladorPAM(
            D=W,
            Fs=fs,
            Samp_rate=samp_rate,
        )
        self.ModuladorPAM_0_0 = ModuladorPAM(
            D=W,
            Fs=fs,
            Samp_rate=samp_rate,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.ModuladorPAM_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.ModuladorPAM_0_2, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.ModuladorPAM_0_2_0, 0), (self.blocks_delay_0_0_0, 0))
        self.connect((self.ModuladorPAM_0_2_0_0, 0), (self.blocks_delay_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.ModuladorPAM_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.ModuladorPAM_0_2, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.ModuladorPAM_0_2_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_0, 0), (self.ModuladorPAM_0_2_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_delay_0_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_0_0_0_0, 0), (self.qtgui_time_sink_x_0, 3))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "PruebaPAM")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_fs(self.samp_rate/100)
        self.ModuladorPAM_0_0.set_Samp_rate(self.samp_rate)
        self.ModuladorPAM_0_2.set_Samp_rate(self.samp_rate)
        self.ModuladorPAM_0_2_0.set_Samp_rate(self.samp_rate)
        self.ModuladorPAM_0_2_0_0.set_Samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.set_fm(self.fs/10)
        self.ModuladorPAM_0_0.set_Fs(self.fs)
        self.ModuladorPAM_0_2.set_Fs(self.fs)
        self.ModuladorPAM_0_2_0.set_Fs(self.fs)
        self.ModuladorPAM_0_2_0_0.set_Fs(self.fs)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self.analog_sig_source_x_0.set_frequency(self.fm)
        self.analog_sig_source_x_0_0.set_frequency(self.fm)
        self.analog_sig_source_x_0_0_0.set_frequency(self.fm)
        self.analog_sig_source_x_0_0_0_0.set_frequency(self.fm)

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W
        self.ModuladorPAM_0_0.set_D(self.W)
        self.ModuladorPAM_0_2.set_D(self.W)
        self.ModuladorPAM_0_2_0.set_D(self.W)
        self.ModuladorPAM_0_2_0_0.set_D(self.W)

    def get_D3(self):
        return self.D3

    def set_D3(self, D3):
        self.D3 = D3
        self.blocks_delay_0_0_0_0.set_dly(self.D3)

    def get_D2(self):
        return self.D2

    def set_D2(self, D2):
        self.D2 = D2
        self.blocks_delay_0_0_0.set_dly(self.D2)

    def get_D1(self):
        return self.D1

    def set_D1(self, D1):
        self.D1 = D1
        self.blocks_delay_0_0.set_dly(self.D1)





def main(top_block_cls=PruebaPAM, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
