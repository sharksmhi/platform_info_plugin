import pathlib

from . import exceptions


def get_platform_info(**kwargs) -> dict:
    return dict(
        platform_name='Platformen',
    )


def get_current_data(
        path_to_credentials: pathlib.Path | str = None,
        # credentials: dict[str, str] = None,
        **kwargs,
        ) -> dict[str, str | int | float]:
    return dict(
        # event_id=str(uuid.uuid4()),
        # parent_event_id=str(uuid.uuid4()),
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
        air_pres='',
        air_temp='',
        wind_spd='',
        wind_dir='',
    )

