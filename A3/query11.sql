-- Retrieve the name and count of the Badge awarded
-- the second-most number of times
-- 1.1 marks: <10 operators
-- 1.0 marks: <12 operators
-- 0.9 marks: <15 operators
-- 0.8 marks: correct answer
-- REFERENCE USED: https://stackoverflow.com/questions/18280138/select-rows-with-the-second-highest-value-in-a-column?noredirect=1&lq=1

SELECT Name, COUNT(*) as Frequency FROM Badge GROUP BY Name ORDER BY Frequency DESC LIMIT 1,1;
