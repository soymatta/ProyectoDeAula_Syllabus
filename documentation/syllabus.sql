CREATE TABLE `faculties` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL
)

INSERT INTO `faculties` (`id`, `name`) VALUES
(1, 'Ingeniería');

CREATE TABLE `faculties_subjects` (
  `id` int(11) NOT NULL,
  `faculties_id` int(11) NOT NULL,
  `subjects_id` int(11) NOT NULL
)

INSERT INTO `faculties_subjects` (`id`, `faculties_id`, `subjects_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3);

CREATE TABLE `subjects` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `type` enum('practica','teorica','teorico-practica') NOT NULL,
  `credits` int(11) NOT NULL,
  `semester` varchar(2) NOT NULL,
  `bibliography` text DEFAULT NULL,
  `content` text NOT NULL
)

INSERT INTO `subjects` (`id`, `name`, `type`, `credits`, `semester`, `bibliography`, `content`) VALUES
(1, 'Ingeniería del Software I', 'teorica', 2, '1', NULL, ''),
(2, 'Programación Web', 'practica', 2, '2', NULL, ''),
(3, 'Metodos numericos', 'teorico-practica', 4, '3', NULL, '');

CREATE TABLE `syllabi` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `cycle` varchar(500) DEFAULT NULL,
  `identification` text DEFAULT NULL,
  `justification` text DEFAULT NULL,
  `competences` text DEFAULT NULL,
  `learning_results` text DEFAULT NULL,
  `methodology` text DEFAULT NULL,
  `program_content` text DEFAULT NULL,
  `strategies` text DEFAULT NULL,
  `evaluation` text DEFAULT NULL,
  `bibliography` text DEFAULT NULL,
  `five_last_updates` text DEFAULT NULL,
  `subject_id` int(11) NOT NULL,
  `faculty_id` int(11) NOT NULL
)

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `role` enum('admin','teacher') NOT NULL,
  `status` tinyint(1) NOT NULL,
  `faculty_id` int(11) NOT NULL
)

INSERT INTO `users` (`id`, `name`, `email`, `password`, `role`, `status`, `faculty_id`) VALUES
(1, 'Decanatura', 'decanatura-baq@unilibre.edu.co', 'decanatura', 'admin', 1, 1),
(2, 'Rol teacher', 'teacher@unilibre.edu.co', 'teacher', 'teacher', 1, 1);

CREATE TABLE `users_subjects` (
  `id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  `subjects_id` int(11) NOT NULL
)

INSERT INTO `users_subjects` (`id`, `users_id`, `subjects_id`) VALUES
(1, 2, 2),
(2, 2, 3);

CREATE TABLE `versions` (
  `id` int(11) NOT NULL,
  `update_date` datetime NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL,
  `user_id` int(11) NOT NULL
)


ALTER TABLE `faculties`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `faculties_subjects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `faculties_id` (`faculties_id`),
  ADD KEY `subjects_id` (`subjects_id`);

ALTER TABLE `subjects`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `syllabi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `subject_id` (`subject_id`),
  ADD KEY `faculty_id` (`faculty_id`);

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `faculty_id` (`faculty_id`);

ALTER TABLE `users_subjects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_id` (`users_id`),
  ADD KEY `subjects_id` (`subjects_id`);

ALTER TABLE `versions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);


ALTER TABLE `faculties`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `faculties_subjects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

ALTER TABLE `subjects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

ALTER TABLE `syllabi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `users_subjects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `versions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `faculties_subjects`
  ADD CONSTRAINT `faculties_subjects_ibfk_1` FOREIGN KEY (`faculties_id`) REFERENCES `faculties` (`id`),
  ADD CONSTRAINT `faculties_subjects_ibfk_2` FOREIGN KEY (`subjects_id`) REFERENCES `subjects` (`id`);

ALTER TABLE `syllabi`
  ADD CONSTRAINT `syllabi_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`),
  ADD CONSTRAINT `syllabi_ibfk_2` FOREIGN KEY (`faculty_id`) REFERENCES `faculties` (`id`);

ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `faculties` (`id`);

ALTER TABLE `users_subjects`
  ADD CONSTRAINT `users_subjects_ibfk_1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `users_subjects_ibfk_2` FOREIGN KEY (`subjects_id`) REFERENCES `subjects` (`id`);

ALTER TABLE `versions`
  ADD CONSTRAINT `versions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;