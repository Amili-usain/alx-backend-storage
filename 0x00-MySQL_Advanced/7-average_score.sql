-- This SQL script creates a stored procedure ComputeAverageScoreForUser that
-- computes and store the average score for a studen
-- Procedure ComputeAverageScoreForUser takes 1 input:
--  user_id, a users.id value (assumes user_id is linked to an existing user)

drop procedure IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
	UPDATE users
   	SET average_score=(SELECT AVG(score) FROM corrections
			     WHERE corrections.user_id=user_id)
	WHERE id=user_id;

END;$$
DELIMITER ;
