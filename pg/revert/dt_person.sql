-- Revert JSON-Resume:dt_person from pg

BEGIN;

SET search_path TO resume;

DROP TABLE dt_person;

COMMIT;
