CREATE OR REPLACE MODEL movies_ds.prediksi_cuan
OPTIONS(model_type='linear_reg') AS
SELECT
  revenue AS label,
  budget,
  popularity,
  rating
FROM
  movies_ds.movies_clean
WHERE
  revenue > 0;