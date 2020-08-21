import numpy as np


def ModelA_lightcurve(times, params):
    """
    Model A for the light curve
    
    f(t) = 'amplitude' * exp( -x**2 )
    where x = t / 'duration'
    
    INPUTS
    ------
    times: numpy array shape=(Ntimes,)
        the time stamps for the observations [seconds]
        
    params: dict of model parameters
        keys 'amplitude' and 'duration'
        
    RETURNS
    -------
    light_curve: numpy array shape=(Ntimes,)
    """
    x = times / params['duration']
    light_curve = params['amplitude']*np.exp( -x**2 )
    return light_curve

def ModelB_lightcurve(times, params):
    """
    Model B for the light curve
    
    f(t) = 'amplitude' / ( 1 + x**2 ) 
    where x = t / 'duration'
    
    INPUTS
    ------
    times: numpy array shape=(Ntimes,)
        the time stamps for the observations [seconds]
        
    params: dict of model parameters
        keys 'amplitude' and 'duration'
        
    RETURNS
    -------
    light_curve: numpy array shape=(Ntimes,)
    """
    x = times / params['duration']
    light_curve = params['amplitude'] / ( 1 + x**2 )
    return light_curve
