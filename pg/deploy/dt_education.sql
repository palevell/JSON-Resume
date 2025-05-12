-- Deploy JSON-Resume:dt_education to pg
-- requires: app_schema
-- requires: dt_person

BEGIN;

SET search_path TO resume, public

-- XXX Add DDLs here.

COMMIT;
