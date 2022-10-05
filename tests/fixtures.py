from datetime import datetime

from spielerplus_calendar import appointment


def practice():
    return appointment.Appointment(
        id=12345,
        title="Training",
        start=datetime(2022, 9, 16, 18, 40),
        end=datetime(2022, 9, 16, 20, 30),
        url="/training/view?id=12345",
    )


def appointments():
    return [
        appointment.Appointment(
            id=11131,
            title="Training",
            start=datetime(2022, 9, 30, 18, 55, 00),
            end=datetime(2022, 9, 30, 20, 30, 00),
            url="/training/view?id=11131",
        ),
        appointment.Appointment(
            id=11132,
            title="Gegner A",
            start=datetime(2022, 7, 11, 18, 10, 00),
            end=datetime(2022, 7, 11, 20, 00, 00),
            url="/game/view?id=11132",
        ),
        appointment.Appointment(
            id=11133,
            title="Training + Spiel",
            start=datetime(2022, 4, 24, 11, 55, 00),
            end=datetime(2022, 4, 24, 15, 30, 00),
            url="/event/view?id=11133",
        ),
        appointment.Appointment(
            id=11134,
            title="Turnier",
            start=datetime(2022, 7, 9, 12, 45, 00),
            end=datetime(2022, 7, 9, 23, 59, 59),
            url="/tournament/view?id=11134",
        ),
    ]


def filtered_appointments():
    return [
        appointment.Appointment(
            id=11141,
            title="Training",
            start=datetime(2022, 9, 5, 17, 55, 00),
            end=datetime(2022, 9, 5, 20, 00, 00),
            url="/training/view?id=11141",
        ),
        appointment.Appointment(
            id=11142,
            title="Training+ Fototermin vorher",
            start=datetime(2022, 9, 12, 17, 50, 00),
            end=datetime(2022, 9, 12, 20, 00, 00),
            url="/training/view?id=11142",
        ),
        appointment.Appointment(
            id=11145,
            title="Training",
            start=datetime(2022, 9, 19, 18, 25, 00),
            end=datetime(2022, 9, 19, 20, 00, 00),
            url="/training/view?id=11145",
        ),
        appointment.Appointment(
            id=11146,
            title="Training",
            start=datetime(2022, 9, 2, 17, 55, 00),
            end=datetime(2022, 9, 2, 20, 00, 00),
            url="/training/view?id=11146",
        ),
        appointment.Appointment(
            id=11147,
            title="Training",
            start=datetime(2022, 9, 9, 17, 55, 00),
            end=datetime(2022, 9, 9, 20, 00, 00),
            url="/training/view?id=11147",
        ),
        appointment.Appointment(
            id=11148,
            title="Training",
            start=datetime(2022, 9, 16, 18, 40, 00),
            end=datetime(2022, 9, 16, 20, 30, 00),
            url="/training/view?id=11148",
        ),
        appointment.Appointment(
            id=11149,
            title="Training",
            start=datetime(2022, 9, 23, 18, 55, 00),
            end=datetime(2022, 9, 23, 20, 30, 00),
            url="/training/view?id=11149",
        ),
        appointment.Appointment(
            id=11131,
            title="Training",
            start=datetime(2022, 9, 30, 18, 55, 00),
            end=datetime(2022, 9, 30, 20, 30, 00),
            url="/training/view?id=11131",
        ),
        appointment.Appointment(
            id=11150,
            title="Gegner W",
            start=datetime(2022, 4, 27, 16, 50, 00),
            end=datetime(2022, 4, 27, 18, 30, 00),
            url="/game/view?id=11150",
        ),
        appointment.Appointment(
            id=11132,
            title="Gegner A",
            start=datetime(2022, 7, 11, 18, 10, 00),
            end=datetime(2022, 7, 11, 20, 00, 00),
            url="/game/view?id=11132",
        ),
        appointment.Appointment(
            id=11133,
            title="Training + Spiel",
            start=datetime(2022, 4, 24, 11, 55, 00),
            end=datetime(2022, 4, 24, 15, 30, 00),
            url="/event/view?id=11133",
        ),
        appointment.Appointment(
            id=11151,
            title="Meisterfeier",
            start=datetime(2022, 5, 25, 18, 00, 00),
            end=datetime(2022, 5, 25, 23, 59, 59),
            url="/event/view?id=11151",
        ),
        appointment.Appointment(
            id=11152,
            title="Quali",
            start=datetime(2022, 4, 30, 10, 00, 00),
            end=datetime(2022, 4, 30, 17, 00, 00),
            url="/tournament/view?id=11152",
        ),
        appointment.Appointment(
            id=11134,
            title="Turnier",
            start=datetime(2022, 7, 9, 12, 45, 00),
            end=datetime(2022, 7, 9, 23, 59, 59),
            url="/tournament/view?id=11134",
        ),
    ]
