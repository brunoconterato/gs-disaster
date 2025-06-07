-- @block (DANGER) Truncate all tables

TRUNCATE TABLE flood_prediction CASCADE;
TRUNCATE TABLE ml_model_metric CASCADE;
TRUNCATE TABLE ml_model CASCADE;
TRUNCATE TABLE sensor_measurement CASCADE;
TRUNCATE TABLE sensor CASCADE;
TRUNCATE TABLE monitoring_station CASCADE;
TRUNCATE TABLE river_segment CASCADE;
TRUNCATE TABLE river CASCADE;
TRUNCATE TABLE station_type CASCADE;
TRUNCATE TABLE sensor_type CASCADE;
TRUNCATE TABLE alert CASCADE;

-- @block
SELECT * FROM river;

-- @block
SELECT * FROM river_segment;

-- @block
SELECT * FROM station_type;

-- @block
SELECT * FROM monitoring_station;

-- @block
SELECT * FROM sensor_type;

-- @block
SELECT * FROM sensor;

-- @block
SELECT * FROM sensor_measurement LIMIT 10;

-- @block
SELECT * FROM ml_model;

-- @block
SELECT * FROM ml_model_metric;

-- @block
SELECT * FROM flood_prediction;

-- @block
SELECT * FROM resampled_measurements_daily;

-- @block
SELECT * FROM alert;
