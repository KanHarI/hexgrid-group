import dataclasses

from __future__ import annotations


ROTATION_TO_L_TO_L = {
    0: 1,
    1: 0,
    2: -1,
    3: -1,
    4: 0,
    5: 1,
}

ROTATION_TO_L_TO_R = {
    0: 0,
    1: -1,
    2: -1,
    3: 0,
    4: 1,
    5: 1,
}

ROTATION_TO_R_TO_L = {0: 0, 1: 1, 2: 1, 3: 0, 4: -1, 5: -1}

ROTATION_TO_R_TO_R = {0: 1, 1: 1, 2: 0, 3: -1, 4: -1, 5: 0}


@dataclasses.dataclass(frozen=True, unsafe_hash=True, repr=True, eq=True)
class HexGroupRepresentation:
    """An additive group"""

    L: int  # Left-and-up steps
    R: int  # Right-and-up steps
    C: int  # Rotation (0 to 5)
    M: bool  # Mirror

    def __add__(self, other: HexGroupRepresentation) -> HexGroupRepresentation:
        other_l_to_l = ROTATION_TO_L_TO_L[self.C]
        other_l_to_r = ROTATION_TO_L_TO_R[self.C]
        other_r_to_l = ROTATION_TO_R_TO_L[self.C]
        other_r_to_r = ROTATION_TO_R_TO_R[self.C]

        other_left = other.R if self.M else other.L
        other_right = other.L if self.M else other.R
        other_c = (6 - other.C) if self.M else other.C

        return HexGroupRepresentation(
            L=self.L + other_l_to_l * other_left + other_r_to_l * other_right,
            R=self.R + other_l_to_r * other_left + other_r_to_r * other_right,
            C=(self.C + other_c) % 6,
            M=self.M ^ other.M,
        )

    def __neg__(self) -> HexGroupRepresentation:
        self_l_to_l = ROTATION_TO_L_TO_L[self.C]
        self_l_to_r = ROTATION_TO_L_TO_R[self.C]
        self_r_to_l = ROTATION_TO_R_TO_L[self.C]
        self_r_to_r = ROTATION_TO_R_TO_R[self.C]

        self_left = self.R if self.M else self.L
        self_right = self.L if self.M else self.R

        return HexGroupRepresentation(
            L=-(self_left * self_l_to_l + self_right * self_r_to_l),
            R=-(self_left * self_l_to_r + self_right * self_r_to_r),
            C=((6 - self.C) if self.M else self.C) % 6,
            M=self.M,
        )
