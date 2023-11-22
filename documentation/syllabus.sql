INSERT INTO `faculties` (`id`, `name`) VALUES
(1, 'Ingeniería');

INSERT INTO `subjects` (`id`, `name`, `modality`, `type`, `credits`, `semester`, `bibliography`) VALUES
(1, 'Ingeniería del Software II', 'presencial', 'teorica', 2, '1', NULL),
(2, 'Programación Web', 'presencial', 'practica', 2, '2', NULL),
(3, 'Metodos numericos', 'presencial', 'teorico-practica', 4, '3', NULL);

INSERT INTO `syllabi` (`id`, `date`, `program`, `cycle`, `justification`, `competences`, `learning_results`, `methodology`, `subject_id`, `faculty_id`) VALUES
(1, '2023-11-21 13:49:53', 'INGENIERÍA DE SISTEMAS', 'PROFESIONAL', 'Después de revisar y aplicar los conceptos previos de las fases de Ingeniería de Software (Análisis y Diseño de Sistemas), es indispensable para el estudiante comprender y desarrollar mecanismos para construir e implementar la aplicación que permitirá solucionar los problemas identificados en la fase de análisis y convertir las estructuras definidas en la fase de diseño en una solución práctica, probada y documentada lista para ser usada por los usuarios\r\n          ', '- Competencias básicas: Comunicar asertivamente las diferentes propuestas para dar solución a las necesidades organizacionales que enfrenta el ingeniero de sistemas.\r\n- Competencias genéricas: Reconocer y respetar los puntos de vistas y opiniones de otros miembros del grupo y llegar a acuerdos, para obtener los mejores resultados trabajando en equipo.\r\n- Competencias específicas: Diseñar, Desarrollar, seleccionar y evaluar aplicaciones y sistemas informáticos, asegurando su fiabilidad, seguridad y calidad conforme a los principios éticos y a la legislación y normativa vigente.\r\n- Competencias específicas: Identificar estándares para creación de prototipos en interfaces de usuarios\r\n- Competencias específicas: Identificar los diferentes tipos de pruebas que se le deben realizar a los sistemas de información para diseñar y aplicar el plan de pruebas.\r\n- Competencias específicas: Identificar las pautas de documentación para la construcción de un sistema de información', 'RA_4:\r\nComunica efectivamente en forma oral, gráfica y por escrito usando un lenguaje técnico.\r\nRA_7:\r\nDiseña procesos, productos y servicios basados en tecnología, software e información para el beneficio de los diferentes sectores socioeconómicos.\r\nRA_8:\r\nAnaliza criterios de selección y configura plataformas tecnológicas para el desarrollo y ejecución de aplicaciones y servicios informáticos.\r\nRA_10:\r\nAplica técnicas, principios y herramientas para el desarrollo de habilidades que fortalezcan el aprendizaje autónomo\r\n          ', '**TRABAJO PRESENCIAL**\r\nLos conocimientos de la asignatura se adquieren a través del estudio razonado de todas las unidades didácticas de la asignatura, previa presentación del docente, ejemplos y ejercicios en clases, así como del material didáctico que se ponga a disposición de los estudiantes en \r\nla plataforma Moodle.\r\n**TRABAJO INDEPENDIENTE**\r\nLos estudiantes tendrán talleres y trabajos prácticos e investigativos sobre los temas vistos en clases que puedan realizar durante las horas independientes asignadas para la materia.\r\n          \r\nen clases que puedan realizar durante las horas independientes asignadas para la materia.', 1, 1);

INSERT INTO `contents_and_strategies` (`id`, `content_name`, `sub_content`, `strategies`, `syllabus_id`) VALUES
(1, 'Ingeniería de Sistemas', 'o Jerarquía de la Ingeniería de Software\r\no Ingeniería de procesos de negocios\r\no Ingeniería del producto\r\no Modelado del Sistema', ' Talleres en clase, \r\n Ejercicios en clase, \r\n Quices, \r\n Trabajo independiente del estudiante, \r\n Participación del estudiante, \r\n Examen individual\r\n Exposiciones\r\n', 1);

INSERT INTO `evaluations` (`id`, `first_percentage`, `description_first_percentage`, `second_percentage`, `description_second_percentage`, `third_percentage`, `description_third_percentage`, `syllabus_id`) VALUES
(1, 30, 'Evaluación formativa (20%): Talleres, exposiciones, Quices\r\nParcial teórico (25%) y práctico (25%)\r\nProyecto de aula (30%)', 30, 'Evaluación formativa (20%): Talleres, exposiciones, Quices\r\nParcial teórico (25%) y práctico (25%', 40, 'Evaluación formativa (20%): Talleres, exposiciones, Quices\r\nParcial teórico (25%) y práctico (25%)\r\nProyecto de aula (30%)\r\n', 1);

INSERT INTO `faculties_subjects` (`id`, `faculties_id`, `subjects_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3);

INSERT INTO `users` (`id`, `name`, `email`, `password`, `role`, `status`, `faculty_id`) VALUES
(1, 'Decanatura', 'decanatura-baq@unilibre.edu.co', 'decanatura', 'admin', 1, 1),
(2, 'Rol teacher', 'teacher@unilibre.edu.co', 'teacher', 'teacher', 1, 1);

INSERT INTO `users_subjects` (`id`, `users_id`, `subjects_id`) VALUES
(1, 2, 1),
(2, 2, 3),
(3, 1, 1);

INSERT INTO `versions` (`id`, `update_date`, `description`, `user_id`, `syllabus_id`) VALUES
(1, '2023-11-21 22:16:38', 'Cambio de prueba 1', 2, 1),
(2, '2023-11-01 16:16:38', 'Cambio de prueba 2', 2, 1);
