-- This SQL script creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all students
-- Procedure ComputeAverageWeightedScoreForUsers  takes no input.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users, 
    (SELECT users.id, SUM(score * weight) / SUM(weight) AS average_score
    FROM users
    JOIN corrections ON users.id = corrections.user_id
    JOIN projects ON corrections.project_id = projects.id
    GROUP BY users.id)
  AS weighted_average
  SET users.average_score = weighted_average.average_score
  WHERE users.id = weighted_average.id;
END;
