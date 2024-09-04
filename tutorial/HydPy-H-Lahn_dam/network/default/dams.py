# -*- coding: utf-8 -*-

from hydpy import Node, Element

Node("dam_1_out", variable="Q", keywords=["dam_out"])

Element("dam_1", inlets="lahn_leun", outlets="dam_1_out", keywords=["dam"])
