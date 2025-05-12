-- Verify JSON-Resume:dt_person on pg

BEGIN;

SET search_path TO resume;

SELECT id, name, job_title, email, phone, address
FROM	dt_person
WHERE	FALSE;

ROLLBACK;
