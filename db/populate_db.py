from crud import *
from database_session import get_db
from datetime import datetime

# 1. River
river_data = {
    "river_name": "Rio Meia Ponte",
    "description": "Rio que atravessa Goiânia / GO",
}

# 2. RiverSegment
segment_data = {
    "segment_name": "Região Metropolitana de Goiânia",
    "location_description": "Trecho do Rio Meia Ponte que atravessa a Região Metropolitana de Goiânia, abrangendo áreas urbanas e rurais próximas à capital.",
    "geographic_coordinates": None,
    "critical_threshold_level": None,
}

# 3. StationType
station_type_data = {
    "name": "Fluviométrica",
    "description": "Estações destinadas à medição de variáveis hidrológicas, como nível e vazão dos rios.",
}

# 5. SensorTypes
sensor_types_data = [
    {
        "name": "rain",
        "unit_of_measure": "mm",
        "description": "Sensor para medir a quantidade de precipitação (chuva) em milímetros.",
    },
    {
        "name": "flow",
        "unit_of_measure": "m³/s",
        "description": "Sensor para medir a vazão do rio em metros cúbicos por segundo.",
    },
    {
        "name": "level",
        "unit_of_measure": "m",
        "description": "Sensor para medir o nível da água do rio em metros.",
    },
]

# 4. MonitoringStations
stations_data = [
    {
        "station_name": "MONTANTE DE GOIÂNIA",
        "geographic_location": "POINT(-49.2648 -16.6869)",
        "installation_date": datetime(2010, 1, 1),
        "status": "Active",
        "description": "Zona urbana inicial - Goiânia",
    },
    {
        "station_name": "JUSANTE DE GOIÂNIA",
        "geographic_location": "POINT(-49.2095 -16.7533)",
        "installation_date": datetime(2010, 1, 1),
        "status": "Active",
        "description": "Zona urbana densa - Goiânia",
    },
    {
        "station_name": "UHE SÃO SIMÃO FAZENDA BONITA DE BAIXO",
        "geographic_location": "POINT(-49.2267 -16.9658)",
        "installation_date": datetime(2010, 1, 1),
        "status": "Active",
        "description": "Zona rural - Hidrolândia - alguns kms após a cidade de Goiânia",
    },
]

# Station codes for sensor identifiers
station_codes = ["60640000", "60650000", "60655001"]
sensor_type_names = ["rain", "flow", "level"]


def main():
    with get_db() as db:
        # River
        river = create_river(db, **river_data)
        # RiverSegment
        segment = create_river_segment(
            db,
            id_river=river.id_river,
            segment_name=segment_data["segment_name"],
            location_description=segment_data["location_description"],
            geographic_coordinates=segment_data["geographic_coordinates"],
            critical_threshold_level=segment_data["critical_threshold_level"],
        )
        # StationType
        station_type = create_station_type(db, **station_type_data)
        # SensorTypes
        sensor_types = []
        for stype in sensor_types_data:
            sensor_types.append(create_sensor_type(db, **stype))
        # MonitoringStations
        stations = []
        for i, sdata in enumerate(stations_data):
            station = create_monitoring_station(
                db,
                id_segment=segment.id_segment,
                id_station_type=station_type.id_station_type,
                station_name=sdata["station_name"],
                geographic_location=sdata["geographic_location"],
                installation_date=sdata["installation_date"],
                status=sdata["status"],
            )
            stations.append(station)
        # Sensors
        for i, station in enumerate(stations):
            for j, sensor_type in enumerate(sensor_types):
                sensor_identifier = f"{station_codes[i]}-{sensor_type.name}"
                create_sensor(
                    db,
                    id_station=station.id_station,
                    id_sensor_type=sensor_type.id_sensor_type,
                    sensor_identifier=sensor_identifier,
                    model=None,
                    calibration_date=None,
                    status="Operational",
                )
    print("Database populated successfully.")


if __name__ == "__main__":
    main()
