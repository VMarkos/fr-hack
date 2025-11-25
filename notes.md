# Notes

Notes on everything

## Literature

Some notes from related literature:

### About Marine Heatwaves

Notes about MHWs in the Med Sea.

#### Demographics

**Marine Heatwave (MHW):** Episodes of exceptionally high ocean temperatures that persist for a long period / long periods of time (they are typically statistically rare). They are observed both on coastal areas and open seas.

Some important surface MHWs include:

1. 1999, Ligurian sea / Marseilles, 2 - 3 C increment.
2. 2003, covering 46% - 70% of the basin, 2 - 7 C local increment, duration of 48 - ~100 days (!).
3. 2007, June, Agean sea, ~3 C increment.
4. 2013, Eastern Med Sea, ~1 C increment.
5. 2015, July - August, Southeast of Spain, 2 C increment, 6 weeks, affected also ~89% of the basin.
6. 2017, Summer, NW Med Sea, 6 months,  top 6 C increment.
7. 2018, Summer, Gulf of Lion, Cyprus, Crete (affecting the entire Basin).
8. 2019, June - December, W Med Sea, 6 MHWs, 1,8 - 5,3 C increment, 5 to 20 days.
9. 2019, Summer, E Med Sea, 2 events, 21 and 159 days.
10. 2020, Summer, E Med Sea, >6 C increment.
11. 2020, Winter, Spring, Summer, W Med Sea, ~2 C increment, max 80 days.
11. 2021, Summer, Aegean sea, > 31 C max sea temperature, >20 days.
12. 2022-3, NW Med Sea, 2,6 C average and 4,3 C max daily anomalies.

In a nutshell, a (surface) MHW could be classified as an (upwards) anomaly in the surface sea temperature over the course of a few days, typically more than a week or so.

**Key reason** for surface MHWs appears to be the long term SST warming trend observed in the recent decades (1982+).

There are also subsurface MHWs, which are most intensely observed at 55m depth, most probably due to the longest heat preservation at deeper sea levels. Such MHWs are more frequent in the last decades (1982+), while, notably, some subsurface events might not have a directly observable impact on the surface level.

#### Spatial Distribution Across The Basin

1. NW Med Sea, Adriatic and Aegean, subsurface Levantine seas often suffer from higher intensity MHWs.
2. Longer MHWs occur in the Balearics, surface Levantine and across the basin at depth, away from boundary currents.
3. Areas with larger water inflow, e.g., Alboran sea, NE Aegean, Ierapetra, experience shorter MHWs.
4. The most MHWs were observed in coastal and not offshore locations, e.g., Ligurian sea, Lions Gulf.
5. For subsurface MHWs, there is a NW - SE variability, with most events occur in W Med Sea.
6. A notable characteristic is that the *surface to subsurface MHW propagation is not uniform across time and space,* e.g., 2012 - 2020 surface MHWs spread vertically eastwards, up to 50-150m in W Med Sea, 200m in Adriatic and 400-700m in E Med Sea.

#### MHW Mechanisms

1. Both air-sea heat fluxes and local oceanographic processes affect MHWs (as expected).
2. Most Med Sea MHWs are affected by:
    * Radiation fluxes;
    * Persistent low wind speed;
    * Surface heat loss supression.
3. Atmospheric Heatwaves (AHWs) also play an important role.
4. At a regional scale, oceanographic influences might prove more important, e.g., due to advection (the transfer of a substance throughout the body of a fluid).
5. Local conditions like heavy rainfalls which might cool and maybe postpone / delay MHW events (Genoa) or more saline water influx (Black Sea to NE Aegean) which might facilitate MHWs.
6. Similarly, the formation of ocean currents (long-lived eddies?) might affect regional MHWs.
7. In a similar way, AHWs also influence MHWs positively.
8. Climate modes do not appear to have a clear causal relationship with MHWs, although correlations do exist.
9. Wind mixing might also contribute to the penetration of surface MHWs to subsurface.
10. Also, downward MHW penetration appears to be more prevalent in autumn.

### About The Problem

Maybe useful for a presentation:

1. Annual Sea Surface Temperature (SST) increment rate ~0,034 - 0,041 Celsius / year vs global trend of 0,0015 C / y.
2. Largest warming trend in the Aegean and Levantine seas (0,05 C / y).
3. Similarly, on the west in the Balearic, Tyrrhenian and Adriatic seas.
4. ...

## Implementation

Notes regarding implementation

### Predicting Temperature

**Idea:** We first predict temperature based on past data and then spot any MHWs by properly annotating our predictions.
