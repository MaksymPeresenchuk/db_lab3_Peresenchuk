DO $$
  DECLARE
    countries_id countries.country_id%TYPE;
    countries_name countries.country_name%TYPE;
    
  BEGIN
    countries_id := 'C';
    countries_name := 'country';
    FOR counter IN 1..5
      LOOP
        INSERT INTO countries (country_id, country_name)
        VALUES (countries_id || counter + 4, countries_name || counter + 4);
      END LOOP;
  END;
$$

SELECT * FROM countries