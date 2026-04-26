"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .arafura import ArafuraFetcher
from .asm import AsmFetcher
from .china_rare_earth import ChinaRareEarthFetcher
from .energy_fuels import EnergyFuelsFetcher
from .hastings import HastingsFetcher
from .iluka import IlukaFetcher
from .lynas import LynasFetcher
from .mp_materials import MpMaterialsFetcher
from .neo import NeoFetcher
from .north_rare_earth import NorthRareEarthFetcher
from .pensana import PensanaFetcher
from .rainbow import RainbowFetcher
from .shenghe import ShengheFetcher
from .ucore import UcoreFetcher
from .vital import VitalFetcher

FETCHERS = {
    "arafura": ArafuraFetcher,
    "asm": AsmFetcher,
    "china_rare_earth": ChinaRareEarthFetcher,
    "energy_fuels": EnergyFuelsFetcher,
    "hastings": HastingsFetcher,
    "iluka": IlukaFetcher,
    "lynas": LynasFetcher,
    "mp_materials": MpMaterialsFetcher,
    "neo": NeoFetcher,
    "north_rare_earth": NorthRareEarthFetcher,
    "pensana": PensanaFetcher,
    "rainbow": RainbowFetcher,
    "shenghe": ShengheFetcher,
    "ucore": UcoreFetcher,
    "vital": VitalFetcher,
}
