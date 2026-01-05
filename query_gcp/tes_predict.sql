SELECT
  *
FROM
  ML.PREDICT(MODEL movies_ds.prediksi_cuan,
    (
    -- INI DATA PURA-PURA (Skenario)
    SELECT
      2000000 AS budget,   -- Skenario: Modal 100 Juta Dollar
      40 AS popularity,      -- Skenario: Viral level 50
      7.0 AS rating          -- Skenario: Rating bagus (8.0)
    )
  );