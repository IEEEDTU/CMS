BEGIN TRANSACTION;
CREATE TABLE "NewsFeed_notice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "subject" varchar(250) NOT NULL, "issuingAuthority" varchar(250) NOT NULL, "issueDate" datetime NOT NULL, "branch_id" varchar(10) NULL REFERENCES "Course_branch" ("branchCode"), "degree_id" integer NULL REFERENCES "Course_degree" ("id"), "department_id" varchar(5) NULL REFERENCES "Course_department" ("deptId"), "fileLink" varchar(200) NOT NULL);
INSERT INTO `NewsFeed_notice` (id,subject,issuingAuthority,issueDate,branch_id,degree_id,department_id,fileLink) VALUES (1,'Examination postponed','Academic Department','2016-04-10 11:59:29.230627',NULL,1,'ACDM','www.dropbox.com/xjtfd76ypb'),
 (2,'Final List of students having short attendance less than 75 %','Academic Department','13.05.2016',NULL,1,'ACDM','http://dtu.ac.in/Web/Academics/notice/2016/may/file507.pdf'),
 (3,'Guidelines for preparation of list of detainees (shortage of attendance 
 less than 75 %) of B.Tech students','Academic Department',' 09.05.2016',NULL,1,'ACDM','http://dtu.ac.in/Web/Academics/notice/2016/may/file505.pdf'),
 (4,'Cancellation of registration and admission of students admitted in 
 academic session 2015 in B.Tech. Program at DTU','Academic Department',' 05.05.2016','',1,'ACDM','http://dtu.ac.in/Web/Academics/notice/2016/may/file501.pdf'),
 (5,'Make-up examination for mid-term even sem 2016','Academic Department',' 05.05.2016',NULL,1,'ACDM','http://dtu.ac.in/Web/Academics/notice/2016/may/file503.pdf'),
 (6,'Guideline for preparation of list of detainees ( shortage of attendance
 less than 75% ) of B.Tech students','Academic Department','22.04.2016',NULL,1,'ACDM','http://dtu.ac.in/Web/Academics/notice/2016/april/file403.pdf'),
 (7,'Circular regarding the submission of M.Tech major project reports','Academic Department','05.04.2016',NULL,1,'ACDM','http://dtu.ac.in/Web/Academics/notice/PG/file109.pdf');
CREATE TABLE "NewsFeed_news" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "headline" varchar(250) NOT NULL, "description" varchar(4000) NOT NULL, "image" varchar(200) NULL, "link" varchar(200) NULL, "date" date NOT NULL, "publishedBy_id" integer NOT NULL REFERENCES "Profiler_name" ("id"));
INSERT INTO `NewsFeed_news` (id,headline,description,image,link,date,publishedBy_id) VALUES
(1,'DTU launched Deferred Placement Policy','Deferred placement policy launched for the students having interest in entrepreneurship','www.dropbox.com/t78phh','www.dtu.ac.in','2016-04-20','DTU/2K12/B08/1200'),
 (2,'DTU takes initiative to
support Start-ups - UDAAN','DCE-DTU Alumni Association',NULL,NULL,'',0),
 (3,'DCE-DTU Alumni Meet','DCE-DTU alumni meet was conducted on 30th January,
2016 at Air Force Auditorium, Subroto Park.
The chief guest of the event was Mr Manish Sisodia,
Deputy Chief Minister of Delhi. The event started
with a musical program by Suresh Raheja. Distinguished
alumni, students and teachers were awarded,
followed by a speech by the President of the association.
It was a huge gathering of more than a thousand
people which included the silver and golden jubilee
members of DCE. The event was funded by two people
from the golden jubilee and by over a hundred
people from silver jubilee.',NULL,NULL,'',0),
 (4,'DTU celebrates Republic
Day','To celebrate the spirit of patriotism, Republic Day',NULL,NULL,'',0);
CREATE TABLE "NewsFeed_event" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "eventName" varchar(250) NOT NULL, "startDateTime" datetime NOT NULL, "endDateTime" datetime NULL, "description" varchar(4000) NOT NULL, "organisedBy" varchar(250) NOT NULL, "email" varchar(254) NOT NULL, "fbEvent" varchar(200) NULL, "website" varchar(200) NULL, "image" varchar(200) NULL, "mobile_id" integer NOT NULL REFERENCES "Profiler_mobile" ("id"), "venue" varchar(500) NOT NULL);
INSERT INTO `NewsFeed_event` (id,eventName,startDateTime,endDateTime,description,organisedBy,email,fbEvent,website,image,mobile_id,venue) VALUES (1,'ICICI Trinity Orientation','2016-04-29 10:30:00.000000','2016-04-29 12:30:00.000000','Trinity is an initiative by ICICI Bank that promotes innovation and entrepreneurship amongst the youth community in India. If you have an idea related to service sector and Fintech domain, or an idea that you believe can make an impact to a larger enterprise, we have the platform for you. Trinity is about celebrating the spirit of innovation. It is a programme, where you can walk in with an idea and walk out as an impactful entrepreneur.

We at ICICI Bank understand the value of an idea and have designed a programme that rewards an idea at every stage. The ICICI Trinity programme comprises of 3 stages – Ideate, Prototype and Be an Entrepreneur. This programme seeks to identify ideas, evaluate, groom, nurture and help turn them into successful business ventures. Apart from funding, the programme provides an opportunity for a participant to meet, interact and learn from industry veterans, thereby making it a rewarding and enriching experience.','SSEDTU','contact.ssedtu@gmail.com','www.facebook.com/icicitrinityorientation2016','www.ssedtu.com','www.dropbox.com/786youg',1,'Senate Hall, Admin Block'),
 (2,'Fortitude, The DTU Quiz Fest','2016-02-29','2016-02-02','Delhi-42: The DTU Quiz Club presents Fortitude, the inaugural edition of the annual quizzing festival of DTU. It will be a three day extravaganza with six main quizzes and three filler quizzes, with on the spot cash prizes for every quiz.

Basic rules:-
1. All quizzes open only to students.
2. Team size of 1-3 member(s) per team. 
3. Cross institution teams are allowed.
4. On the spot cash prizes worth ₹90,000/-
5. Exciting audience prizes as well. Chocolates/Pulse candy at the very least.

Day-1, February 29
0930 - Fahrenheit 42, the FLAME Quiz
1230 - Anime and Manga Filler
1400 - Shree42, The HindEnt Quiz

Day-2, March 1
0930 - 101010 : The Tech Quiz
1230 - Video Games Filler
1400 - Monopoly : The Business Quiz

Day-3, March 2
0930 - Mrs. Shakuntala and Mr. Trilok Chand Memorial India Quiz
1230 - War Filler
1400 - Pana Po''o, The General Quiz','','contact.ssedtu@gmail.com',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (3,'HackEnvision 2016','2016-02-19','2016-02-20','In the context of a hackathon, the word "hack" is used to describe how multiple technologies can be used together in a new and innovative way. Teams of up to four people spend the weekend working on innovative software solutions to real-world problems. These projects range in platform and application, including elements of web development, mobile applications, and more. However, many times the most important aspect of a hackathon is the community it generates and skills that inexperienced hackers walk away with.

Envision is built upon the idea that everyone should be able to participate, from individuals who have never written a line of code to experts who have been developing for years. To help facilitate the learning experience, we''ve compiled a number of resources to help during the weekend. In addition, we''ll be offering a series of tech talks throughout the event.','','contact.ssedtu@gmail.com',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (4,'
Troika 2016','2016-02-19','2016-02-21','IEEE DTU, one of the most active student branch of IEEE proudly presents its annual technical fest Troika 2016.

Troika, which is Russian for "a set of three", represents the three pillars of engineering: Approach, Theory and Practice.

With an array of competitive events covering all aspects of technical aptitude, Troika is one of the most eagerly awaited Techfests of North India and attracts participation from all over the country. Continuing the rich legacy, Troika 2016 aspires to be an exhibition of, and a platform for young engineering talent.','','contact.@ieeedtu.com',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (5,'COGENESIS ''16','2016-02-19','2016-02-21','Cogenesis is the Annual Technical Festival of CSE Dept, DTU hosted by CSI-DTU, SSE-DTU and SITE-DTU.','','contact.ssedtu@gmail.com',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (6,'
DTU Programming Mania Contest 2!','2015-07-03','2015-07-04','IEEE DTU, in association with IEEE Computer Society and Codechef DTU Chapter, present DTU Programming Mania! Codechef Goodies to be won.','','contact.@ieeedtu.com',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (7,'
Programming Interviews Bootcamp','2015-04-11','2015-04-19','A four day workshop with the aim of preparing students to do well in their programming interviews.

We will be teaching the most important concepts, discussing the most important questions and sharing other tips.

We will get you experiences from your seniors who have done it right.

Contact: 
Nimish Aggarwal (placed at Goldman Sachs): +919650908927
Gitanshu Behal (placed at Snapdeal): +918130678611
Abhinav Agarwal (placed at Amazon): +919013353477

The bootcamp will be held on 11, 12, 18 and 19 April, from 9:00 AM to 5:00 PM, each day.','','contact.ssedtu@gmail.com',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (8,'
Startup Internship Fair','2015-02-11',NULL,'E-cell DTU presents Startup Internship Fair, powered by iSpirt and in association with SwiftIntern.com. ','','contact.@ieeedtu.com',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (9,'
E-Summit''15','2015-02-14','2015-02-15','The Entrepreneurship Summit from 14th to 15th February is a confluence of visionary students, professionals or anyone who wishes to make a mark in the the world, start ','','contact.@ieeedtu.com',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (10,'
INNOVA-2015 UNLEASH YOURSELF.','2015-02-13','2015-02-14','Innova-DTU is the biggest techno-management fest of DTU. This year we host the 21st edition of the annual fest from 13-15th of Februrary.','','contact.@ieeedtu.com',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (11,'
Cadcraft','2015-02-13',NULL,'It''s all about creating designs using computerized drafting techniques based on a given problem statement. This event aims at testing the imagination and spontaneity of the students using mind-boggling queries and their equally innovative results.','','contact.@ieeedtu.com',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (12,'Web and Software Development Workshop','2015-01-24',NULL,'This workshop will help you learn the basics of web and software development and give you a head start in the field of Development.','','',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (13,'
mini-Envision','2015-02-05',NULL,'Two hours software development sprint. Create a website/app on given themes and take the advantage in main event, ENVISION!!','','',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (14,'
Bytes','2015-02-08',NULL,'Troika 2015 brings to you Bytes, our online coding contest. If you’re active on CodeChef, HackerRank and SPOJ more than Facebook and Twitter, Bytes is the event that you’ve been waiting for.','','',NULL,NULL,NULL,1,'Senate Hall, Admin Block'),
 (15,'
Mind Mumble','2015-02-13',NULL,'MIND MUMBLE :','','',NULL,NULL,NULL,1,'Senate Hall, Admin Block');
CREATE INDEX "django_session_de54fa62" ON "django_session" ("expire_date");
CREATE UNIQUE INDEX "django_content_type_app_label_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE INDEX "django_admin_log_e8701ad4" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_417f1b1c" ON "django_admin_log" ("content_type_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_e8701ad4" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_8373b171" ON "auth_user_user_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_e8701ad4" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_0e939a4f" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_permission_content_type_id_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_417f1b1c" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "auth_group_permissions_group_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_8373b171" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_group_permissions_0e939a4f" ON "auth_group_permissions" ("group_id");
CREATE INDEX "Resource_resource_ea134da7" ON "Resource_resource" ("course_id");
CREATE INDEX "Resource_resource_10d4336a" ON "Resource_resource" ("updatedBy_id");
CREATE INDEX "Profiler_studentskill_d38d4c39" ON "Profiler_studentskill" ("skill_id");
CREATE INDEX "Profiler_studentskill_30a811f6" ON "Profiler_studentskill" ("student_id");
CREATE INDEX "Profiler_studentfield_3aabf39f" ON "Profiler_studentfield" ("field_id");
CREATE INDEX "Profiler_studentfield_30a811f6" ON "Profiler_studentfield" ("student_id");
CREATE INDEX "Profiler_student_d15634c0" ON "Profiler_student" ("guardianAdd_id");
CREATE INDEX "Profiler_student_c90dfaec" ON "Profiler_student" ("personalMobile_id");
CREATE INDEX "Profiler_student_a5343a4c" ON "Profiler_student" ("alternativeMobile_id");
CREATE INDEX "Profiler_student_9df25263" ON "Profiler_student" ("presentAdd_id");
CREATE INDEX "Profiler_student_707df528" ON "Profiler_student" ("fatherName_id");
CREATE INDEX "Profiler_student_6ee97270" ON "Profiler_student" ("permanentAdd_id");
CREATE INDEX "Profiler_student_653cda86" ON "Profiler_student" ("motherName_id");
CREATE INDEX "Profiler_student_3db78b68" ON "Profiler_student" ("name_id");
CREATE INDEX "Profiler_student_0e798d2a" ON "Profiler_student" ("degree_id");
CREATE INDEX "Profiler_student_09fd5b13" ON "Profiler_student" ("branch_id");
CREATE INDEX "Profiler_skill_4ea47e6d" ON "Profiler_skill" ("skillName");
CREATE INDEX "Profiler_project_30a811f6" ON "Profiler_project" ("student_id");
CREATE INDEX "Profiler_field_972bf3f0" ON "Profiler_field" ("fieldName");
CREATE INDEX "Profiler_facultyfield_5bb92a88" ON "Profiler_facultyfield" ("faculty_id");
CREATE INDEX "Profiler_facultyfield_3aabf39f" ON "Profiler_facultyfield" ("field_id");
CREATE INDEX "Profiler_faculty_d15634c0" ON "Profiler_faculty" ("guardianAdd_id");
CREATE INDEX "Profiler_faculty_c90dfaec" ON "Profiler_faculty" ("personalMobile_id");
CREATE INDEX "Profiler_faculty_bf691be4" ON "Profiler_faculty" ("department_id");
CREATE INDEX "Profiler_faculty_a5343a4c" ON "Profiler_faculty" ("alternativeMobile_id");
CREATE INDEX "Profiler_faculty_9df25263" ON "Profiler_faculty" ("presentAdd_id");
CREATE INDEX "Profiler_faculty_707df528" ON "Profiler_faculty" ("fatherName_id");
CREATE INDEX "Profiler_faculty_6ee97270" ON "Profiler_faculty" ("permanentAdd_id");
CREATE INDEX "Profiler_faculty_653cda86" ON "Profiler_faculty" ("motherName_id");
CREATE INDEX "Profiler_faculty_3db78b68" ON "Profiler_faculty" ("name_id");
CREATE INDEX "NewsFeed_notice_bf691be4" ON "NewsFeed_notice" ("department_id");
CREATE INDEX "NewsFeed_notice_0e798d2a" ON "NewsFeed_notice" ("degree_id");
CREATE INDEX "NewsFeed_notice_09fd5b13" ON "NewsFeed_notice" ("branch_id");
CREATE INDEX "NewsFeed_news_24b425c9" ON "NewsFeed_news" ("publishedBy_id");
CREATE INDEX "NewsFeed_event_673596b3" ON "NewsFeed_event" ("mobile_id");
CREATE INDEX "NewsFeed_announcement_dfef1f0f" ON "NewsFeed_announcement" ("courseGroup_id");
CREATE INDEX "Course_laboratory_b5a9fd30" ON "Course_laboratory" ("dept_id");
CREATE INDEX "Course_group_09fd5b13" ON "Course_group" ("branch_id");
CREATE INDEX "Course_department_c292c8fa" ON "Course_department" ("hod_id");
CREATE INDEX "Course_coursegroup_ea134da7" ON "Course_coursegroup" ("course_id");
CREATE INDEX "Course_coursegroup_0e939a4f" ON "Course_coursegroup" ("group_id");
CREATE INDEX "Course_coursegroup_06aab9f3" ON "Course_coursegroup" ("instructor_id");
CREATE INDEX "Course_coursecurriculum_ea134da7" ON "Course_coursecurriculum" ("course_id");
CREATE INDEX "Course_course_0e798d2a" ON "Course_course" ("degree_id");
CREATE INDEX "Course_course_09fd5b13" ON "Course_course" ("branch_id");
CREATE INDEX "Course_branch_bf691be4" ON "Course_branch" ("department_id");
CREATE INDEX "Course_branch_0e798d2a" ON "Course_branch" ("degree_id");
CREATE INDEX "Course_batch_bf691be4" ON "Course_batch" ("department_id");
CREATE INDEX "Course_batch_0e798d2a" ON "Course_batch" ("degree_id");
CREATE INDEX "Assessment_score_ea134da7" ON "Assessment_score" ("course_id");
CREATE INDEX "Assessment_score_30a811f6" ON "Assessment_score" ("student_id");
CREATE INDEX "Assessment_result_30a811f6" ON "Assessment_result" ("student_id");
CREATE INDEX "Assessment_assignmentresponse_93c4899b" ON "Assessment_assignmentresponse" ("assignment_id");
CREATE INDEX "Assessment_assignmentresponse_30a811f6" ON "Assessment_assignmentresponse" ("student_id");
CREATE INDEX "Assessment_assignment_ea134da7" ON "Assessment_assignment" ("course_id");
COMMIT;
