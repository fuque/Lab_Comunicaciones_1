# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ModuladorPAM
# Author: L1A_G6
# GNU Radio version: 3.10.1.1

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal







class Modulador_PAM(gr.hier_block2, Qt.QWidget):
    def __init__(self, D=10, Fs=100000, Samp_rate=100e3):
        gr.hier_block2.__init__(
            self, "ModuladorPAM",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        Qt.QWidget.__init__(self)
        self.top_layout = Qt.QVBoxLayout()
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)
        self.setLayout(self.top_layout)

        ##################################################
        # Parameters
        ##################################################
        self.D = D
        self.Fs = Fs
        self.Samp_rate = Samp_rate

        ##################################################
        # Blocks
        ##################################################
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 20-D)
        self.analog_sig_source_x_0 = analog.sig_source_f(Samp_rate, analog.GR_SQR_WAVE, Fs, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self, 0), (self.blocks_multiply_xx_0, 0))


    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self.blocks_delay_0.set_dly(20-self.D)

    def get_Fs(self):
        return self.Fs

    def set_Fs(self, Fs):
        self.Fs = Fs
        self.analog_sig_source_x_0.set_frequency(self.Fs)

    def get_Samp_rate(self):
        return self.Samp_rate

    def set_Samp_rate(self, Samp_rate):
        self.Samp_rate = Samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.Samp_rate)

