DROP TABLE IF EXISTS WORK_SCHEDULE;
CREATE TABLE WORK_SCHEDULE
(
    EMP_ID VARCHAR(4),
    DATES DATE,
    START_TIME TIMESTAMP, 
    END_TIME TIMESTAMP, 
    WORK_HOURS DECIMAL(5,2)
);
ALTER TABLE WORK_SCHEDULE ADD CONSTRAINT PK_WORK_SCHEDULE PRIMARY KEY(EMP_ID, DATES);
ALTER TABLE WORK_SCHEDULE ADD CONSTRAINT FK_EMPLOYEE FOREIGN KEY(EMP_ID) REFERENCES EMPLOYEE(EMP_ID);