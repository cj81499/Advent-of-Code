import dataclasses
import re
from collections.abc import Generator

from typing_extensions import Self, override

__all__ = ("Point3D",)


@dataclasses.dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

    PARSE_REGEX = re.compile(r"(\d+)\D+(\d+)\D+(\d+)")

    def __add__(self, other: Self) -> Self:
        cls = self.__class__
        return cls(self.x + other.x, self.y + other.y, self.z + other.z)

    @override
    def __str__(self) -> str:
        return str((self.x, self.y, self.z))

    @staticmethod
    def parse(point3d: str) -> "Point3D":
        m = Point3D.PARSE_REGEX.match(point3d)
        assert m is not None
        x, y, z = map(int, m.groups())
        return Point3D(x, y, z)

    def adj(self) -> Generator["Point3D", None, None]:
        yield Point3D(self.x + 1, self.y, self.z)
        yield Point3D(self.x - 1, self.y, self.z)
        yield Point3D(self.x, self.y + 1, self.z)
        yield Point3D(self.x, self.y - 1, self.z)
        yield Point3D(self.x, self.y, self.z + 1)
        yield Point3D(self.x, self.y, self.z - 1)
