"""cj's solutions for https://adventofcode.com/"""

import importlib
import logging
from pathlib import Path
from types import ModuleType
from typing import Literal

PROJECT_ROOT = Path(__file__).parent.parent.parent
LOGS_DIR = PROJECT_ROOT / "logs"
LOGS_DIR.mkdir(exist_ok=True)

Answer = int | str | None
Part = Literal[1, 2]

logging.basicConfig(
    filename=LOGS_DIR / "aoc_cj.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
)


def solve(year: int, day: int, data: str) -> tuple[Answer, Answer]:  # pragma: no cover
    ans_1: Answer = None
    ans_2: Answer = None

    module_name = f"{__name__}.aoc{year}.day{day:02d}"
    try:
        module = importlib.import_module(module_name)

        ans_1 = _solve_part(module, data, 1)
        ans_2 = _solve_part(module, data, 2)
    except ModuleNotFoundError as e:
        raise NotImplementedError(f"module '{module_name}' not found") from e
    except Exception as e:
        logging.exception("exception thrown while solving year=%s day=%s", year, day)
        raise e
    finally:
        logging.info("result for year=%s day=%s: (part_1: %s, part_2: %s)", year, day, ans_1, ans_2)

    return ans_1, ans_2


def _solve_part(module: ModuleType, data: str, part: Part) -> Answer:  # pragma: no cover
    if f := getattr(module, f"part_{part}", None):
        assert callable(f), f"f ({f}) is not callable"
        try:
            # TODO: consider checking that inspect.signature matches expected signature
            resp = f(data)
            assert isinstance(resp, int | str) or resp is None, f"resp ({resp}) must be an int, str, or None"
            return resp
        except NotImplementedError:  # unsolved
            return None
    return None
