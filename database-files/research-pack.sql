CREATE DATABASE researchpack;
USE researchpack;

CREATE TABLE Departments (
    DepartmentId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100)
);

CREATE TABLE Skill (
    SkillId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50)
);

CREATE TABLE Student (
    StudentId INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE NOT NULL,
    SkillId INT,
    DepartmentId INT,
    ResearchInterest VARCHAR(100),
    Year INT,
    Major VARCHAR(50),
    StudentType ENUM('Undergraduate', 'Graduate') NOT NULL,
    FOREIGN KEY (SkillId) REFERENCES Skill(SkillId),
    FOREIGN KEY (DepartmentId) REFERENCES Departments(DepartmentId)
);



CREATE TABLE Professors (
    ProfessorId INT AUTO_INCREMENT PRIMARY KEY,
    Email VARCHAR(100) UNIQUE NOT NULL,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentId INT,
    ResearchArea VARCHAR(100),
    FOREIGN KEY (DepartmentId) REFERENCES Departments(DepartmentId)
);

CREATE TABLE Admins (
    AdminId INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentId INT,
    FOREIGN KEY (DepartmentId) REFERENCES Departments(DepartmentId)
);

CREATE TABLE ResearchOpportunities (
    PositionId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    OwnerId INT NOT NULL,
    ResearchArea VARCHAR(100),
    Description Text,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    DepartmentId INT,
    SkillId INT,
    FOREIGN KEY (OwnerId) REFERENCES Professors(ProfessorId),
    FOREIGN KEY (DepartmentId) REFERENCES Departments(DepartmentId),
    FOREIGN KEY (SkillId) REFERENCES Skill(SkillId)
);

CREATE TABLE Applications (
    ApplicationId INT AUTO_INCREMENT PRIMARY KEY,
    ApplicantId INT NOT NULL,
    ApplicationStatus ENUM('Pending', 'Under Review', 'Accepted', 'Rejected', 'Withdrawn'),
    PositionId INT NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ApplicantId) REFERENCES Student(StudentId),
    FOREIGN KEY (PositionId) REFERENCES ResearchOpportunities(PositionId)
);

CREATE TABLE Posts (
    PostId INT AUTO_INCREMENT PRIMARY KEY,
    CreatorId INT,
    PostTitle VARCHAR(200),
    PostContent TEXT,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PostType ENUM('Question', 'Collaboration'),
    PGroup ENUM('Engineering', 'Computer Science', 'Science', 'Health Science', 'Social Science', 'Business'),
    FOREIGN KEY (CreatorId) REFERENCES Student(StudentId)
);

CREATE TABLE Comments (
    PostId INT NOT NULL,
    OwnerId INT NOT NULL,
    CommentId INT AUTO_INCREMENT PRIMARY KEY,
    PostTitle VARCHAR(200),
    PostContent TEXT,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (PostId) REFERENCES Posts(PostId),
    FOREIGN KEY (OwnerId) REFERENCES Student(StudentId)
);