# power values are in MW of how much power the building uses
# (negative values are power production)

# this will need to be converted to 60 * MW to calculate MJ/min

class Building():
    def __init__(self, power : float):
        self.power = power

Buildings = {

    # power production buildings
    'COAL_GENERATOR': Building(-75),
    'FUEL_GENERATOR': Building(-150),
    'NUCLEAR_POWER_PLANT': Building(-2500),

    'WATER_EXTRACTOR': Building(20),
    'OIL_EXTRACTOR': Building(134.31),

    # This was calculated by averaging out the energy cost of the 6
    # pressurisers (150MW) across the 45 extractors.
    'NITROGEN_GAS_WELL_EXTRACTOR': Building(67.1549), # 6 wells, 45 extractors
    'OIL_WELL_EXTRACTOR': Building(83.9437), # 2 wells, 12 extractors
    'WATER_WELL_EXTRACTOR': Building(73.2599), # 8 wells, # 55 extractors

    'MINER_MK1': Building(16.7887), 
    'MINER_MK2': Building(40.2929),
    'MINER_MK3': Building(100.7324),

    'SMELTER': Building(4),
    'FOUNDRY': Building(16),

    'REFINERY': Building(30),
    'BLENDER': Building(75),
    'PACKAGER': Building(10),

    'CONSTRUCTOR': Building(4),
    'ASSEMBLER': Building(15),
    'MANUFACTURER': Building(55),
    'PARTICAL_ACCELERATOR_PLUTONIUM_PELLET': Building(500),
    'PARTICAL_ACCELERATOR_PLUTONIUM_CELL': Building(500),
    'PARTICAL_ACCELERATOR_NUCLEAR_PASTA': Building(1000),
    
}