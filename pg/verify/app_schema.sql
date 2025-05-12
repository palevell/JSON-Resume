-- Verify JSON-Resume:app_schema on pg

BEGIN;

SELECT pg_catalog.has_schema_privilege('resume', 'usage');

ROLLBACK;
