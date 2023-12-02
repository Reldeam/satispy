from ingredient import Ingredient

class Recipe():
    def __init__(self, building : str, ingredients : [str], result : [str]):
        self.building = building
        self.ingredients = ingredients
        self.result = result

# All ingredients are in the form of items per minute.
# Ore recipies are assumed to use a Mk.3 miner at 250%.
# Pure ore nodes are capped at 780 ore per minute.

Recipes = {

    # power recipes
    'COAL_POWER': Recipe('COAL_GENERATOR', [Ingredient('COAL', 15), Ingredient('WATER', 45)], []),
    'FUEL_POWER': Recipe('FUEL_GENERATOR', [Ingredient('FUEL', 12)], []),
    'TURBOFUEL_POWER': Recipe('FUEL_GENERATOR', [Ingredient('TURBOFUEL', 4.5)], []),
    'URANIUM_POWER': Recipe('NUCLEAR_POWER_PLANT', [Ingredient('URANIUM_FUEL_ROD', 0.2)], [Ingredient('URANIUM_WASTE', 10)]),
    'PLUTONIUM_POWER': Recipe('NUCLEAR_POWER_PLANT', [Ingredient('PLUTONIUM_FUEL_ROD', 0.1)], [Ingredient('PLUTONIUM_WASTE', 1)]),

    # fluids - well extraction
    
    'IMPURE_NITROGEN_GAS': Recipe('NITROGEN_GAS_WELL_EXTRACTOR', [Ingredient('IMPURE_NITROGEN_GAS_WELL', 1)], [Ingredient('NITROGEN_GAS', 75)]),
    'NORMAL_NITROGEN_GAS': Recipe('NITROGEN_GAS_WELL_EXTRACTOR', [Ingredient('NORMAL_NITROGEN_GAS_WELL', 1)], [Ingredient('NITROGEN_GAS', 150)]),
    'PURE_NITROGEN_GAS': Recipe('NITROGEN_GAS_WELL_EXTRACTOR', [Ingredient('PURE_NITROGEN_GAS_WELL', 1)], [Ingredient('NITROGEN_GAS', 300)]),
    
    'IMPURE_CRUDE_OIL_WELL': Recipe('OIL_WELL_EXTRACTOR', [Ingredient('IMPURE_CRUDE_OIL_WELL', 1)], [Ingredient('CRUDE_OIL', 75)]),
    'NORMAL_CRUDE_OIL_WELL': Recipe('OIL_WELL_EXTRACTOR', [Ingredient('NORMAL_CRUDE_OIL_WELL', 1)], [Ingredient('CRUDE_OIL', 150)]),
    'PURE_CRUDE_OIL_WELL': Recipe('OIL_WELL_EXTRACTOR', [Ingredient('PURE_CRUDE_OIL_WELL', 1)], [Ingredient('CRUDE_OIL', 300)]),
    
    'IMPURE_WATER_WELL': Recipe('WATER_WELL_EXTRACTOR', [Ingredient('IMPURE_WATER_WELL', 1)], [Ingredient('WATER', 75)]),
    'NORMAL_WATER_WELL': Recipe('WATER_WELL_EXTRACTOR', [Ingredient('NORMAL_WATER_WELL', 1)], [Ingredient('WATER', 150)]),
    'PURE_WATER_WELL': Recipe('WATER_WELL_EXTRACTOR', [Ingredient('PURE_WATER_WELL', 1)], [Ingredient('WATER', 300)]),
    
    # fluids - node extraction
    
    'WATER_EXTRACTOR': Recipe('WATER_EXTRACTOR', [], [Ingredient('WATER', 120)]),
    
    'IMPURE_CRUDE_OIL': Recipe('OIL_EXTRACTOR', [Ingredient('IMPURE_CRUDE_OIL_NODE', 1)], [Ingredient('CRUDE_OIL', 150)]),
    'NORMAL_CRUDE_OIL': Recipe('OIL_EXTRACTOR', [Ingredient('NORMAL_CRUDE_OIL_NODE', 1)], [Ingredient('CRUDE_OIL', 300)]),
    'PURE_CRUDE_OIL': Recipe('OIL_EXTRACTOR', [Ingredient('PURE_CRUDE_OIL_NODE', 1)], [Ingredient('CRUDE_OIL', 600)]),

    # ores
    'IMPURE_IRON_ORE': Recipe('MINER_MK3', [Ingredient('IMPURE_IRON_NODE', 1)], [Ingredient('IRON_ORE', 300)]),
    'NORMAL_IRON_ORE': Recipe('MINER_MK3', [Ingredient('NORMAL_IRON_NODE', 1)], [Ingredient('IRON_ORE', 600)]),
    'PURE_IRON_ORE': Recipe('MINER_MK3', [Ingredient('PURE_IRON_NODE', 1)], [Ingredient('IRON_ORE', 780)]),

    'IMPURE_COPPER_ORE': Recipe('MINER_MK3', [Ingredient('IMPURE_COPPER_NODE', 1)], [Ingredient('COPPER_ORE', 300)]),
    'NORMAL_COPPER_ORE': Recipe('MINER_MK3', [Ingredient('NORMAL_COPPER_NODE', 1)], [Ingredient('COPPER_ORE', 600)]),
    'PURE_COPPER_ORE': Recipe('MINER_MK3', [Ingredient('PURE_COPPER_NODE', 1)], [Ingredient('COPPER_ORE', 780)]),

    'IMPURE_LIMESTONE': Recipe('MINER_MK3', [Ingredient('IMPURE_LIMESTONE_NODE', 1)], [Ingredient('LIMESTONE', 300)]),
    'NORMAL_LIMESTONE': Recipe('MINER_MK3', [Ingredient('NORMAL_LIMESTONE_NODE', 1)], [Ingredient('LIMESTONE', 600)]),
    'PURE_LIMESTONE': Recipe('MINER_MK3', [Ingredient('PURE_LIMESTONE_NODE', 1)], [Ingredient('LIMESTONE', 780)]),

    'IMPURE_COAL': Recipe('MINER_MK3', [Ingredient('IMPURE_COAL_NODE', 1)], [Ingredient('COAL', 300)]),
    'NORMAL_COAL': Recipe('MINER_MK3', [Ingredient('NORMAL_COAL_NODE', 1)], [Ingredient('COAL', 600)]),
    'PURE_COAL': Recipe('MINER_MK3', [Ingredient('PURE_COAL_NODE', 1)], [Ingredient('COAL', 780)]),

    'IMPURE_CATERIUM_ORE': Recipe('MINER_MK3', [Ingredient('IMPURE_CATERIUM_NODE', 1)], [Ingredient('CATERIUM_ORE', 300)]),
    'NORMAL_CATERIUM_ORE': Recipe('MINER_MK3', [Ingredient('NORMAL_CATERIUM_NODE', 1)], [Ingredient('CATERIUM_ORE', 600)]),
    'PURE_CATERIUM_ORE': Recipe('MINER_MK3', [Ingredient('PURE_CATERIUM_NODE', 1)], [Ingredient('CATERIUM_ORE', 780)]),

    'IMPURE_RAW_QUARTZ': Recipe('MINER_MK3', [Ingredient('IMPURE_QUARTZ_NODE', 1)], [Ingredient('RAW_QUARTZ', 300)]),
    'NORMAL_RAW_QUARTZ': Recipe('MINER_MK3', [Ingredient('NORMAL_QUARTZ_NODE', 1)], [Ingredient('RAW_QUARTZ', 600)]),
    'PURE_RAW_QUARTZ': Recipe('MINER_MK3', [Ingredient('PURE_QUARTZ_NODE', 1)], [Ingredient('RAW_QUARTZ', 780)]),

    'IMPURE_SULFUR': Recipe('MINER_MK3', [Ingredient('IMPURE_SULFUR_NODE', 1)], [Ingredient('SULFUR', 300)]),
    'NORMAL_SULFUR': Recipe('MINER_MK3', [Ingredient('NORMAL_SULFUR_NODE', 1)], [Ingredient('SULFUR', 600)]),
    'PURE_SULFUR': Recipe('MINER_MK3', [Ingredient('PURE_SULFUR_NODE', 1)], [Ingredient('SULFUR', 780)]),

    'IMPURE_URANIUM': Recipe('MINER_MK3', [Ingredient('IMPURE_URANIUM_NODE', 1)], [Ingredient('URANIUM', 300)]),
    'NORMAL_URANIUM': Recipe('MINER_MK3', [Ingredient('NORMAL_URANIUM_NODE', 1)], [Ingredient('URANIUM', 600)]),
    'PURE_URANIUM': Recipe('MINER_MK3', [Ingredient('PURE_URANIUM_NODE', 1)], [Ingredient('URANIUM', 780)]),

    'IMPURE_BAUXITE': Recipe('MINER_MK3', [Ingredient('IMPURE_BAUXITE_NODE', 1)], [Ingredient('BAUXITE', 300)]),
    'NORMAL_BAUXITE': Recipe('MINER_MK3', [Ingredient('NORMAL_BAUXITE_NODE', 1)], [Ingredient('BAUXITE', 600)]),
    'PURE_BAUXITE': Recipe('MINER_MK3', [Ingredient('PURE_BAUXITE_NODE', 1)], [Ingredient('BAUXITE', 780)]),

    'IMPURE_SAM_ORE': Recipe('MINER_MK3', [Ingredient('IMPURE_SAM_NODE', 1)], [Ingredient('SAM_ORE', 300)]),
    'NORMAL_SAM_ORE': Recipe('MINER_MK3', [Ingredient('NORMAL_SAM_NODE', 1)], [Ingredient('SAM_ORE', 600)]),
    'PURE_SAM_ORE': Recipe('MINER_MK3', [Ingredient('PURE_SAM_NODE', 1)], [Ingredient('SAM_ORE', 780)]),

    # ingots
    'IRON_INGOT': Recipe('SMELTER', [Ingredient('IRON_ORE', 30)], [Ingredient('IRON_INGOT', 30)]),
    'IRON_ALLOY_INGOT': Recipe('FOUNDRY', [Ingredient('IRON_ORE', 20), Ingredient('COPPER_ORE', 20)], [Ingredient('IRON_INGOT', 50)]),
    'PURE_IRON_INGOT': Recipe('REFINERY', [Ingredient('IRON_ORE', 35), Ingredient('WATER', 20)], [Ingredient('IRON_INGOT', 65)]),

    'COPPER_INGOT': Recipe('SMELTER', [Ingredient('COPPER_ORE', 30)], [Ingredient('COPPER_INGOT', 30)]),
    'COPPER_ALLOY_INGOT': Recipe('FOUNDRY', [Ingredient('COPPER_ORE', 50), Ingredient('IRON_ORE', 25)], [Ingredient('COPPER_INGOT', 100)]),
    'PURE_COPPER_INGOT': Recipe('REFINERY', [Ingredient('COPPER_ORE', 15), Ingredient('WATER', 10)], [Ingredient('COPPER_INGOT', 37.5)]),

    'CATERIUM_INGOT': Recipe('SMELTER', [Ingredient('CATERIUM_ORE', 45)], [Ingredient('CATERIUM_INGOT', 15)]),
    'PURE_CATERIUM_INGOT': Recipe('REFINERY', [Ingredient('CATERIUM_ORE', 24), Ingredient('WATER', 24)], [Ingredient('CATERIUM_INGOT', 12)]),

    'STEEL_INGOT': Recipe('FOUNDRY', [Ingredient('IRON_ORE', 45), Ingredient('COAL', 45)], [Ingredient('STEEL_INGOT', 45)]),
    'COKE_STEEL_INGOT': Recipe('FOUNDRY', [Ingredient('IRON_ORE', 75), Ingredient('PETROLEUM_COKE', 75)], [Ingredient('STEEL_INGOT', 100)]),
    'COMPACTED_STEEL_INGOT': Recipe('FOUNDRY', [Ingredient('IRON_ORE', 22.5), Ingredient('COMPACTED_COAL', 11.25)], [Ingredient('STEEL_INGOT', 37.5)]),
    'SOLID_STEEL_INGOT': Recipe('FOUNDRY', [Ingredient('IRON_INGOT', 40), Ingredient('COAL', 40)], [Ingredient('STEEL_INGOT', 60)]),

    'ALUMINUM_INGOT': Recipe('FOUNDRY', [Ingredient('ALUMINUM_SCRAP', 90), Ingredient('SILICA', 75)], [Ingredient('ALUMINUM_INGOT', 60)]),
    'PURE_ALUMINUM_INGOT': Recipe('SMELTER', [Ingredient('ALUMINUM_SCRAP', 60)], [Ingredient('ALUMINUM_INGOT', 30)]),
    
    # minerals
    
    'CONCRETE': Recipe('CONSTRUCTOR', [Ingredient('LIMESTONE', 45)], [Ingredient('CONCRETE', 15)]),
    'FINE_CONCRETE': Recipe('ASSEMBLER', [Ingredient('LIMESTONE', 30), Ingredient('SILICA', 7.5)], [Ingredient('CONCRETE', 25)]),
    'RUBBER_CONCRETE': Recipe('ASSEMBLER', [Ingredient('LIMESTONE', 50), Ingredient('RUBBER', 10)], [Ingredient('CONCRETE', 45)]),
    'WET_CONCRETE': Recipe('REFINERY', [Ingredient('LIMESTONE', 120), Ingredient('WATER', 100)], [Ingredient('CONCRETE', 80)]),
    
    'QUARTZ_CRYSTAL': Recipe('CONSTRUCTOR', [Ingredient('RAW_QUARTZ', 37.5)], [Ingredient('QUARTZ_CRYSTAL', 22.5)]),
    'PURE_QUARTZ_CRYSTAL': Recipe('REFINERY', [Ingredient('RAW_QUARTZ', 67.5), Ingredient('WATER', 37.5)], [Ingredient('QUARTZ_CRYSTAL', 52.5)]),

    'SILICA': Recipe('CONSTRUCTOR', [Ingredient('RAW_QUARTZ', 22.5)], [Ingredient('SILICA', 37.5)]),
    'CHEAP_SILICA': Recipe('ASSEMBLER', [Ingredient('RAW_QUARTZ', 11.25), Ingredient('LIMESTONE', 18.75)], [Ingredient('SILICA', 26.25)]),
    
    'COPPER_POWDER': Recipe('CONSTRUCTOR', [Ingredient('COPPER_INGOT', 300)], [Ingredient('COPPER_POWDER', 50)]),
    
    'POLYMER_RESIN': Recipe('REFINERY', [Ingredient('CRUDE_OIL', 60)], [Ingredient('POLYMER_RESIN', 130), Ingredient('HEAVY_OIL_RESIDUE', 20)]),
    
    'PETROLEUM_COKE': Recipe('REFINERY', [Ingredient('HEAVY_OIL_RESIDUE', 40)], [Ingredient('PETROLEUM_COKE', 120)]),
    
    'ALUMINUM_SCRAP': Recipe('REFINERY', [Ingredient('ALUMINA_SOLUTION', 240), Ingredient('COAL', 120)], [Ingredient('ALUMINUM_SCRAP', 360), Ingredient('WATER', 120)]),
    'ELECTRODE_ALUMINUM_SCRAP': Recipe('REFINERY', [Ingredient('ALUMINA_SOLUTION', 180), Ingredient('PETROLEUM_COKE', 60)], [Ingredient('ALUMINUM_SCRAP', 300), Ingredient('WATER', 105)]),
    'INSTANT_SCRAP': Recipe('BLENDER', [Ingredient('BAUXITE', 150), Ingredient('COAL', 100), Ingredient('SULFURIC_ACID', 50), Ingredient('WATER', 60)], [Ingredient('ALUMINUM_SCRAP', 300), Ingredient('WATER', 50)]),

    # fluids
    
    'UNPACKAGE_WATER': Recipe('PACKAGER', [Ingredient('PACKAGED_WATER', 120)], [Ingredient('WATER', 120), Ingredient('EMPTY_CANISTER', 120)]),
    
    'UNPACKAGE_OIL': Recipe('PACKAGER', [Ingredient('PACKAGED_OIL', 60)], [Ingredient('CRUDE_OIL', 60), Ingredient('EMPTY_CANISTER', 60)]),
    
    'HEAVY_OIL_RESIDUE': Recipe('REFINERY', [Ingredient('CRUDE_OIL', 30)], [Ingredient('HEAVY_OIL_RESIDUE', 40), Ingredient('POLYMER_RESIN', 20)]),
    'UNPACKAGE_HEAVY_OIL_RESIDUE': Recipe('PACKAGER', [Ingredient('PACKAGED_HEAVY_OIL_RESIDUE', 20)], [Ingredient('HEAVY_OIL_RESIDUE', 20), Ingredient('EMPTY_CANISTER', 20)]),
    
    'FUEL': Recipe('REFINERY', [Ingredient('CRUDE_OIL', 60)], [Ingredient('FUEL', 40), Ingredient('POLYMER_RESIN', 30)]),
    'RESIDUAL_FUEL': Recipe('REFINERY', [Ingredient('HEAVY_OIL_RESIDUE', 60)], [Ingredient('FUEL', 40)]),
    'UNPACKAGE_FUEL': Recipe('PACKAGER', [Ingredient('PACKAGED_FUEL', 60)], [Ingredient('FUEL', 60), Ingredient('EMPTY_CANISTER', 60)]),
    'DILUTED_FUEL': Recipe('BLENDER', [Ingredient('HEAVY_OIL_RESIDUE', 50), Ingredient('WATER', 100)], [Ingredient('FUEL', 100)]),
    
    'TURBOFUEL': Recipe('REFINERY', [Ingredient('FUEL', 22.5), Ingredient('COMPACTED_COAL', 15)], [Ingredient('TURBOFUEL', 18.75)]),
    'UNPACKAGE_TURBOFUEL': Recipe('PACKAGER', [Ingredient('PACKAGED_TURBOFUEL', 20)], [Ingredient('TURBOFUEL', 20), Ingredient('EMPTY_CANISTER', 20)]),
    'TURBO_BLEND_FUEL': Recipe('BLENDER', [Ingredient('FUEL', 15), Ingredient('HEAVY_OIL_RESIDUE', 30), Ingredient('SULFUR', 22.5), Ingredient('PETROLEUM_COKE', 22.5)], [Ingredient('TURBOFUEL', 45)]),
    'TURBO_HEAVY_FUEL': Recipe('REFINERY', [Ingredient('HEAVY_OIL_RESIDUE', 37.5), Ingredient('COMPACTED_COAL', 30)], [Ingredient('TURBOFUEL', 30)]),
    
    'ALUMINA_SOLUTION': Recipe('REFINERY', [Ingredient('BAUXITE', 120), Ingredient('WATER', 180)], [Ingredient('ALUMINA_SOLUTION', 120), Ingredient('SILICA', 50)]),
    'SLOPPY_ALUMINA': Recipe('REFINERY', [Ingredient('BAUXITE', 200), Ingredient('WATER', 200)], [Ingredient('ALUMINA_SOLUTION', 240)]),
    'UNPACKAGED_ALUMINA_SOLUTION': Recipe('PACKAGER', [Ingredient('PACKAGED_ALUMINA_SOLUTION', 120)], [Ingredient('ALUMINA_SOLUTION', 120), Ingredient('EMPTY_CANISTER', 120)]),
    
    'SULFURIC_ACID': Recipe('REFINERY', [Ingredient('SULFUR', 50), Ingredient('WATER', 50)], [Ingredient('SULFURIC_ACID', 50)]),
    'UNPACKAGE_SULFURIC_ACID': Recipe('PACKAGER', [Ingredient('PACKAGED_SULFURIC_ACID', 60)], [Ingredient('SULFURIC_ACID', 60), Ingredient('EMPTY_CANISTER', 60)]),
    
    'NITRIC_ACID': Recipe('BLENDER', [Ingredient('NITROGEN_GAS', 120), Ingredient('WATER', 30), Ingredient('IRON_PLATE', 10)], [Ingredient('NITRIC_ACID', 30)]),
    'UNPACKAGE_NITRIC_ACID': Recipe('PACKAGER', [Ingredient('PACKAGED_NITRIC_ACID', 20)], [Ingredient('NITRIC_ACID', 20), Ingredient('EMPTY_FLUID_TANK', 20)]),
    
    'UNPACKAGE_NITROGEN_GAS': Recipe('PACKAGER', [Ingredient('PACKAGED_NITROGEN_GAS', 60)], [Ingredient('NITROGEN_GAS', 240), Ingredient('EMPTY_FLUID_TANK', 60)]),

    # standard parts

    'IRON_ROD': Recipe('CONSTRUCTOR', [Ingredient('IRON_INGOT', 15)], [Ingredient('IRON_ROD', 15)]),
    'STEEL_ROD': Recipe('CONSTRUCTOR', [Ingredient('STEEL_INGOT', 12)], [Ingredient('IRON_ROD', 48)]),

    'SCREW': Recipe('CONSTRUCTOR', [Ingredient('IRON_ROD', 10)], [Ingredient('SCREW', 40)]),
    'CAST_SCREW': Recipe('CONSTRUCTOR', [Ingredient('IRON_INGOT', 12.5)], [Ingredient('SCREW', 50)]),
    'STEEL_SCREW': Recipe('CONSTRUCTOR', [Ingredient('STEEL_BEAM', 5)], [Ingredient('SCREW', 260)]),

    'IRON_PLATE': Recipe('CONSTRUCTOR', [Ingredient('IRON_INGOT', 30)], [Ingredient('IRON_PLATE', 20)]),
    'COATED_IRON_PLATE': Recipe('ASSEMBLER', [Ingredient('IRON_INGOT', 50), Ingredient('PLASTIC', 10)], [Ingredient('IRON_PLATE', 75)]),
    'STEEL_COATED_PLATE': Recipe('ASSEMBLER', [Ingredient('STEEL_INGOT', 7.5), Ingredient('PLASTIC', 5)], [Ingredient('IRON_PLATE', 45)]),

    'REINFORCED_IRON_PLATE': Recipe('ASSEMBLER', [Ingredient('IRON_PLATE', 30), Ingredient('SCREW', 60)], [Ingredient('REINFORCED_IRON_PLATE', 5)]),
    'ADHERED_IRON_PLATE': Recipe('ASSEMBLER', [Ingredient('IRON_PLATE', 11.25), Ingredient('RUBBER', 3.75)], [Ingredient('REINFORCED_IRON_PLATE', 3.75)]),
    'BOLTED_IRON_PLATE': Recipe('ASSEMBLER', [Ingredient('IRON_PLATE', 90), Ingredient('SCREW', 250)], [Ingredient('REINFORCED_IRON_PLATE', 15)]),
    'STITCHED_IRON_PLATE': Recipe('ASSEMBLER', [Ingredient('IRON_PLATE', 18.75), Ingredient('WIRE', 37.5)], [Ingredient('REINFORCED_IRON_PLATE', 5.63)]),

    'COPPER_SHEET': Recipe('CONSTRUCTOR', [Ingredient('COPPER_INGOT', 20)], [Ingredient('COPPER_SHEET', 10)]),
    'STEAMED_COPPER_SHEET': Recipe('REFINERY', [Ingredient('COPPER_INGOT', 22.5), Ingredient('WATER', 22.5)], [Ingredient('COPPER_SHEET', 22.5)]),

    'ALCLAD_ALUMINUM_SHEET': Recipe('ASSEMBLER', [Ingredient('ALUMINUM_INGOT', 30), Ingredient('COPPER_INGOT', 10)], [Ingredient('ALCLAD_ALUMINUM_SHEET', 30)]),

    'ALUMINUM_CASING': Recipe('CONSTRUCTOR', [Ingredient('ALUMINUM_INGOT', 90)], [Ingredient('ALUMINUM_CASING', 60)]),
    'ALCLAD_CASING': Recipe('ASSEMBLER', [Ingredient('ALUMINUM_INGOT', 150), Ingredient('COPPER_INGOT', 75)], [Ingredient('ALUMINUM_CASING', 112.5)]),

    'STEEL_PIPE': Recipe('CONSTRUCTOR', [Ingredient('STEEL_INGOT', 30)], [Ingredient('STEEL_PIPE', 20)]),
    'STEEL_BEAM': Recipe('CONSTRUCTOR', [Ingredient('STEEL_INGOT', 60)], [Ingredient('STEEL_BEAM', 15)]),

    'ENCASED_INDUSTRIAL_BEAM': Recipe('ASSEMBLER', [Ingredient('STEEL_BEAM', 24), Ingredient('CONCRETE', 30)], [Ingredient('ENCASED_INDUSTRIAL_BEAM', 6)]),
    'ENCASED_INDUSTRIAL_PIPE': Recipe('ASSEMBLER', [Ingredient('STEEL_PIPE', 28), Ingredient('CONCRETE', 20)], [Ingredient('ENCASED_INDUSTRIAL_BEAM', 4)]),

    'MODULAR_FRAME': Recipe('ASSEMBLER', [Ingredient('REINFORCED_IRON_PLATE', 3), Ingredient('IRON_ROD', 12)], [Ingredient('MODULAR_FRAME', 2)]),
    'BOLTED_FRAME': Recipe('ASSEMBLER', [Ingredient('REINFORCED_IRON_PLATE', 7.5), Ingredient('SCREW', 140)], [Ingredient('MODULAR_FRAME', 5)]),
    'STEELED_FRAME': Recipe('ASSEMBLER', [Ingredient('REINFORCED_IRON_PLATE', 2), Ingredient('STEEL_PIPE', 10)], [Ingredient('MODULAR_FRAME', 3)]),

    'HEAVY_MODULAR_FRAME': Recipe('MANUFACTURER', [Ingredient('MODULAR_FRAME', 10), Ingredient('ENCASED_INDUSTRIAL_BEAM', 10), Ingredient('STEEL_PIPE', 30), Ingredient('SCREW', 200)], [Ingredient('HEAVY_MODULAR_FRAME', 2)]),
    'HEAVY_ENCASED_FRAME': Recipe('MANUFACTURER', [Ingredient('MODULAR_FRAME', 7.5), Ingredient('ENCASED_INDUSTRIAL_BEAM', 9.38), Ingredient('STEEL_PIPE', 33.75), Ingredient('CONCRETE', 20.63)], [Ingredient('HEAVY_MODULAR_FRAME', 2.81)]),
    'HEAVY_FLEXIBLE_FRAME': Recipe('MANUFACTURER', [Ingredient('MODULAR_FRAME', 18.75), Ingredient('ENCASED_INDUSTRIAL_BEAM', 11.25), Ingredient('RUBBER', 75), Ingredient('SCREW', 390)], [Ingredient('HEAVY_MODULAR_FRAME', 3.75)]),

    'FUSED_MODULAR_FRAME': Recipe('BLENDER', [Ingredient('HEAVY_MODULAR_FRAME', 1.5), Ingredient('ALUMINUM_CASING', 75), Ingredient('NITROGEN_GAS', 37.5)], [Ingredient('FUSED_MODULAR_FRAME', 1.5)]),
    'HEAT_FUSED_FRAME': Recipe('BLENDER', [Ingredient('HEAVY_MODULAR_FRAME', 3), Ingredient('ALUMINUM_INGOT', 150), Ingredient('NITRIC_ACID', 24), Ingredient('FUEL', 30)], [Ingredient('FUSED_MODULAR_FRAME', 3)]),

    'POLYESTER_FABRIC': Recipe('REFINERY', [Ingredient('POLYMER_RESIN', 30), Ingredient('WATER', 30)], [Ingredient('FABRIC', 30)]),
    
    'PLASTIC': Recipe('REFINERY', [Ingredient('CRUDE_OIL', 30)], [Ingredient('PLASTIC', 20), Ingredient('HEAVY_OIL_RESIDUE', 10)]),
    'RESIDUAL_PLASTIC': Recipe('REFINERY', [Ingredient('POLYMER_RESIN', 60), Ingredient('WATER', 20)], [Ingredient('PLASTIC', 20)]),
    'RECYCLED_PLASTIC': Recipe('REFINERY', [Ingredient('RUBBER', 30), Ingredient('FUEL', 30)], [Ingredient('PLASTIC', 60)]),

    'RUBBER': Recipe('REFINERY', [Ingredient('CRUDE_OIL', 30)], [Ingredient('RUBBER', 20), Ingredient('HEAVY_OIL_RESIDUE', 20)]),
    'RESIDUAL_RUBBER': Recipe('REFINERY', [Ingredient('POLYMER_RESIN', 40), Ingredient('WATER', 40)], [Ingredient('RUBBER', 20)]),
    'RECYCLED_RUBBER': Recipe('REFINERY', [Ingredient('PLASTIC', 30), Ingredient('FUEL', 30)], [Ingredient('RUBBER', 60)]),
    
    # industrial parts

    'ROTOR': Recipe('ASSEMBLER', [Ingredient('IRON_ROD', 20), Ingredient('SCREW', 100)], [Ingredient('ROTOR', 4)]),
    'COPPER_ROTOR': Recipe('ASSEMBLER', [Ingredient('COPPER_SHEET', 22.5), Ingredient('SCREW', 195)], [Ingredient('ROTOR', 11.25)]),
    'STEEL_ROTOR': Recipe('ASSEMBLER', [Ingredient('STEEL_PIPE', 10), Ingredient('WIRE', 30)], [Ingredient('ROTOR', 5)]),

    'STATOR': Recipe('ASSEMBLER', [Ingredient('STEEL_PIPE', 15), Ingredient('WIRE', 40)], [Ingredient('STATOR', 5)]),
    'QUICKWIRE_STATOR': Recipe('ASSEMBLER', [Ingredient('STEEL_PIPE', 16), Ingredient('QUICKWIRE', 60)], [Ingredient('STATOR', 8)]),

    'BATTERY': Recipe('BLENDER', [Ingredient('ALUMINUM_CASING', 20), Ingredient('SULFURIC_ACID', 50), Ingredient('ALUMINA_SOLUTION', 40)], [Ingredient('BATTERY', 20), Ingredient('WATER', 30)]),
    'CLASSIC_BATTERY': Recipe('MANUFACTURER', [Ingredient('SULFUR', 45), Ingredient('ALCLAD_ALUMINUM_SHEET', 52.5), Ingredient('PLASTIC', 60), Ingredient('WIRE', 90)], [Ingredient('BATTERY', 30)]),

    'MOTOR': Recipe('ASSEMBLER', [Ingredient('ROTOR', 10), Ingredient('STATOR', 10)], [Ingredient('MOTOR', 5)]),
    'ELECTRIC_MOTOR': Recipe('ASSEMBLER', [Ingredient('ROTOR', 7.5), Ingredient('ELECTROMAGNETIC_CONTROL_ROD', 3.75)], [Ingredient('MOTOR', 7.5)]),
    'RIGOUR_MOTOR': Recipe('MANUFACTURER', [Ingredient('ROTOR', 3.75), Ingredient('STATOR', 3.75), Ingredient('CRYSTAL_OSCILLATOR', 1.25)], [Ingredient('MOTOR', 7.5)]),

    'HEAT_SINK': Recipe('ASSEMBLER', [Ingredient('ALCLAD_ALUMINUM_SHEET', 37.5), Ingredient('COPPER_SHEET', 22.5)], [Ingredient('HEAT_SINK', 7.5)]),
    'HEAT_EXCHANGER': Recipe('ASSEMBLER', [Ingredient('ALUMINUM_CASING', 30), Ingredient('RUBBER', 30)], [Ingredient('HEAT_SINK', 10)]),

    'COOLING_SYSTEM': Recipe('BLENDER', [Ingredient('HEAT_SINK', 12), Ingredient('RUBBER', 12), Ingredient('WATER', 30), Ingredient('NITROGEN_GAS', 150)], [Ingredient('COOLING_SYSTEM', 6)]),
    'COOLING_DEVICE': Recipe('BLENDER', [Ingredient('HEAT_SINK', 9.38), Ingredient('MOTOR', 1.88), Ingredient('NITROGEN_GAS', 45)], [Ingredient('COOLING_SYSTEM', 3.75)]),

    'TURBO_MOTOR': Recipe('MANUFACTURER', [Ingredient('COOLING_SYSTEM', 7.5), Ingredient('RADIO_CONTROL_UNIT', 3.75), Ingredient('MOTOR', 7.5), Ingredient('RUBBER', 45)], [Ingredient('TURBO_MOTOR', 1.88)]),
    'TURBO_ELECTRIC_MOTOR': Recipe('MANUFACTURER', [Ingredient('MOTOR', 6.56), Ingredient('RADIO_CONTROL_UNIT', 8.44), Ingredient('ELECTROMAGNETIC_CONTROL_ROD', 4.69), Ingredient('ROTOR', 6.56)], [Ingredient('TURBO_MOTOR', 2.81)]),
    'TURBO_PRESSURE_MOTOR': Recipe('MANUFACTURER', [Ingredient('MOTOR', 7.5), Ingredient('PRESSURE_CONVERSION_CUBE',1.88), Ingredient('PACKAGED_NITROGEN_GAS', 45), Ingredient('STATOR', 15)], [Ingredient('TURBO_MOTOR', 3.75)]),

    # electronics

    'WIRE': Recipe('CONSTRUCTOR', [Ingredient('COPPER_INGOT', 15)], [Ingredient('WIRE', 30)]),
    'CATERIUM_WIRE': Recipe('CONSTRUCTOR', [Ingredient('CATERIUM_INGOT', 15)], [Ingredient('WIRE', 120)]),
    'FUSED_WIRE': Recipe('ASSEMBLER', [Ingredient('COPPER_INGOT', 12), Ingredient('CATERIUM_INGOT', 3)], [Ingredient('WIRE', 90)]),
    'IRON_WIRE': Recipe('CONSTRUCTOR', [Ingredient('IRON_INGOT', 12.5)], [Ingredient('WIRE', 22.5)]),

    'CABLE': Recipe('CONSTRUCTOR', [Ingredient('WIRE', 60)], [Ingredient('CABLE', 30)]),
    'COATED_CABLE': Recipe('REFINERY', [Ingredient('WIRE', 37.5), Ingredient('HEAVY_OIL_RESIDUE', 15)], [Ingredient('CABLE', 67.5)]),
    'INSULATED_CABLE': Recipe('ASSEMBLER', [Ingredient('WIRE', 45), Ingredient('RUBBER', 30)], [Ingredient('CABLE', 100)]),
    'QUICKWIRE_CABLE': Recipe('ASSEMBLER', [Ingredient('QUICKWIRE', 7.5), Ingredient('RUBBER', 5)], [Ingredient('CABLE', 27.5)]),

    'QUICKWIRE': Recipe('CONSTRUCTOR', [Ingredient('CATERIUM_INGOT', 12)], [Ingredient('QUICKWIRE', 60)]),
    'FUSED_QUICKWIRE': Recipe('ASSEMBLER', [Ingredient('CATERIUM_INGOT', 7.5), Ingredient('COPPER_INGOT', 37.5)], [Ingredient('QUICKWIRE', 90)]),

    'CIRCUIT_BOARD': Recipe('ASSEMBLER', [Ingredient('PLASTIC', 30), Ingredient('COPPER_SHEET', 15)], [Ingredient('CIRCUIT_BOARD', 7.5)]),
    'CATERIUM_CIRCUIT_BOARD': Recipe('ASSEMBLER', [Ingredient('PLASTIC', 12.5), Ingredient('QUICKWIRE', 37.5)], [Ingredient('CIRCUIT_BOARD', 8.75)]),
    'ELECTRODE_CIRCUIT_BOARD': Recipe('ASSEMBLER', [Ingredient('RUBBER', 30), Ingredient('PETROLEUM_COKE', 45)], [Ingredient('CIRCUIT_BOARD', 5)]),
    'SILICON_CIRCUIT_BOARD': Recipe('ASSEMBLER', [Ingredient('COPPER_SHEET', 27.5), Ingredient('SILICA', 27.5)], [Ingredient('CIRCUIT_BOARD', 12.5)]),

    'AI_LIMITER': Recipe('ASSEMBLER', [Ingredient('COPPER_SHEET', 25), Ingredient('QUICKWIRE', 100)], [Ingredient('AI_LIMITER', 5)]),

    'HIGH_SPEED_CONNECTOR': Recipe('MANUFACTURER', [Ingredient('QUICKWIRE', 210), Ingredient('CABLE', 37.5), Ingredient('CIRCUIT_BOARD', 3.75)], [Ingredient('HIGH_SPEED_CONNECTOR', 3.75)]),
    'SILICON_HIGH_SPEED_CONNECTOR': Recipe('MANUFACTURER', [Ingredient('QUICKWIRE', 90), Ingredient('SILICA', 37.5), Ingredient('CIRCUIT_BOARD', 3)], [Ingredient('HIGH_SPEED_CONNECTOR', 3)]),

    # communication

    'COMPUTER': Recipe('MANUFACTURER', [Ingredient('CIRCUIT_BOARD', 25), Ingredient('CABLE', 22.5), Ingredient('PLASTIC', 45), Ingredient('SCREW', 130)], [Ingredient('COMPUTER', 2.5)]),
    'CATERIUM_COMPUTER': Recipe('MANUFACTURER', [Ingredient('CIRCUIT_BOARD', 26.25), Ingredient('QUICKWIRE', 105), Ingredient('RUBBER', 45)], [Ingredient('COMPUTER', 3.75)]),
    'CRYSTAL_COMPUTER': Recipe('ASSEMBLER', [Ingredient('CIRCUIT_BOARD', 7.5), Ingredient('CRYSTAL_OSCILLATOR', 2.81)], [Ingredient('COMPUTER', 2.81)]),

    'SUPERCOMPUTER': Recipe('MANUFACTURER', [Ingredient('COMPUTER', 3.75), Ingredient('AI_LIMITER', 3.75), Ingredient('HIGH_SPEED_CONNECTOR', 5.63), Ingredient('PLASTIC', 52.5)], [Ingredient('SUPERCOMPUTER', 1.88)]),
    'OC_SUPERCOMPUTER': Recipe('ASSEMBLER', [Ingredient('RADIO_CONTROL_UNIT', 9), Ingredient('COOLING_SYSTEM', 9)], [Ingredient('SUPERCOMPUTER', 3)]),
    'SUPER_STATE_COMPUTER': Recipe('MANUFACTURER', [Ingredient('COMPUTER', 3.6), Ingredient('ELECTROMAGNETIC_CONTROL_ROD', 2.4), Ingredient('BATTERY', 24), Ingredient('WIRE', 54)], [Ingredient('SUPERCOMPUTER', 2.4)]),

    'RADIO_CONTROL_UNIT': Recipe('MANUFACTURER', [Ingredient('ALUMINUM_CASING', 40), Ingredient('CRYSTAL_OSCILLATOR', 1.25), Ingredient('COMPUTER', 1.25)], [Ingredient('RADIO_CONTROL_UNIT', 2.5)]),
    'RADIO_CONNECTION_UNIT': Recipe('MANUFACTURER', [Ingredient('HEAT_SINK', 15), Ingredient('HIGH_SPEED_CONNECTOR', 7.5), Ingredient('QUARTZ_CRYSTAL', 45)], [Ingredient('RADIO_CONTROL_UNIT', 3.75)]),
    'RADIO_CONTROL_SYSTEM': Recipe('MANUFACTURER', [Ingredient('CRYSTAL_OSCILLATOR', 1.5), Ingredient('CIRCUIT_BOARD', 15), Ingredient('ALUMINUM_CASING', 90), Ingredient('RUBBER', 45)], [Ingredient('RADIO_CONTROL_UNIT', 4.5)]),

    'CRYSTAL_OSCILLATOR': Recipe('MANUFACTURER', [Ingredient('QUARTZ_CRYSTAL', 18), Ingredient('CABLE', 14), Ingredient('REINFORCED_IRON_PLATE', 2.5)], [Ingredient('CRYSTAL_OSCILLATOR', 1)]),
    'INSULATED_CRYSTAL_OSCILLATOR': Recipe('MANUFACTURER', [Ingredient('QUARTZ_CRYSTAL', 18.75), Ingredient('RUBBER', 13.13), Ingredient('AI_LIMITER', 1.88)], [Ingredient('CRYSTAL_OSCILLATOR', 1.88)]),

    # containers

    'EMPTY_CANISTER': Recipe('CONSTRUCTOR', [Ingredient('PLASTIC', 30)], [Ingredient('EMPTY_CANISTER', 60)]),
    'COATED_IRON_CANISTER': Recipe('ASSEMBLER', [Ingredient('IRON_PLATE', 30), Ingredient('COPPER_SHEET', 15)], [Ingredient('EMPTY_CANISTER', 60)]),
    'STEEL_CANISTER': Recipe('CONSTRUCTOR', [Ingredient('STEEL_INGOT', 60)], [Ingredient('EMPTY_CANISTER', 40)]),

    'EMPTY_FLUID_TANK': Recipe('CONSTRUCTOR', [Ingredient('ALUMINUM_INGOT', 60)], [Ingredient('EMPTY_FLUID_TANK', 60)]),

    'PRESSURE_CONVERSION_CUBE': Recipe('ASSEMBLER', [Ingredient('FUSED_MODULAR_FRAME', 1), Ingredient('RADIO_CONTROL_UNIT', 2)], [Ingredient('PRESSURE_CONVERSION_CUBE', 1)]),

    'PACKAGED_WATER': Recipe('PACKAGER', [Ingredient('WATER', 60), Ingredient('EMPTY_CANISTER', 60)], [Ingredient('PACKAGED_WATER', 60)]),
    'PACKAGED_ALUMINA_SOLUTION': Recipe('PACKAGER', [Ingredient('ALUMINA_SOLUTION', 120), Ingredient('EMPTY_CANISTER', 120)], [Ingredient('PACKAGED_ALUMINA_SOLUTION', 120)]),
    'PACKAGED_SULFURIC_ACID': Recipe('PACKAGER', [Ingredient('SULFURIC_ACID', 40), Ingredient('EMPTY_CANISTER', 40)], [Ingredient('PACKAGED_SULFURIC_ACID', 40)]),
    'PACKAGED_NITRIC_ACID': Recipe('PACKAGER', [Ingredient('NITRIC_ACID', 30), Ingredient('EMPTY_FLUID_TANK', 30)], [Ingredient('PACKAGED_NITRIC_ACID', 30)]),
    'PACKAGED_NITROGEN_GAS': Recipe('PACKAGER', [Ingredient('NITROGEN_GAS', 240), Ingredient('EMPTY_FLUID_TANK', 60)], [Ingredient('PACKAGED_NITROGEN_GAS', 60)]),
    
    # fuels
    
    'COMPACTED_COAL': Recipe('ASSEMBLER', [Ingredient('COAL', 25), Ingredient('SULFUR', 25)], [Ingredient('COMPACTED_COAL', 25)]),
    'PACKAGED_OIL': Recipe('PACKAGER', [Ingredient('CRUDE_OIL', 30), Ingredient('EMPTY_CANISTER', 30)], [Ingredient('PACKAGED_OIL', 30)]),
    'PACKAGED_HEAVY_OIL_RESIDUE': Recipe('PACKAGER', [Ingredient('HEAVY_OIL_RESIDUE', 30), Ingredient('EMPTY_CANISTER', 30)], [Ingredient('PACKAGED_HEAVY_OIL_RESIDUE', 30)]),
    
    'PACKAGED_FUEL': Recipe('PACKAGER', [Ingredient('FUEL', 40), Ingredient('EMPTY_CANISTER', 40)], [Ingredient('PACKAGED_FUEL', 40)]),
    'DILUTED_PACKAGED_FUEL': Recipe('REFINERY', [Ingredient('HEAVY_OIL_RESIDUE', 30), Ingredient('PACKAGED_WATER', 60)], [Ingredient('PACKAGED_FUEL', 60)]),
    
    'PACKAGED_TURBOFUEL': Recipe('PACKAGER', [Ingredient('TURBOFUEL', 20), Ingredient('EMPTY_CANISTER', 20)], [Ingredient('PACKAGED_TURBOFUEL', 20)]),

    # consumables
    
    'BEACON': Recipe('MANUFACTURER', [Ingredient('IRON_PLATE', 22.5), Ingredient('IRON_ROD', 7.5), Ingredient('WIRE', 112.5), Ingredient('CABLE', 15)], [Ingredient('BEACON', 7.5)]),
    'CRYSTAL_BEACON': Recipe('MANUFACTURER', [Ingredient('STEEL_BEAM', 2), Ingredient('STEEL_PIPE', 8), Ingredient('CRYSTAL_OSCILLATOR', 0.5)], [Ingredient('BEACON', 10)]),

    # nuclear

    'ELECTROMAGNETIC_CONTROL_ROD': Recipe('ASSEMBLER', [Ingredient('STATOR', 6), Ingredient('AI_LIMITER', 4)], [Ingredient('ELECTROMAGNETIC_CONTROL_ROD', 4)]),
    'ELECTROMAGNETIC_CONNECTION_ROD': Recipe('ASSEMBLER', [Ingredient('STATOR', 8), Ingredient('HIGH_SPEED_CONNECTOR', 4)], [Ingredient('ELECTROMAGNETIC_CONTROL_ROD', 8)]),

    # subtract sulfuric acid output from input (40 - 10 = 30)
    'ENCASED_URANIUM_CELL': Recipe('BLENDER', [Ingredient('URANIUM', 50), Ingredient('CONCRETE', 15), Ingredient('SULFURIC_ACID', 30)], [Ingredient('ENCASED_URANIUM_CELL', 25)]),
    'INFUSED_URANIUM_CELL': Recipe('MANUFACTURER', [Ingredient('URANIUM', 25), Ingredient('SILICA', 15), Ingredient('SULFUR', 25), Ingredient('QUICKWIRE', 75)], [Ingredient('ENCASED_URANIUM_CELL', 20)]),

    'NON_FISSILE_URANIUM': Recipe('BLENDER', [Ingredient('URANIUM_WASTE', 37.5), Ingredient('SILICA', 25), Ingredient('NITRIC_ACID', 15), Ingredient('SULFURIC_ACID', 15)], [Ingredient('NON_FISSILE_URANIUM', 50), Ingredient('WATER', 15)]),
    'FERTILE_URANIUM': Recipe('BLENDER', [Ingredient('URANIUM_WASTE', 25), Ingredient('URANIUM', 25), Ingredient('NITRIC_ACID', 15), Ingredient('SULFURIC_ACID', 25)], [Ingredient('NON_FISSILE_URANIUM', 100), Ingredient('WATER', 40)]),

    'PLUTONIUM_PELLET': Recipe('PARTICAL_ACCELERATOR_PLUTONIUM_PELLET', [Ingredient('NON_FISSILE_URANIUM', 100), Ingredient('URANIUM_WASTE', 25)], [Ingredient('PLUTONIUM_PELLET', 30)]),

    'ENCASED_PLUTONIUM_CELL': Recipe('ASSEMBLER', [Ingredient('PLUTONIUM_PELLET', 10), Ingredient('CONCRETE', 20)], [Ingredient('ENCASED_PLUTONIUM_CELL', 5)]),
    'INSTANT_PLUTONIUM_CELL': Recipe('PARTICAL_ACCELERATOR_PLUTONIUM_CELL', [Ingredient('NON_FISSILE_URANIUM', 75), Ingredient('ALUMINUM_CASING', 10)], [Ingredient('ENCASED_PLUTONIUM_CELL', 10)]),

    'URANIUM_FUEL_ROD': Recipe('MANUFACTURER', [Ingredient('ENCASED_URANIUM_CELL', 20), Ingredient('ENCASED_INDUSTRIAL_BEAM', 1.2), Ingredient('ELECTROMAGNETIC_CONTROL_ROD', 2)], [Ingredient('URANIUM_FUEL_ROD', 0.4)]),
    'URANIUM_FUEL_UNIT': Recipe('MANUFACTURER', [Ingredient('ENCASED_URANIUM_CELL', 20), Ingredient('ELECTROMAGNETIC_CONTROL_ROD', 2), Ingredient('CRYSTAL_OSCILLATOR', 0.6), Ingredient('BEACON', 1.2)], [Ingredient('URANIUM_FUEL_ROD', 0.6)]),

    'PLUTONIUM_FUEL_ROD': Recipe('MANUFACTURER', [Ingredient('ENCASED_PLUTONIUM_CELL', 7.5), Ingredient('STEEL_BEAM', 4.5), Ingredient('ELECTROMAGNETIC_CONTROL_ROD', 1.5), Ingredient('HEAT_SINK', 2.5)], [Ingredient('PLUTONIUM_FUEL_ROD', 0.25)]),
    'PLUTONIUM_FUEL_UNIT': Recipe('ASSEMBLER', [Ingredient('ENCASED_PLUTONIUM_CELL', 10), Ingredient('PRESSURE_CONVERSION_CUBE', 0.5)], [Ingredient('PLUTONIUM_FUEL_ROD', 0.5)]),

    # space elevator

    'SMART_PLATING': Recipe('ASSEMBLER', [Ingredient('REINFORCED_IRON_PLATE', 2), Ingredient('ROTOR', 2)], [Ingredient('SMART_PLATING', 2)]),
    'PLASTIC_SMART_PLATING': Recipe('MANUFACTURER', [Ingredient('REINFORCED_IRON_PLATE', 2.5), Ingredient('ROTOR', 2.5), Ingredient('PLASTIC', 7.5)], [Ingredient('SMART_PLATING', 5)]),

    'VERSATILE_FRAMEWORK': Recipe('ASSEMBLER', [Ingredient('MODULAR_FRAME', 2.5), Ingredient('STEEL_PIPE', 30)], [Ingredient('VERSATILE_FRAMEWORK', 5)]),
    'FLEXIBLE_FRAMEWORK':Recipe('MANUFACTURER', [Ingredient('MODULAR_FRAME', 3.75), Ingredient('STEEL_BEAM', 22.5), Ingredient('RUBBER', 30)], [Ingredient('VERSATILE_FRAMEWORK', 7.5)]),

    'AUTOMATED_WIRING': Recipe('ASSEMBLER', [Ingredient('CABLE', 50), Ingredient('STATOR', 2.5)], [Ingredient('AUTOMATED_WIRING', 2.5)]),
    'AUTOMATED_SPEED_WIRING':Recipe('MANUFACTURER', [Ingredient('STATOR', 3.75), Ingredient('WIRE', 75), Ingredient('HIGH_SPEED_CONNECTOR', 1.88)], [Ingredient('AUTOMATED_WIRING', 7.5)]),

    'MODULAR_ENGINE': Recipe('MANUFACTURER', [Ingredient('MOTOR', 2), Ingredient('RUBBER', 15), Ingredient('SMART_PLATING', 2)], [Ingredient('MODULAR_ENGINE', 1)]),

    'ADAPTIVE_CONTROL_UNIT': Recipe('MANUFACTURER', [Ingredient('AUTOMATED_WIRING', 7.5), Ingredient('CIRCUIT_BOARD', 5), Ingredient('HEAVY_MODULAR_FRAME', 1), Ingredient('COMPUTER', 1)], [Ingredient('ADAPTIVE_CONTROL_UNIT', 1)]),

    'ASSEMBLY_DIRECTOR_SYSTEM': Recipe('ASSEMBLER', [Ingredient('ADAPTIVE_CONTROL_UNIT', 1.5), Ingredient('SUPERCOMPUTER', 0.75)], [Ingredient('ASSEMBLY_DIRECTOR_SYSTEM', 0.75)]),

    'MAGNETIC_FIELD_GENERATOR': Recipe('MANUFACTURER', [Ingredient('VERSATILE_FRAMEWORK', 2.5), Ingredient('ELECTROMAGNETIC_CONTROL_ROD', 1),  Ingredient('BATTERY', 5)], [Ingredient('MAGNETIC_FIELD_GENERATOR', 1)]),

    'THERMAL_PROPULSION_ROCKET': Recipe('MANUFACTURER', [Ingredient('MODULAR_ENGINE', 2.5), Ingredient('TURBO_MOTOR', 1), Ingredient('COOLING_SYSTEM', 3), Ingredient('FUSED_MODULAR_FRAME', 1)], [Ingredient('THERMAL_PROPULSION_ROCKET', 1)]),

    'NUCLEAR_PASTA': Recipe('PARTICAL_ACCELERATOR_NUCLEAR_PASTA', [Ingredient('COPPER_POWDER', 100), Ingredient('PRESSURE_CONVERSION_CUBE', 0.5)], [Ingredient('NUCLEAR_PASTA', 0.5)]),

}