# -*- coding: utf-8 -*-

from hydpy import Node, Element


Element("stream_dill_assl_lahn_leun", inlets="dill_assl", outlets="lahn_leun", keywords=["river"])

Element("stream_lahn_marb_lahn_leun", inlets="lahn_marb", outlets="lahn_leun", keywords=["river"])

Element("stream_dam_1_out_lahn_kalk", inlets="dam_1_out", outlets="lahn_kalk", keywords=["river"])
