from tools.configs.dump import DumpConfig
from tools.configs.font import FontConfig
import math

version = '1.10.0'
version_time = '2025-08-24'

dump_configs = [
    DumpConfig(
        font_name='ASC12',
        font_type='asc',
        font_size=12,
    ),
    DumpConfig(
        font_name='ASC16',
        font_type='asc',
        font_size=16,
    ),
    DumpConfig(
        font_name='ASC48',
        font_type='asc',
        font_size=48,
    ),
    DumpConfig(
        font_name='HZK12',
        font_type='hzk',
        font_size=12,
    ),
    DumpConfig(
        font_name='HZK14',
        font_type='hzk',
        font_size=14,
    ),
    DumpConfig(
        font_name='HZK16',
        font_type='hzk',
        font_size=16,
    ),
    DumpConfig(
        font_name='HZK16F',
        font_type='hzk',
        font_size=16,
    ),
    DumpConfig(
        font_name='HZK16S',
        font_type='hzk',
        font_size=16,
    ),
    DumpConfig(
        font_name='HZK24F',
        font_type='hzk',
        font_size=24,
    ),
    DumpConfig(
        font_name='HZK24H',
        font_type='hzk',
        font_size=24,
    ),
    DumpConfig(
        font_name='HZK24K',
        font_type='hzk',
        font_size=24,
    ),
    DumpConfig(
        font_name='HZK24S',
        font_type='hzk',
        font_size=24,
    ),
    DumpConfig(
        font_name='HZK32',
        font_type='hzk',
        font_size=32,
    ),
    DumpConfig(
        font_name='HZK40',
        font_type='hzk',
        font_size=40,
    ),
    DumpConfig(
        font_name='HZK48',
        font_type='hzk',
        font_size=48,
    ),
]

font_configs = [
    FontConfig(
        font_size=12,
        ascent=9,
        descent=-3,
        x_height=6,
        cap_height=8,
        source_names=['ASC12', 'HZK12'],
    ),
    FontConfig(
        font_size=16,
        ascent=12,
        descent=-4,
        x_height=7,
        cap_height=10,
        source_names=['ASC16', 'HZK16'],
    ),
    FontConfig(
        font_size=16,
        ascent=16 * 3 // 4,
        descent=-16 // 4,
        x_height=math.floor(16 / 4 + 3),
        cap_height=math.floor(16 * 2 / 3),
        source_names=['ASC16', 'HZK16F'],
        family='F',
    ),
    FontConfig(
        font_size=16,
        ascent=16 * 3 // 4,
        descent=-16 // 4,
        x_height=math.floor(16 / 4 + 3),
        cap_height=math.floor(16 * 2 / 3),
        source_names=['ASC16', 'HZK16S'],
        family='S',
    ),
    FontConfig(
        font_size=24,
        ascent=24 * 3 // 4,
        descent=-24 // 4,
        x_height=math.floor(24 / 4 + 3),
        cap_height=math.floor(24 * 2 / 3),
        source_names=['HZK24F'],
        family='F',
    ),
    FontConfig(
        font_size=24,
        ascent=24 * 3 // 4,
        descent=-24 // 4,
        x_height=math.floor(24 / 4 + 3),
        cap_height=math.floor(24 * 2 / 3),
        source_names=['HZK24H'],
        family='H',
    ),
    FontConfig(
        font_size=24,
        ascent=24 * 3 // 4,
        descent=-24 // 4,
        x_height=math.floor(24 / 4 + 3),
        cap_height=math.floor(24 * 2 / 3),
        source_names=['HZK24K'],
        family='K',
    ),
    FontConfig(
        font_size=24,
        ascent=24 * 3 // 4,
        descent=-24 // 4,
        x_height=math.floor(24 / 4 + 3),
        cap_height=math.floor(24 * 2 / 3),
        source_names=['HZK24S'],
        family='S',
    ),
    FontConfig(
        font_size=32,
        ascent=32 * 3 // 4,
        descent=-32 // 4,
        x_height=math.floor(32 / 4 + 3),
        cap_height=math.floor(32 * 2 / 3),
        source_names=['HZK32'],
    ),
    FontConfig(
        font_size=40,
        ascent=40 * 3 // 4,
        descent=-40 // 4,
        x_height=math.floor(40 / 4 + 3),
        cap_height=math.floor(40 * 2 / 3),
        source_names=['HZK40'],
    ),
    FontConfig(
        font_size=48,
        ascent=48 * 3 // 4,
        descent=-48 // 4,
        x_height=math.floor(48 / 4 + 3),
        cap_height=math.floor(48 * 2 / 3),
        source_names=['ASC48', 'HZK48'],
    ),
]
