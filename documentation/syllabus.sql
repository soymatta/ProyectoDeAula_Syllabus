INSERT INTO `subjects` (`id`, `name`, `modality`, `type`, `credits`, `semester`, `bibliography`) VALUES
(1, 'Ingeniería del Software I', 'presencial', 'teorico-practica', 4, '1', NULL),
(2, 'Ingeniería del Software II', 'presencial', 'teorico-practica', 4, '2', NULL),
(3, 'Calculo I', 'presencial', 'teorico-practica', 4, '1', NULL),
(4, 'Internet de las cosas', 'virtual', 'teorica', 2, '2', NULL);

INSERT INTO `faculties` (`id`, `name`) VALUES
(1, 'Ingeniería');

INSERT INTO `formats` (`id`, `code`, `version`, `update_date`) VALUES
(1, 'ST-DOC-01-E-01-F01 ', 1, '2021-07-26 00:00:00'),
(2, 'ST-DOC-01-E-01-F01 ', 2, '2023-07-04 00:00:00');

INSERT INTO `programs` (`id`, `name`, `faculty_id`) VALUES
(1, 'Ingeniería de sistemas', 1),
(2, 'Ingeniería industrial', 1);

INSERT INTO `syllabi` (`id`, `cycle`, `component`, `justification`, `competences`, `learning_results`, `methodology`, `subject_id`, `faculty_id`, `format_id`, `program_id`) VALUES
(1, 'PROFESIONAL', 'PROFESIONAL', 'Después de revisar y aplicar los conceptos previos de las fases de Ingeniería de Software (Análisis \r\ny Diseño de Sistemas), es indispensable para el estudiante comprender y desarrollar mecanismos \r\npara construir e implementar la aplicación que permitirá solucionar los problemas identificados \r\nen  la  fase  de  análisis  y  convertir  las  estructuras  definidas  en  la  fase  de  diseño  en  una  solución \r\npráctica, probada y documentada lista para ser usada por los usuarios.', 'Competencias básicas: Comunicar asertivamente las diferentes propuestas para dar solución a \r\nlas necesidades organizacionales que enfrenta el ingeniero de sistemas.', 'RA_4: \r\nComunica efectivamente en forma oral, gráfica y por escrito usando un lenguaje técnico.', 'TRABAJO PRESENCIAL \r\nLos conocimientos de la asignatura se adquieren a través del estudio razonado de todas las \r\nunidades didácticas de la asignatura, previa presentación del docente, ejemplos y ejercicios \r\nen clases, así como del material didáctico que se ponga a disposición de los estudiantes en \r\nla plataforma Moodle. \r\nTRABAJO INDEPENDIENTE \r\nLos estudiantes tendrán talleres y trabajos prácticos e investigativos sobre los temas vistos \r\nen clases que puedan realizar durante las horas independientes asignadas para la materia.', 2, 1, 2, 1),
(2, 'PROFESIONAL', 'PROFESIONAL', 'La Ingeniería del Software I sienta las bases fundamentales para que los estudiantes comprendan los principios, técnicas y herramientas esenciales en el desarrollo de software. Este curso es crucial para que los futuros ingenieros de software adquieran una comprensión sólida de los conceptos básicos necesarios en el ciclo de vida del desarrollo de software.', 'Competencias básicas: Aplicar metodologías de desarrollo de software para analizar, diseñar e implementar sistemas de información efectivos y eficientes.', 'RA_2: Diseña soluciones de software que satisfacen los requisitos especificados.', 'TRABAJO PRESENCIAL Los estudiantes participarán en clases teóricas, discusiones y ejercicios prácticos para comprender los conceptos fundamentales. TRABAJO INDEPENDIENTE Los estudiantes realizarán proyectos prácticos, ejercicios de codificación y estudios de caso para aplicar los conocimientos adquiridos en clase.', 1, 1, 2, 1),
(3, 'PROFESIONAL', 'PROFESIONAL', 'El curso de Internet de las Cosas (IoT) proporciona a los estudiantes la comprensión necesaria de los principios y aplicaciones de la conexión de dispositivos en red. Con un enfoque práctico, este curso permite a los estudiantes diseñar y desarrollar soluciones para el mundo interconectado de IoT.', 'Competencias básicas: Diseñar e implementar soluciones de IoT para resolver problemas del mundo real.', 'RA_5: Implementa soluciones de Internet de las Cosas que abordan desafíos específicos.', 'TRABAJO PRESENCIAL Las clases incluirán teoría sobre arquitecturas de IoT, ejemplos prácticos y discusiones sobre casos de uso. TRABAJO INDEPENDIENTE Los estudiantes desarrollarán proyectos prácticos de IoT, realizarán experimentos y estudiarán casos de éxito en el campo de IoT.', 4, 1, 2, 1),
(4, 'BÁSICO', 'PROFESIONAL', 'El curso de Cálculo es esencial para que los estudiantes adquieran las habilidades matemáticas fundamentales necesarias en diversas disciplinas. Proporciona las bases para entender conceptos avanzados en matemáticas y aplicarlos en problemas del mundo real.', 'Competencias básicas: Aplicar conceptos matemáticos para resolver problemas en contextos diversos.', 'RA_1: Aplica conceptos de cálculo para resolver problemas matemáticos y aplicaciones prácticas.', 'TRABAJO PRESENCIAL Las clases incluirán explicaciones teóricas, resolución de problemas y discusiones interactivas. TRABAJO INDEPENDIENTE Los estudiantes resolverán problemas adicionales, realizarán ejercicios prácticos y participarán en sesiones de tutoría para reforzar los conceptos aprendidos.', 3, 1, 1, 1);

INSERT INTO `users` (`id`, `name`, `email`, `password`, `role`, `status`, `faculty_id`) VALUES
(1, 'Decano', 'decanatura-baq@unilibre.edu.co', 'decanatura', 'admin', 1, 1),
(2, 'Juan Martinez', 'teacher1@unilibre.edu.co', 'teacher', 'teacher', 1, 1),
(3, 'Alba Romero', 'teacher2@unilibre.edu.co', 'teacher', 'teacher', 1, 1);


INSERT INTO `versions` (`id`, `update_date`, `description`, `user_id`, `syllabus_id`) VALUES
(1, '2023-11-24 01:51:24', 'Cambio 1', 3, 4),
(2, '2023-11-01 19:53:18', 'Cambio 2', 2, 4),
(3, '2023-11-24 01:51:24', 'Cambio 1', 2, 3);

INSERT INTO `contents_and_strategies` (`id`, `content_name`, `sub_content`, `strategies`, `syllabus_id`) VALUES
(5, 'Introducción a la Ingeniería de Software', 'Definición y evolución.\r\nPrincipios y conceptos fundamentales.\r\nImportancia y aplicaciones.', 'Clases Teóricas y Prácticas:\r\n\r\nConferencias magistrales para la presentación de conceptos teóricos.\r\nDesarrollo práctico de proyectos en clase para aplicar los conocimientos adquiridos.', 2),
(6, 'Conceptos Básicos de Cálculo', 'Funciones y límites.\r\nContinuidad y derivadas.\r\nAplicaciones de la derivada.', 'Clases Teóricas y Ejercicios Prácticos:\r\n\r\nLecciones teóricas con ejemplos prácticos.\r\nResolución de problemas en clase.', 4),
(7, 'Introducción a IoT', 'Definición y evolución.\r\nPrincipios y tecnologías clave.\r\nAplicaciones en la vida cotidiana e industrial.', 'Proyectos Prácticos:\r\n\r\nDesarrollo de proyectos IoT desde cero.\r\nIntegración de sensores, actuadores y plataformas de desarrollo.', 3),
(8, 'Ingeniería de Sistemas ', 'Jerarquía de la Ingeniería de Software \r\nIngeniería de procesos de negocios \r\nIngeniería del producto \r\nModelado del Sistema', 'Ejercicios en clase\r\nQuices,  \r\nTrabajo independiente del estudiante,  \r\nParticipación del estudiante,  \r\nExamen individual \r\nExposiciones ', 1);

INSERT INTO `evaluations` (`id`, `first_percentage`, `description_first_percentage`, `second_percentage`, `description_second_percentage`, `third_percentage`, `description_third_percentage`, `syllabus_id`) VALUES
(1, 30, 'Parciales y tareas', 30, 'Proyectos y tareas', 40, 'Parcial final', 4),
(2, 30, 'Parciales y tareas', 30, 'Proyectos y tareas', 40, 'Parcial final', 1),
(3, 30, 'Parciales y tareas', 30, 'Proyectos y tareas', 40, 'Parcial final', 2),
(6, 100, 'Unico parcial', NULL, NULL, NULL, NULL, 3);

INSERT INTO `faculties_subjects` (`id`, `faculties_id`, `subjects_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4);

INSERT INTO `programs_subjects` (`id`, `programs_id`, `subjects_id`) VALUES
(1, 1, 3),
(2, 1, 1),
(3, 1, 2),
(4, 1, 4),
(5, 2, 3);

INSERT INTO `users_programs` (`id`, `users_id`, `programs_id`) VALUES
(1, 3, 2),
(2, 3, 1),
(3, 2, 1);

INSERT INTO `users_subjects` (`id`, `users_id`, `subjects_id`) VALUES
(1, 3, 3),
(2, 2, 1),
(3, 2, 2),
(4, 2, 4),
(5, 3, 4);
