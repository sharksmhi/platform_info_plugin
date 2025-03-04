import pathlib

import uuid

from . import exceptions


def get_platform_info(
        path_to_credentials: pathlib.Path | str = None,
        # credentials: dict[str, str] = None,
        **kwargs,
        ) -> dict[str, str | int | float]:
    return dict(
        event_id=str(uuid.uuid4()),
        parent_event_id=str(uuid.uuid4()),
        cruise_nr='10',
        latitude='5757.4',   # or lat
        longitude='1212.2',  # or lon
        # position='',
        additional_sampling='BTL, FERRYBOX',  # or add_samp
        series='',
        depth='',
        operator='',
        station='Teststation',
        ship_name='Svea',
        ship_code='77SE',
    )

