SELECT
  title,
  budget,
  revenue,
  genre
FROM
  ipsd-480109.movies_ds.movies_clean
WHERE
  budget > 0 AND revenue > 0
LIMIT 200;