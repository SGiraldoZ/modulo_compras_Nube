CREATE DATABASE UDemy;

\c UDemy;

CREATE TABLE Purchases (
    user_token VARCHAR NOT NULL,
    course_cms_id VARCHAR NOT NULL,
    price FLOAT,
    purchase_date DATE,
    CONSTRAINT Purchase_pk PRIMARY KEY (user_token, course_cms_id)
);