SELECT
  title,
  budget,
  revenue,
  roi,
  genre
FROM
  ipsd-480109.movies_ds.movies_clean
ORDER BY
  roi DESC
LIMIT 5;