"""Rust backend typing stubs."""

from dataclasses import dataclass, field
from typing import Optional, Tuple

import polars as pl

@dataclass
class DataLoader:
    root_dir: str
    dataset_name: str
    dataset_type: str
    split_name: str
    num_accumulated_sweeps: int
    memory_map: bool

    file_index: pl.DataFrame = field(init=False)

    def get(self, index: int) -> Sweep: ...
    def __len__(self) -> int: ...

@dataclass
class Sweep:
    city_pose: pl.DataFrame
    lidar: pl.DataFrame
    sweep_uuid: Tuple[str, int]
    cuboids: Optional[pl.DataFrame]
