#
#  Copyright (2024) Hewlett Packard Enterprise Development LP
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

"""
Python APIs to simulate various CAMs (Content Addressable Memory) on GPUs at scale.
"""

import importlib.metadata

from .cam import (
    acam_count_mismatches,
    acam_match,
    acam_reduce_sum,
    tcam_hamming_distance,
    tcam_match,
    tcam_reduce_sum,
)
from .util import flip_indices

__all__ = [
    "acam_count_mismatches",
    "acam_match",
    "acam_reduce_sum",
    "flip_indices",
    "tcam_hamming_distance",
    "tcam_match",
    "tcam_reduce_sum",
]

# https://github.com/python-poetry/poetry/issues/144#issuecomment-1488038660
__version__ = importlib.metadata.version("campie")
