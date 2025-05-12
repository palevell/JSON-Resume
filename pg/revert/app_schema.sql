-- Revert JSON-Resume:app_schema from pg

BEGIN;

DROP SCHEMA resume;

COMMIT;
