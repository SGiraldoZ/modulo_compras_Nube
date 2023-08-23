CREATE DATABASE UDemy;

USE UDemy;

CREATE TABLE Users (
    u_id SERIAL NOT NULL UNIQUE,
    token VARCHAR,
    username VARCHAR,
    CONSTRAINT user_pk PRIMARY KEY (u_id)
);

CREATE TABLE Courses (
    course_id SERIAL NOT NULL UNIQUE,
    cms_id VARCHAR NOT NULL UNIQUE,
    course_name VARCHAR,
    CONSTRAINT course_pk PRIMARY KEY (course_id)
);

CREATE TABLE Purchases (
    u_id INT NOT NULL UNIQUE,
    course_id INT NOT NULL UNIQUE,
    CONSTRAINT Purchase_pk PRIMARY KEY (u_id, course_id),
    CONSTRAINT purchase_user_fk FOREIGN KEY (u_id) REFERENCES Users (u_id),
    CONSTRAINT purchase_course_fk FOREIGN KEY (course_id) REFERENCES Courses (course_id)
);