# -*- coding: utf-8 -*-

from hydpy.models.dam_llake import *

simulationstep("1d")
parameterstep("1d")

surfacearea(15.0)
catchmentarea(3565.0)
correctionprecipitation(3565.0)
correctionevaporation(3565.0)
weightevaporation(1.0)
thresholdevaporation(0.0)
toleranceevaporation(0.001)
watervolume2waterlevel(
    PPoly(
        Poly(x0=0.0, cs=(0.0, 0.06666666666666667)),
    )
)
waterlevel2flooddischarge(
    PPoly(
        Poly(x0=0.0, cs=(0.0, 10.0)),
    )
)
allowedwaterleveldrop(0.5)
dischargetolerance(0.1)
