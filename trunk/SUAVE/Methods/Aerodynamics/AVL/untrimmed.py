## @ingroup Methods-Aerodynamics-AVL
#untrimmed.py
#
# Created:  Jan 2014, T. Orra (base file in low fidelity)
# Modified: May 2017, T. MacDonald  

## @ingroup Methods-Aerodynamics-AVL
def untrimmed(state,settings,geometry):
    """ Computes untrimmed drag of the aircraft

    Assumptions:
        None
        
    Source:
        None

    Inputs:
        state
        settings
        geometry

    Outputs:
        aircraft_untrimmed

    Properties Used:
        N/A
    """    
    
    # Unpack inputs
    conditions     = state.conditions
    configuration  = settings
    drag_breakdown = conditions.aerodynamics.drag_breakdown

    # Various drag components
    compressibility_total = conditions.aerodynamics.drag_breakdown.compressible.total    
    induced_total         = conditions.aerodynamics.drag_breakdown.induced.total  
    invisid_total         = compressibility_total + induced_total
    parasite_total        = conditions.aerodynamics.drag_breakdown.parasite.total              
    miscellaneous_drag    = conditions.aerodynamics.drag_breakdown.miscellaneous.total 

    # Untrimmed drag
    aircraft_untrimmed = invisid_total        \
        + parasite_total \
        + miscellaneous_drag
    
    conditions.aerodynamics.drag_breakdown.untrimmed = aircraft_untrimmed
    
    return aircraft_untrimmed