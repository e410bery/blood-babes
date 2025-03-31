import constants as c



#enzyme reactions:
def competitive_inhibition(sub, vmax, km, inhibitor, ki):
    return (vmax * sub) / (km * (1 + inhibitor / ki) + sub)

def uncompetitive_inhibition(sub, vmax, km, inhibitor, ki):
    return (vmax * sub) / (km + sub * (1 + inhibitor / ki))

def noncompetitive_inhibition(sub, vmax, km, inhibitor, ki):
    return (vmax * sub) / ((km + sub) * (1 + inhibitor / ki))

def mixed_inhibition(sub, vmax, km, inhibitor, ki, ki_prime):
    return (vmax * sub) / ((km * (1 + inhibitor / ki)) + sub * (1 + inhibitor / ki_prime))
