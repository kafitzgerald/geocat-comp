import numpy as np


def calc_kbdi(max_daily_temp, daily_precip):
    """ Calculates the Keetch-Byram Drought Index. Based on calculations made
        in "A Drought Index for Fire Control" by John Keetch and George Byram
        in 1968.

            Args:
                max_daily_temp (:class:`numpy.ndarray` or :obj:`list`):
                    Temperature in Fahrenheight

                daily_precip (:class:`numpy.ndarray` or :obj:`list`):
                    Daily precipitation in inches.

            Returns:

                kdbi (:class:`numpy.ndarray` or :obj:`list`):
                    Keetch-Byram Drought Index. It is on a scale between 0
                    and 800, where 0 indicates saturated soil and 800 indicates
                    severe drought.
    """
