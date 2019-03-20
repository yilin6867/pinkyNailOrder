DROP TABLE SERVICE;
CREATE TABLE SERVICE
(
    ID INT,
    NAME VARCHAR(40),
    TYPE VARCHAR(15),
    PRICE DECIMAL(5,2)
);
ALTER TABLE "SERVICE" ADD CONSTRAINT PK_SERVICE PRIMARY KEY(ID);