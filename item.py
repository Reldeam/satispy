# the item_value is the awesome sink value
# the limit is the maximum number of that item that exists in the world

class Item():
    def __init__(self, sink_value : float, limit : float = 0):
        self.sink_value = sink_value
        self.limit = limit

Items = {

    'POWER' : Item(0),

    # resource wells
    'IMPURE_CRUDE_OIL_WELL' : Item(0, 6),
    'NORMAL_CRUDE_OIL_WELL' : Item(0, 3),
    'PURE_CRUDE_OIL_WELL' : Item(0, 3),

    'IMPURE_NITROGEN_GAS_WELL' : Item(0, 2),
    'NORMAL_NITROGEN_GAS_WELL' : Item(0, 7),
    'PURE_NITROGEN_GAS_WELL' : Item(0, 36),
    
    'IMPURE_WATER_WELL' : Item(0, 7),
    'NORMAL_WATER_WELL' : Item(0, 12),
    'PURE_WATER_WELL' : Item(0, 36),

    # resource nodes
    'IMPURE_IRON_NODE' : Item(0, 33),
    'NORMAL_IRON_NODE' : Item(0, 41),
    'PURE_IRON_NODE' : Item(0, 46),

    'IMPURE_COPPER_NODE' : Item(0, 9),
    'NORMAL_COPPER_NODE' : Item(0, 28),
    'PURE_COPPER_NODE' : Item(0, 12),

    'IMPURE_LIMESTONE_NODE' : Item(0, 12),
    'NORMAL_LIMESTONE_NODE' : Item(0, 47),
    'PURE_LIMESTONE_NODE' : Item(0, 27),

    'IMPURE_COAL_NODE' : Item(0, 6),
    'NORMAL_COAL_NODE' : Item(0, 29),
    'PURE_COAL_NODE' : Item(0, 15),

    'IMPURE_CATERIUM_NODE' : Item(0, 0),
    'NORMAL_CATERIUM_NODE' : Item(0, 8),
    'PURE_CATERIUM_NODE' : Item(0, 8),

    'IMPURE_QUARTZ_NODE' : Item(0, 0),
    'NORMAL_QUARTZ_NODE' : Item(0, 11),
    'PURE_QUARTZ_NODE' : Item(0, 5),

    'IMPURE_SULFUR_NODE' : Item(0, 1),
    'NORMAL_SULFUR_NODE' : Item(0, 7),
    'PURE_SULFUR_NODE' : Item(0, 3),

    'IMPURE_URANIUM_NODE' : Item(0, 1),
    'NORMAL_URANIUM_NODE' : Item(0, 3),
    'PURE_URANIUM_NODE' : Item(0, 0),

    'IMPURE_BAUXITE_NODE' : Item(0, 5),
    'NORMAL_BAUXITE_NODE' : Item(0, 6),
    'PURE_BAUXITE_NODE' : Item(0, 6),

    'IMPURE_SAM_NODE' : Item(0, 8),
    'NORMAL_SAM_NODE' : Item(0, 5),
    'PURE_SAM_NODE' : Item(0, 0),

    'IMPURE_CRUDE_OIL_NODE' : Item(0, 10),
    'NORMAL_CRUDE_OIL_NODE' : Item(0, 12),
    'PURE_CRUDE_OIL_NODE' : Item(0, 8),

    # ores
    'LIMESTONE' : Item(2),
    'IRON_ORE' : Item(1),
    'COPPER_ORE' : Item(3),
    'COAL' : Item(3),
    'CATERIUM_ORE' : Item(7),
    'RAW_QUARTZ' : Item(15),
    'SULFUR' : Item(11),
    'URANIUM' : Item(35),
    'BAUXITE' : Item(8),
    'SAM_ORE' : Item(0),

    # ingots
    'IRON_INGOT' : Item(2),
    'COPPER_INGOT' : Item(6),
    'CATERIUM_INGOT' : Item(42),
    'STEEL_INGOT' : Item(8),
    'ALUMINUM_INGOT' : Item(131),
    
    # minerals
    'CONCRETE' : Item(12),
    'QUARTZ_CRYSTAL' : Item(50),
    'SILICA' : Item(20),
    'COPPER_POWDER': Item(72),
    'POLYMER_RESIN' : Item(12),
    'PETROLEUM_COKE' : Item(20),
    'ALUMINUM_SCRAP': Item(27),
    
     # fluids
    'WATER' : Item(0),
    'CRUDE_OIL': Item(0),
    'HEAVY_OIL_RESIDUE': Item(0),
    'FUEL': Item(0),
    'TURBOFUEL': Item(0),
    'ALUMINA_SOLUTION' : Item(0),
    'SULFURIC_ACID': Item(0),
    'NITRIC_ACID': Item(0),
    'NITROGEN_GAS': Item(0),

    # standard parts
    'IRON_ROD' : Item(4),
    'SCREW' : Item(2),
    'IRON_PLATE' : Item(6),
    'REINFORCED_IRON_PLATE' : Item(120),
    'COPPER_SHEET': Item(24),
    'ALCLAD_ALUMINUM_SHEET' : Item(266),
    'ALUMINUM_CASING': Item(393),
    'STEEL_PIPE': Item(24),
    'STEEL_BEAM': Item(64),
    'ENCASED_INDUSTRIAL_BEAM': Item(632),
    'MODULAR_FRAME': Item(408),
    'HEAVY_MODULAR_FRAME': Item(11520),
    'FUSED_MODULAR_FRAME': Item(62840),
    'FABRIC': Item(140),
    'PLASTIC' : Item(75),
    'RUBBER' : Item(60),

    # industrial parts
    'ROTOR' : Item(140),
    'STATOR' : Item(240),
    'BATTERY': Item(465),
    'MOTOR' : Item(1520),
    'HEAT_SINK': Item(2804),
    'COOLING_SYSTEM': Item(12006),
    'TURBO_MOTOR': Item(242720),
    
    # electronics
    'WIRE' : Item(6),
    'CABLE': Item(24),
    'QUICKWIRE': Item(17),
    'CIRCUIT_BOARD': Item(696),
    'AI_LIMITER': Item(920),
    'HIGH_SPEED_CONNECTOR': Item(3776),

    # communications
    'COMPUTER' : Item(17260),
    'SUPERCOMPUTER': Item(99576),
    'QUANTUM_COMPUTER': Item(200),
    'RADIO_CONTROL_UNIT': Item(19600),
    'CRYSTAL_OSCILLATOR': Item(3072), 

    # containers
    'EMPTY_CANISTER': Item(60),
    'EMPTY_FLUID_TANK': Item(225),
    'PRESSURE_CONVERSION_CUBE': Item(257312),
    'PACKAGED_WATER': Item(130),
    'PACKAGED_ALUMINA_SOLUTION': Item(160),
    'PACKAGED_SULFURIC_ACID': Item(152),
    'PACKAGED_NITRIC_ACID': Item(412),
    'PACKAGED_NITROGEN_GAS': Item(312),
    
    # fuels
    'LEAVES' : Item(3),
    'MYCELIA' : Item(10),
    'FLOWER_PETALS' : Item(10),
    'WOOD': Item(30),
    'BIOMASS':  Item(12),
    'SOLID_BIOFUEL': Item(48),
    'COMPACTED_COAL' : Item(28),
    'PACKAGED_OIL' : Item(180),
    'PACKAGED_HEAVY_OIL_RESIDUE' : Item(180),
    'PACKAGED_FUEL' : Item(270),
    'PACKAGED_TURBOFUEL' : Item(570),
    
    # consumables
    'BLACK_POWDER': Item(14),
    'SMOKELESS_POWDER': Item(58),
    'GAS_FILTER': Item(830),
    'COLOR_CARTRIDGE': Item(10),
    'BEACON': Item(320),
    'IODINE_INFUSED_FILTER': Item(2718),

    # nuclear
    'ELECTROMAGNETIC_CONTROL_ROD': Item(2560),
    'ENCASED_URANIUM_CELL': Item(147),
    'NON_FISSILE_URANIUM': Item(0),
    'PLUTONIUM_PELLET': Item(0),
    'ENCASED_PLUTONIUM_CELL': Item(0),
    
    'URANIUM_FUEL_ROD': Item(44092),
    'PLUTONIUM_FUEL_ROD': Item(153184),
    
    'URANIUM_WASTE': Item(0),
    'PLUTONIUM_WASTE': Item(0),

    # space elevator
    'SMART_PLATING': Item(520),
    'VERSATILE_FRAMEWORK': Item(1176),
    'AUTOMATED_WIRING': Item(1440),
    'MODULAR_ENGINE': Item(9960),
    'ADAPTIVE_CONTROL_UNIT': Item(86120),
    'ASSEMBLY_DIRECTOR_SYSTEM': Item(543632),
    'MAGNETIC_FIELD_GENERATOR': Item(15650),
    'THERMAL_PROPULSION_ROCKET': Item(732956),
    'NUCLEAR_PASTA': Item(543424),
    
}