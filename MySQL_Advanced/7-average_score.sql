-- Creates a stored procedure ComputeAverageScoreForUser 
-- that computes and stores the average score for a student.
-- Input: user_id
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score from the corrections table
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE corrections.user_id = user_id;

    -- Update the average_score in the users table for the specific user
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END; //

DELIMITER ;
