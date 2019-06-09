DROP TABLE IF EXISTS CERTIFY;
CREATE TABLE CERTIFY
(
    EMP_ID VARCHAR(4),
    CERT_ID VARCHAR(12),
    OBTAINED_DATE DATE,
    EXPIRE_certifyDATE DATE
);
ALTER TABLE CERTIFY ADD CONSTRAINT PK_CERTIFY PRIMARY KEY(EMP_ID, CERT_ID);
ALTER TABLE CERTIFY ADD CONSTRAINT FK_EMP FOREIGN KEY(EMP_ID) REFERENCES EMPLOYEE(EMP_ID);
ALTER TABLE CERTIFY ADD CONSTRAINT FK_CERT FOREIGN KEY(CERT_ID) REFERENCES CERTIFICATION(CERT_ID);