#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Dec 30 12:32:39 2020
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import histosink_gl
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 128000
        self.noise = noise = 0.05
        self.lo = lo = 0.250
        self.hi = hi = 0.750
        self.const = const = 0

        ##################################################
        # Blocks
        ##################################################
        _noise_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noise_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_noise_sizer,
        	value=self.noise,
        	callback=self.set_noise,
        	label='noise',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noise_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_noise_sizer,
        	value=self.noise,
        	callback=self.set_noise,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_noise_sizer)
        _lo_sizer = wx.BoxSizer(wx.VERTICAL)
        self._lo_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_lo_sizer,
        	value=self.lo,
        	callback=self.set_lo,
        	label='lo',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._lo_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_lo_sizer,
        	value=self.lo,
        	callback=self.set_lo,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_lo_sizer)
        _hi_sizer = wx.BoxSizer(wx.VERTICAL)
        self._hi_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_hi_sizer,
        	value=self.hi,
        	callback=self.set_hi,
        	label='hi',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._hi_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_hi_sizer,
        	value=self.hi,
        	callback=self.set_hi,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_hi_sizer)
        _const_sizer = wx.BoxSizer(wx.VERTICAL)
        self._const_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_const_sizer,
        	value=self.const,
        	callback=self.set_const,
        	label='const',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._const_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_const_sizer,
        	value=self.const,
        	callback=self.set_const,
        	minimum=-1,
        	maximum=2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_const_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0.250,
        	v_offset=0.500,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=5,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        	size=(510,320),
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_histosink2_0 = histosink_gl.histo_sink_f(
        	self.GetWin(),
        	title='Histogram Plot',
        	num_bins=241,
        	frame_size=10000,
        )
        self.Add(self.wxgui_histosink2_0.win)
        self.blocks_throttle_0_2 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(0.250, 0.750, 0)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise, 0)
        self.analog_const_source_x_1_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, hi)
        self.analog_const_source_x_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, lo)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, const)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_const_source_x_1, 0), (self.blocks_throttle_0_1, 0))
        self.connect((self.analog_const_source_x_1_0, 0), (self.blocks_throttle_0_2, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_scopesink2_0, 2))
        self.connect((self.blocks_threshold_ff_0, 0), (self.wxgui_scopesink2_0, 3))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_scopesink2_0, 4))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_0_0, 0), (self.wxgui_histosink2_0, 0))
        self.connect((self.blocks_throttle_0_1, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_throttle_0_2, 0), (self.wxgui_scopesink2_0, 1))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_2.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self._noise_slider.set_value(self.noise)
        self._noise_text_box.set_value(self.noise)
        self.analog_noise_source_x_0.set_amplitude(self.noise)

    def get_lo(self):
        return self.lo

    def set_lo(self, lo):
        self.lo = lo
        self._lo_slider.set_value(self.lo)
        self._lo_text_box.set_value(self.lo)
        self.analog_const_source_x_1.set_offset(self.lo)

    def get_hi(self):
        return self.hi

    def set_hi(self, hi):
        self.hi = hi
        self._hi_slider.set_value(self.hi)
        self._hi_text_box.set_value(self.hi)
        self.analog_const_source_x_1_0.set_offset(self.hi)

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const
        self._const_slider.set_value(self.const)
        self._const_text_box.set_value(self.const)
        self.analog_const_source_x_0.set_offset(self.const)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
