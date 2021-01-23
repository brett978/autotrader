"""
optValCalc.py
calculates the value contributions of an option.

inputs:
dictionary of
    underlyingValue
    strike
    IV
    rho
    TTE
    dividend
    }

returns:
dictionary of
    delta
    gamma
    theta
    vega
    }
"""

def opValue(
