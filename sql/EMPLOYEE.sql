DROP TABLE EMPLOYEE;
CREATE TABLE EMPLOYEE
(
    EMP_ID VARCHAR(4),
    F_NAME VARCHAR(20),
    MI VARCHAR(1),
    L_NAME VARCHAR(20),
    GENDER VARCHAR(1),
    SALARY_HOUR DECIMAL(5,2),
    AREA_CODE VARCHAR(3),
    PHONE_NUM VARCHAR(8)
);
ALTER TABLE EMPLOYEE ADD CONSTRAINT PK_EMP_ID PRIMARY KEY(EMP_ID);