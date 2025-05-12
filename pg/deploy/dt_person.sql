-- Deploy JSON-Resume:dt_person to pg
-- requires: app_schema

BEGIN;

SET search_path TO resume;

CREATE TABLE dt_person (
	id		INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY (START WITH 1000001),
	name		VARCHAR(100) NOT NULL,
	job_title	VARCHAR(100) NOT NULL,
	email		VARCHAR(254) NOT NULL,
	phone		VARCHAR(20) NOT NULL,
	address		TEXT NOT NULL
);

COMMIT;
