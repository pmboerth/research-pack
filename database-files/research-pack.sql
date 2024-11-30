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

-- Insert Skills
INSERT INTO Skill (SkillId, Name) VALUES
(1, 'Python Programming'),
(2, 'Data Analysis'),
(3, 'Machine Learning');

-- Insert Departments
INSERT INTO Departments (DepartmentId, Name) VALUES
(1, 'Computer Science'),
(2, 'Electrical Engineering'),
(3, 'Bioengineering');

-- Insert Students
INSERT INTO Student (StudentId, FirstName, LastName, Email, SkillId, DepartmentId, ResearchInterest, Year, Major, StudentType) VALUES
(1, 'Alice', 'Johnson', 'alice.j@university.edu', 1, 1, 'Artificial Intelligence', 3, 'Computer Science', 'undergraduate'),
(2, 'Bob', 'Smith', 'bob.s@university.edu', 2, 2, 'Signal Processing', 2, 'Electrical Engineering', 'undergraduate'),
(3, 'Carol', 'Davis', 'carol.d@university.edu', 3, 1, 'Machine Learning', 1, 'Computer Science', 'graduate');

-- Insert Professors
INSERT INTO Professors (ProfessorId, Email, FirstName, LastName, DepartmentId, ResearchArea) VALUES
(1, 'john.doe@university.edu', 'John', 'Doe', 1, 'Artificial Intelligence'),
(2, 'mary.smith@university.edu', 'Mary', 'Smith', 2, 'Signal Processing'),
(3, 'james.wilson@university.edu', 'James', 'Wilson', 3, 'Biomedical Imaging');

-- Insert Admins
INSERT INTO Admins (AdminId, FirstName, LastName, DepartmentId) VALUES
(1, 'Admin', 'Jones', 1),
(2, 'Admin', 'Brown', 2),
(3, 'Admin', 'Wilson', 3);

-- Insert Research Opportunities
INSERT INTO ResearchOpportunities (PositionId, Name, OwnerId, ResearchArea, Description, DepartmentId, SkillId) VALUES
(1, 'AI Research Assistant', 1, 'Machine Learning', 'DESCRIPTION', 1, 1),
(2, 'Signal Processing Lab Assistant', 2, 'Digital Signal Processing', 'DESCRIPTION', 2, 2),
(3, 'Bioinformatics Research', 3, 'Computational Biology', 'DESCRIPTION', 3, 3);

-- Insert Applications
INSERT INTO Applications (ApplicationId, ApplicantId, ApplicationStatus, PositionId) VALUES
(1, 1, 'Pending', 1),
(2, 2, 'Under Review', 2),
(3, 3, 'Accepted', 3);

-- Insert Posts
INSERT INTO Posts (PostId, CreatorId, PostTitle, PostContent, PostType, PGroup) VALUES
(1, 1, 'Looking for AI Study Group', 'Anyone interested in forming an AI study group?', 'Question', 'Computer Science'),
(2, 2, 'Signal Processing Workshop', 'Workshop next week on DSP fundamentals', 'Collaboration', 'Engineering'),
(3, 3, 'Research Paper Discussion', 'Lets discuss recent ML papers', 'Collaboration', 'Computer Science');

-- Insert Comments
INSERT INTO Comments (CommentId, PostId, OwnerId, PostTitle, PostContent) VALUES
(1, 1, 2, 'RE: AI Study Group', 'Im interested! When are you planning to meet?'),
(2, 2, 1, 'RE: Workshop', 'Will the workshop be recorded?'),
(3, 3, 3, 'RE: Paper Discussion', 'Great idea! I suggest starting with the latest transformers paper.');