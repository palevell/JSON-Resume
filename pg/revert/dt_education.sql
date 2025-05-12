-- Revert JSON-Resume:dt_education from pg

BEGIN;

SET search_path TO resume, public

-- XXX Add DDLs here.

COMMIT;
