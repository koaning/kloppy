from typing import List

from kloppy.domain import AttackingDirection, Frame

from .transformers import Transformer

# NOT YET: from .enrichers import TrackingPossessionEnricher


def avg(items: List[float]) -> float:
    if not items:
        return 0
    return sum(items) / len(items)


def attacking_direction_from_frame(frame: Frame) -> AttackingDirection:
    """ This method should only be called for the first frame of a """
    avg_x_home = avg(
        [
            coordinates.x
            for key, coordinates in frame.players_coordinates.items()
            if "home" in key
        ]
    )
    avg_x_away = avg(
        [
            coordinates.x
            for key, coordinates in frame.players_coordinates.items()
            if "away" in key
        ]
    )

    if avg_x_home < avg_x_away:
        return AttackingDirection.HOME_AWAY
    else:
        return AttackingDirection.AWAY_HOME
