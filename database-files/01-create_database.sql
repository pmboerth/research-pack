CREATE DATABASE IF NOT EXISTS researchpack;
USE researchpack;

CREATE TABLE Departments (
    DepartmentId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100)
);

CREATE TABLE Skills (
    SkillId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50)
);

CREATE TABLE Students (
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
    FOREIGN KEY (SkillId) REFERENCES Skills(SkillId) ON DELETE SET NULL,
    FOREIGN KEY (DepartmentId) REFERENCES Departments(DepartmentId) ON DELETE SET NULL
);

CREATE TABLE Professors (
    ProfessorId INT AUTO_INCREMENT PRIMARY KEY,
    Email VARCHAR(100) UNIQUE NOT NULL,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentId INT,
    ResearchArea VARCHAR(100),
    FOREIGN KEY (DepartmentId) REFERENCES Departments(DepartmentId) ON DELETE SET NULL
);

CREATE TABLE Admins (
    AdminId INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentId INT,
    FOREIGN KEY (DepartmentId) REFERENCES Departments(DepartmentId) ON DELETE SET NULL
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
    FOREIGN KEY (OwnerId) REFERENCES Professors(ProfessorId) ON DELETE CASCADE,
    FOREIGN KEY (DepartmentId) REFERENCES Departments(DepartmentId) ON DELETE SET NULL,
    FOREIGN KEY (SkillId) REFERENCES Skills(SkillId) ON DELETE SET NULL
);

CREATE TABLE Applications (
    ApplicationId INT AUTO_INCREMENT PRIMARY KEY,
    ApplicantId INT NOT NULL,
    ApplicationStatus ENUM('Pending', 'Under Review', 'Accepted', 'Rejected', 'Withdrawn'),
    PositionId INT NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ApplicantId) REFERENCES Students(StudentId) ON DELETE CASCADE,
    FOREIGN KEY (PositionId) REFERENCES ResearchOpportunities(PositionId) ON DELETE CASCADE
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
    FOREIGN KEY (CreatorId) REFERENCES Students(StudentId) ON DELETE CASCADE
);

CREATE TABLE Comments (
    PostId INT NOT NULL,
    OwnerId INT NOT NULL,
    CommentId INT AUTO_INCREMENT PRIMARY KEY,
    PostTitle VARCHAR(200),
    PostContent TEXT,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (PostId) REFERENCES Posts(PostId) ON DELETE CASCADE,
    FOREIGN KEY (OwnerId) REFERENCES Students(StudentId) ON DELETE CASCADE
);