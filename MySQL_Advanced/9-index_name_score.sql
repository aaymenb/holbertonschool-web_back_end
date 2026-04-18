-- Creates a composite index idx_name_first_score on the table names
-- Indexing the first letter of 'name' and the 'score' column.
CREATE INDEX idx_name_first_score ON names (name(1), score);
